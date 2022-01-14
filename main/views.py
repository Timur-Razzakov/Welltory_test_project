from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from scipy.stats import pearsonr
from icecream import ic

from .forms import Parameters_Form, AddDataForm
from .models import Data, First_parameter, Second_parameter, Correlation
from account.models import MyUser


def home_view(request):
    return render(request, 'main/home.html')


# Функция для подсчёта
def count_view(request):
    form = Parameters_Form()

    return render(request, 'main/count_up.html', {'form': form})


# Функция для вывода всех данных в виде JSON формата
def show_all_data(request):

    # qs = Data.objects.all()
    # qs_json = serializers.serialize('json', qs)
    # answer = HttpResponse(qs_json, content_type='application/json')
    # return HttpResponse()
    return render(request, 'main/show_data.html')


# Функция для вывода результата в виде JSON формата
def show_results(request):
    if request.method == 'Get':
        pass
    return render(request, 'main/show_result.html')


# Функция для вывода формы, которая служит для заполнения данными
def show_form(request):
    form = AddDataForm()
    return render(request, 'main/add_param.html', {'form': form})


# Функция для добавления новых значений для корреляции
def new_value(request):
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

            first_parameter = [float(item) for item in x_value]
            second_parameter = [float(item) for item in y_value]
            table = Data.objects.filter(x_data_type=x_data_type, y_data_type=y_data_type)

            if table.exists():
                data_table = table
            else:
                data_table = Data(
                    user_id=user,
                    x_data_type=x_data_type,
                    y_data_type=y_data_type,
                    x_value=x_value,
                    y_value=y_value
                ).save()

            if len(first_parameter) == len(second_parameter):

                for first_item, second_item in zip(first_parameter, second_parameter):
                    First_parameter(x_value=first_item, date_for_the_first=date).save()
                    Second_parameter(y_value=second_item, date_for_the_second=date).save()

                    data_table.first_parameter = First_parameter.pk
                    data_table.second_parameter = Second_parameter.pk
                    # вычисляем корреляцию
                cor, p_value = pearsonr(first_parameter, second_parameter)
                Correlation(
                    user_id=user,
                    x_data_type=x_data_type,
                    y_data_type=y_data_type,
                    value=cor,
                    p_value=p_value
                ).save()
                messages.success(request, 'Данные отправлены')
                return redirect('show_form')
            else:
                messages.WARNING(request, 'Значения должны быть одинакового количества')
                return redirect('show_form')
        else:
            return redirect('home')
    return redirect('home')
