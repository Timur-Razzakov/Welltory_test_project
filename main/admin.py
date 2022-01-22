from django.contrib import admin
from django import forms
from django.template.defaultfilters import truncatechars
from .models import *


class AdminForm(forms.ModelForm):
    class Meta:
        model = Correlation
        fields = '__all__'


class CorrelationAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'x_data_type',
        'y_data_type',
        'value',
        'p_value')  # исл для показа каких либо данных в админке

    save_as = False  # добавляет кнопку "сохранить как новый объект" в админке
    # search_fields = ('user_id')  # поиск по айди и по дате


class First_parameterAdmin(admin.ModelAdmin):
    list_display = ('id','x_value', 'date_for_the_first', 'created_at')


class Second_parameterAdmin(admin.ModelAdmin):
    list_display = ('id','y_value', 'date_for_the_second', 'created_at')


class DataAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'x_data_type', 'y_data_type', 'created_at')


admin.site.register(Correlation, CorrelationAdmin)
admin.site.register(First_parameter, First_parameterAdmin)
admin.site.register(Second_parameter, Second_parameterAdmin)
admin.site.register(Error)
admin.site.register(Data, DataAdmin)
