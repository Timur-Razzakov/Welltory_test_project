from django.urls import path
from .views import *

# app_name = 'account'

urlpatterns = [
    path('', home_view, name='home'),
    path('count_up/', count_view, name='count_up'),
    path('add_param/', new_value, name='add_param'),
    # form for add new_value
    path('show_form/', show_form, name='show_form'),

]
