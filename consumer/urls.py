import imp
from django.urls import path
from .views import *

urlpatterns = [

    path("", HomeConsumerView.as_view(), name="home_consumer"),
    path('addprofile', AddProfileView.as_view(), name="addprofile"),
    path('showprofilfe', showprofilfe, name="showprofilfe"),

]
