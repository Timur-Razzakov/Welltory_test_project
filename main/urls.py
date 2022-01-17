from django.urls import path
from .views import *

# app_name = 'account'

urlpatterns = [
    path('', home_view, name='home'),
    path('count_up/', count_view, name='count_up'),
    path('add_param/', new_value, name='add_param'),
    path('show_form/', show_form, name='show_form'),
    path('show_data/', show_all_data, name='show_data'),
    path('show_result/', show_all_results, name='show_result'),

]
