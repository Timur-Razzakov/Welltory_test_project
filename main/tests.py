
# Create your tests here.

from icecream import ic
# from scipy.stats import linregress
#
a = ('15', '12', '8', '8', '7', '7', '7', '6', '5', '3')
a.split(',')
# b = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

ic(a)
#
# ic(linregress(a, b))











def new_value(request):
    if request.method == 'POST':
        value_form = AddDataForm(data=request.POST or None)
        if value_form.is_valid():
            data = value_form.cleaned_data
            first_parameter = data.get('first_parameter')
            second_parameter = data.get('second_parameter')
            x_data_type = data.get('x_data_type')
            y_data_type = data.get('y_data_type')
            date_for_the_first = data.get('date')
            date_for_the_second = data.get('date')
            # Проверка есть ли эти данные в бд
            qs = Error.objects.filter(created_at=dt.date.today())
            if qs.exists():
                err = qs.first()
                # Превращаем в словарь
                data = literal_eval(err.data.replace('user_data:', ''))
                data = {'user_data': data}
                data.update({'first_parameter': first_parameter,
                             'second_parameter': second_parameter,
                             'date_for_the_first': date_for_the_first,
                             'date_for_the_second': date_for_the_second,
                             'y_data_type': y_data_type,
                             'x_data_type': x_data_type, })
                ic(data)
                ic(err.data)
                err.data['user_data'] = data
                ic(err)
                ic(type(err))
                err.save()
            else:
                data = [{'first_parameter': first_parameter,
                         'second_parameter': second_parameter,
                         'date_for_the_first': date_for_the_first,
                         'date_for_the_second': date_for_the_second,
                         'y_data_type': y_data_type,
                         'x_data_type': x_data_type}]

                Error(data=f"user_data:{data}").save()
            messages.success(request, 'Данные отправлены.')
            return redirect('show_form')
        else:
            return redirect('home')
    return redirect('count_up')
