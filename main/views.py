from django.contrib import messages
from django.shortcuts import render, redirect
import numpy

# Create your views here.
from icecream import ic
import datetime as dt

from .forms import Parameters_Form, AddDataForm
from .models import Error, Data, First_parameter

# для превращения строки в дикт
from ast import literal_eval


# numpy.corrcoef(list1, list2)[0, 1]

def home_view(request):
    return render(request, 'main/home.html')


def count_view(request):
    form = Parameters_Form()

    return render(request, 'main/count_up.html', {'form': form})


def show_form(request):
    form = AddDataForm()
    return render(request, 'main/add_param.html', {'form': form})


"""func for add new parameter in our db"""


#
# def new_value(request):
#     if request.method == 'POST':
#         value_form = AddDataForm(data=request.POST or None)
#         if value_form.is_valid():
#             data = value_form.cleaned_data
#             first_parameter = data.get('first_parameter')
#             second_parameter = data.get('second_parameter')
#             date = data.get('date')
#             qs = Error.objects.filter(created_at=dt.date.today())
#             if qs.exists():
#                 err = qs.first()
#                 ic((err.data))
#                 data = err.data.get('user_data', [])
#                 data.append({'first_parameter': first_parameter,
#                              'second_parameter': second_parameter, 'date': date})
#                 err.data['user_data'] = data
#                 err.save()
#             else:
#                 data = [{'first_parameter': first_parameter,
#                          'second_parameter': second_parameter, 'date': date}]
#                 Error(data=f"user_data:{data}").save()
#             messages.success(request, 'Данные отправлены.')
#             return redirect('add_param')
#         else:
#             return redirect('add_param')
#     return redirect('add_param')


# def new_value(request):
#     if request.method == 'POST':
#         value_form = AddDataForm(request.POST)
#         if value_form.is_valid():
#             data = value_form.cleaned_data
#             x_value = data.get('first_parameter').split(',')
#             y_value = data.get('second_parameter').split(',')
#             x_data_type = data.get('x_data_type')
#             y_data_type = data.get('y_data_type')
#             date_for_the_first = data.get('date')
#             date_for_the_second = data.get('date')
#             table = x_data_type, y_data_type
#             ic(table)
#             if table is not None:
#                 data_table = table
#                 ic(data_table)
#             else:
#                 data_table = Data.save(x_data_type, y_data_type)
#                 ic(data_table)
#             first_parameter = [float(item) for item in x_value]
#             second_parameter = [float(item) for item in y_value]
#             # TODO: дописать сохранение в бд
#             for x, y in zip(first_parameter, second_parameter):
#                 data_table.objects.get('pk')
#                 pass
#
#             messages.success(request, 'Данные отправлены')
#             return redirect('show_form')
#         else:
#             return redirect('home')
#     return redirect('count_up')


def new_value(request):
    if request.method == 'POST':
        value_form = AddDataForm(request.POST)
        if value_form.is_valid():
            # data = Data.objects.create(**value_form.cleaned_data)
            data = value_form.save()
            # x_value = data.get('first_parameter').split(',')
            # y_value = data.get('second_parameter').split(',')
            # x_data_type = data.get('x_data_type')
            # y_data_type = data.get('y_data_type')
            # date_for_the_first = data.get('date')
            # date_for_the_second = data.get('date')
            #
            # table = x_data_type, y_data_type
            # ic(table)
            # if table is not None:
            #     data_table = table
            #     ic(data_table)
            # else:
            #     data_table = Data.save(x_data_type, y_data_type)
            #     ic(data_table)
            # first_parameter = [float(item) for item in x_value]
            # second_parameter = [float(item) for item in y_value]
            # # TODO: дописать сохранение в бд
            # for x, y in zip(first_parameter, second_parameter):
            #     data_table.objects.get('pk')
            #     pass

            messages.success(request, 'Данные отправлены')
            return redirect('show_form')
        else:
            return redirect('home')
    return redirect('count_up')

