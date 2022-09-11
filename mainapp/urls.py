import imp
from django.contrib import admin
from django.urls import path
from mainapp.views import *

app_name = 'mainapp'

urlpatterns = [
    path('', LoginTransportView.as_view(), name='home'),
    path('transport_register', RegisterTransportView.as_view(),
         name='transport_register'),
    path('consumer_login', LoginConsumerView.as_view(), name='consumer_login'),
    path('consumer_register', RegisterConsumerView.as_view(),
         name='consumer_register'),
]
