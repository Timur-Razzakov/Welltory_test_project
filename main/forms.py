from django import forms

from .models import First_parameter, Second_parameter, Data


class Parameters_Form(forms.Form):
    date = forms.DateField(
        required=True, widget=forms.DateInput(attrs={
            'class': 'form-control', 'type': 'date'}),
        label='Дата'
    )
    x_data_type = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Вид первого значения'
    )
    y_data_type = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Вид второго значение'
    )


class AddDataForm(forms.Form):
    x_data_type = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Вид первого значения'
    )
    y_data_type = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Вид второго значение'
    )

    first_parameter = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Первое значение'
    )

    second_parameter = forms.CharField(
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Второе значение'
    )
    date = forms.DateField(
        required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Дата'
    )

    # def clean_second_parameter(self):
    #     second_parameter = self.cleaned_data['second_parameter'].split(',')
    #     first_parameter = self.cleaned_data['first_parameter'].split(',')
    #     first_parameter = [float(item_x) for item_x in first_parameter]
    #     second_parameter = [float(item_y) for item_y in second_parameter]
    #     if len(second_parameter) != len(first_parameter):
    #         raise ValidationError('Значения должны быть одинакового количества')
    #     return second_parameter
