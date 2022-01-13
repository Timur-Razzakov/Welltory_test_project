from django import forms
from django.forms import ModelForm, Textarea
from .models import First_parameter, Second_parameter, Data


class Parameters_Form(forms.Form):
    date_for_the_first = forms.CharField(label='Дата', widget=forms.DateInput(
        attrs={'class': 'form-control'}))

    first_parameter = forms.ModelChoiceField(
        queryset=First_parameter.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Первое значение'
    )

    second_parameter = forms.ModelChoiceField(
        queryset=Second_parameter.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Второе значение'
    )

    class Meta:
        model = First_parameter
        fields = '__all__'


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
