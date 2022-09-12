import imp
from django.urls import path
from .views import *


urlpatterns = [
    path('', number_of_passeneger,
         name="number_of_passeneger"),
    path("allrouts", HomeConsumerView.as_view(), name="allrouts"),
    path('addprofile', AddProfileView.as_view(), name="addprofile"),
    path('showprofilfe', showprofilfe, name="showprofilfe"),
    path('busrequest', RequestBusView.as_view(), name="busrequest"),
    path('notifiactionbus', notifiactionbus, name="notifiactionbus"),
    path('notdelete/<int:id>/', notdelete, name="notdelete"),



]
