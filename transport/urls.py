import imp
from django.urls import path
from transport.views import *

urlpatterns = [

    path('', home, name="hometransport"),

]
