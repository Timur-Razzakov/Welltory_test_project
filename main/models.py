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
    x_value = models.ManyToManyField(First_parameter, verbose_name='Значения для x')
    y_value = models.ManyToManyField(Second_parameter, verbose_name='Значения для y')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return str('{}:{}'.format(self.x_value, self.y_value))


"""   {
       "user_id": int,
       "x_data_type": str,
       "y_data_type": str,
       "correlation": {
           "value": float,
           "p_value": float,
       }
   }"""


class Correlation(models.Model):
    user_id = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    x_data_type = models.CharField(max_length=50, verbose_name='Вид данных_x')
    y_data_type = models.CharField(max_length=50, verbose_name='Вид данных_y')
    value = models.FloatField(verbose_name='коэффициент корреляции')
    p_value = models.FloatField(verbose_name='двухстороннее п-значение')

    class Meta:
        ordering = ['user_id']

    def __str__(self):
        return self.user_id


# class Correlation(models.Model):
#     title = models.CharField(max_length=90, verbose_name='Наименование')
#
#     slug = models.SlugField(verbose_name='url', unique=True, max_length=90)
#     created_at = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
#     first_parameter = models.ForeignKey(First_parameter,
#                                         on_delete=models.CASCADE, verbose_name='x_value')
#     second_parameter = models.ForeignKey(Second_parameter,
#                                          on_delete=models.CASCADE, verbose_name='y_value')
#     result = models.CharField(max_length=255, verbose_name='Результат Корреляции')
#
#     class Meta:
#         ordering = ['-created_at']
#
#     def __str__(self):
#         return self.title


class Error(models.Model):
    created_at = models.DateField(auto_now_add=True)
    data = models.JSONField()

    def __str__(self):
        return str(self.created_at)
