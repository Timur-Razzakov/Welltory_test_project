from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, redirect
from itertools import chain  # для сбора кортежа в один список

from icecream import ic

from .tasks import correlation_calculation

from .forms import Parameters_Form, AddDataForm
from .models import Data, First_parameter, Second_parameter, Correlation
from account.models import MyUser


# TODO: выводить messages выводить в цвете


def home_view(request):
    return render(request, 'main/home.html')


# Функция для подсчёта
def count_view(request):
    global user_id, second_value, first_value
    form = Parameters_Form()
    if request.method == 'POST':
        value_form = Parameters_Form(request.POST)
        if value_form.is_valid():
            data = value_form.cleaned_data
            x_data_type = data.get('x_data_type')
            y_data_type = data.get('y_data_type')
            date = data.get('date')
        get_value = Data.objects.filter(x_data_type=x_data_type,
                                        y_data_type=y_data_type,
                                        created_at=date).prefetch_related('x_value', 'y_value')
        if get_value.exists():
            list_value = list(get_value)
            # получаем x_val и y_val
            for item in list_value:
                user_id = item.user_id
                x_val = item.x_value.values_list('x_value')
                y_val = item.y_value.values_list('y_value')
                # затем собираем кортеж в один список
                first_value = list(chain.from_iterable(x_val))
                second_value = list(chain.from_iterable(y_val))
            # производим вычисление delay--говорит, о том что это таск и не ждёт
            correlation_calculation.delay(
                first_value,
                second_value,
                x_data_type,
                y_data_type, )
            messages.success(request, 'Вычисляем...\n'
                                      '(Результат можете посмотреть в разделе\n'
                                      '"Вывести результат")')

        else:
            messages.error(request, 'Данная форма невалидна')
            return redirect('count_up')

    return render(request, 'main/count_up.html', {'form': form})


# Функция для вывода всех данных в виде JSON формата
def show_all_data(request):
    data = list(Data.objects.prefetch_related('x_value', 'y_value').values())

    return JsonResponse(data, safe=False)


# Функция для вывода результата в виде JSON формата
def show_all_results(request):
    data = list(Correlation.objects.values())
    return JsonResponse(data, safe=False)


# Функция для добавления новых значений для корреляции
def new_value(request):
    form = AddDataForm()
    if request.method == 'POST':
        value_form = AddDataForm(request.POST)
        if value_form.is_valid():
            data = value_form.cleaned_data
            x_value = data.get('first_parameter').split(',')
            y_value = data.get('second_parameter').split(',')
            x_data_type = data.get('x_data_type')
            y_data_type = data.get('y_data_type')
            date = data.get('date')
            # Получаем id пользователя
            try:
                user_id = request.user.id
                user = MyUser.objects.get(id=int(user_id))
            except ObjectDoesNotExist:
                user = MyUser.objects.create(id=user_id)
            # str-->float
            first_parameter = [float(item_x) for item_x in x_value]
            second_parameter = [float(item_y) for item_y in y_value]

            table = Data.objects.filter(x_data_type=x_data_type, y_data_type=y_data_type)

            if table.exists():  # если существует
                data_table = table
            else:
                data_table = Data.objects.create(
                    user_id=user,
                    x_data_type=x_data_type,
                    y_data_type=y_data_type,
                    created_at=date
                )
                if len(first_parameter) == len(second_parameter):
                    for first_item, second_item in zip(first_parameter, second_parameter):
                        first = First_parameter.objects.create(x_value=first_item, date_for_the_first=date)
                        second = Second_parameter.objects.create(y_value=second_item, date_for_the_second=date)
                        data_table.x_value.add(first)
                        data_table.y_value.add(second)
                    data_table.x_value.set(First_parameter.pk)
                    data_table.y_value.set(Second_parameter.pk)
                else:
                    messages.warning(request, 'Значения должны быть одинакового количества')
                    return redirect('add_param')

            messages.success(request, 'Данные отправлены')
            return redirect('add_param')
        else:
            messages.error(request, 'Данная форма невалидна')
            return redirect('add_param')
    return render(request, 'main/add_param.html', {'form': form})
