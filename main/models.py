from django.db import models
from account.models import MyUser


#
class First_parameter(models.Model):
    x_value = models.FloatField(verbose_name='Значение')
    date_for_the_first = models.DateField(verbose_name='Дата')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str(self.x_value)


class Second_parameter(models.Model):
    y_value = models.FloatField(verbose_name='Значение')
    date_for_the_second = models.DateField(verbose_name='Дата')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str(self.y_value)


class Data(models.Model):
    user_id = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    x_data_type = models.CharField(max_length=50, verbose_name='Вид данных_x')
    y_data_type = models.CharField(max_length=50, verbose_name='Вид данных_y')
    x_value = models.ForeignKey(First_parameter, verbose_name='Значения для x', on_delete=models.CASCADE)
    y_value = models.ForeignKey(Second_parameter, verbose_name='Значения для y', on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name='Дата создания')

    def __str__(self):
        return str(self.user_id)


class Correlation(models.Model):
    user_id = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    x_data_type = models.CharField(max_length=50, verbose_name='Вид данных_x')
    y_data_type = models.CharField(max_length=50, verbose_name='Вид данных_y')
    value = models.FloatField(verbose_name='коэффициент корреляции')
    p_value = models.FloatField(verbose_name='двухстороннее п-значение')

    class Meta:
        ordering = ['user_id']

    def __str__(self):
        return str(self.user_id)


class Error(models.Model):
    created_at = models.DateField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.created_at)
