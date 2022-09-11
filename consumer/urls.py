import imp
from django.urls import path
from .views import *


urlpatterns = [

    path("", HomeConsumerView.as_view(), name="home_consumer"),
    path('addprofile', AddProfileView.as_view(), name="addprofile"),
    path('showprofilfe', showprofilfe, name="showprofilfe"),
    path('busrequest', RequestBusView.as_view(), name="busrequest"),
    path('notifiactionbus', notifiactionbus, name="notifiactionbus"),
    path('notdelete/<int:id>/', notdelete, name="notdelete"),
    path('number_of_passeneger', number_of_passeneger,
         name="number_of_passeneger"),

]
