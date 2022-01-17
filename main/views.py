from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import pickle
from django.http import JsonResponse
from django.shortcuts import render, redirect
from icecream import ic

from .forms import Parameters_Form, AddDataForm
from .models import Data, First_parameter, Second_parameter, Correlation
from account.models import MyUser


# TODO: выводить messages выводить в цвете
# TODO: Дописать добавление списка в мани ту мани
# TODO: настроить Селери для расчета  в фоновых процессах
# TODO: разобраться как из id получить значения из мани ту мани
# TODO: Засунуть всё это в докер #Done
# TODO: получить x_value and y_value при подсчёте DONE
# TODO: Перенести подсчёт корреляции в отдельную функцию #done
# https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/
# https://gist.github.com/sancau/41b11ddb5ffce1d0ae90d1df8948d0b1
# https://django.fun/tutorials/select_related-i-prefetch_related-v-django/

def home_view(request):
    return render(request, 'main/home.html')


# Функция для подсчёта
def count_view(request):
    form = Parameters_Form()
    if request.method == 'POST':
        value_form = Parameters_Form(request.POST)
        if value_form.is_valid():
            data = value_form.cleaned_data
            x_data_type = data.get('x_data_type')
            y_data_type = data.get('y_data_type')
            date = data.get('date')
        get_value = Data.objects.filter(
            created_at=date,
            x_data_type=x_data_type,
            y_data_type=y_data_type
        ).select_related('user_id',
                         'x_value',
                         'y_value'
                         ).values_list('user_id',
                                       'x_value',
                                       'y_value',
                                       'id')
        if get_value.exists():
            ic(get_value)

            # list_value = list(get_value)
            # x_value = []
            # y_value = set()
            # for dicts in list_value:
            #     for key, value in dicts.items():
            #         if key == 'user_id':
            #             user_id = value
            #         elif key == 'x_value':
            #             x_value.append(value)
            #         else:
            #             y_value.add(value)
            #             break
            # ic(user_id)
            # ic(len(x_value))
            # ic(len(y_value))
            # cor, p_value = pearsonr(first_parameter, second_parameter)
            # Correlation(
            #     user_id=user,
            #     x_data_type=x_data_type,
            #     y_data_type=y_data_type,
            #     value=cor,
            #     p_value=p_value
            # ).save()
        else:
            print('sdafasdfsdafsdafs')

    return render(request, 'main/count_up.html', {'form': form})


# Функция для запроса всех данных

# Второй варианты вывода данных
# def get_all_data(request):
#     if request.method == "POST":
#         data = Data.objects.all()
#         qs_json = serializers.serialize('json', data)
#     return render(request, 'main/show_data.html', {'dataset': qs_json})

# Функция для вывода всех данных в виде JSON формата
def show_all_data(request):
    data = list(Data.objects.values())
    return JsonResponse(data, safe=False)


# Функция для вывода результата в виде JSON формата
def show_all_results(request):
    data = list(Correlation.objects.values())
    return JsonResponse(data, safe=False)


# Функция для вывода формы, которая служит для заполнения данными
def show_form(request):
    form = AddDataForm()
    return render(request, 'main/add_param.html', {'form': form})


# Функция для добавления новых значений для корреляции
def new_value(request):
    ic(request.method)
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
            ic(second_parameter)
            table = Data.objects.filter(x_data_type=x_data_type, y_data_type=y_data_type)

            if len(first_parameter) == len(second_parameter):
                for first_item, second_item in zip(first_parameter, second_parameter):
                    first_value = First_parameter(x_value=first_item, date_for_the_first=date).save()
                    second_value = Second_parameter(y_value=second_item, date_for_the_second=date).save()
                if table.exists():  # если существует
                    data_table = table
                    ic(data_table)
                else:
                    Data(
                        user_id=user,
                        x_data_type=x_data_type,
                        y_data_type=y_data_type,
                        created_at=date,
                        x_value=first_value,
                        y_value=second_value
                    ).save()

                    # for first_item, second_item in zip(first_parameter, second_parameter):
                    #     first_value = Data.x_value.create(x_value=first_item)
                    #     second_value = Data.y_value.create(y_value=second_item)
                    #     First_parameter(date_for_the_first=date).save()
                    #     Second_parameter(date_for_the_second=date).save()
                    #     ic(first_value)
                    #     ic(second_value)

                data_table.x_value = First_parameter.pk
                data_table.y_value = Second_parameter.pk
                messages.success(request, 'Данные отправлены')
                return redirect('show_form')
            else:
                messages.warning(request, 'Значения должны быть одинакового количества')
                return redirect('show_form')
        else:
            messages.error(request, 'Данная форма невалидна')
            return redirect('show_form')
    messages.error(request, 'Ошибка в методе запроса')
    # return render(request, 'main/add_param.html', {'form': form})
    return redirect('show_form')
