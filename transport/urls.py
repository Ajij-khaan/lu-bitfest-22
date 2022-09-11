import imp
from django.urls import path
from transport.views import *


urlpatterns = [

    path('', BusHomeView.as_view(), name="hometransport"),
    path('addbus', AddBusView.as_view(), name="addbus"),
    path('updatebus/<int:id>/', EditBusInfo.as_view(), name="updatebus"),
    path('deletebus/<int:id>/', DeleteBusInfo.as_view(), name="deletebus"),

]
