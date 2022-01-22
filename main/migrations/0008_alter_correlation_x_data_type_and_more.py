# Generated by Django 4.0.1 on 2022-01-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_data_x_value_data_x_value_remove_data_y_value_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correlation',
            name='x_data_type',
            field=models.CharField(max_length=50, verbose_name='Тип данных для X'),
        ),
        migrations.AlterField(
            model_name='correlation',
            name='y_data_type',
            field=models.CharField(max_length=50, verbose_name='Тип данных для Y '),
        ),
        migrations.AlterField(
            model_name='data',
            name='x_data_type',
            field=models.CharField(max_length=50, verbose_name='Тип данных_x'),
        ),
        migrations.RemoveField(
            model_name='data',
            name='x_value',
        ),
        migrations.AddField(
            model_name='data',
            name='x_value',
            field=models.ManyToManyField(to='main.First_parameter', verbose_name='Значения для x'),
        ),
        migrations.AlterField(
            model_name='data',
            name='y_data_type',
            field=models.CharField(max_length=50, verbose_name='Тип данных_y'),
        ),
        migrations.RemoveField(
            model_name='data',
            name='y_value',
        ),
        migrations.AddField(
            model_name='data',
            name='y_value',
            field=models.ManyToManyField(to='main.Second_parameter', verbose_name='Значения для y'),
        ),
    ]