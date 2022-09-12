import imp
from django.urls import path
from transport.views import *


urlpatterns = [

    path('', BusHomeView.as_view(), name="hometransport"),
    path('addbus', AddBusView.as_view(), name="addbus"),
    path('updatebus/<int:id>/', EditBusInfo.as_view(), name="updatebus"),
    path('deletebus/<int:id>/', DeleteBusInfo.as_view(), name="deletebus"),
    path('allroute', RouteallView.as_view(), name="allroute"),
    path('addroute', AddRouteView.as_view(), name="addroute"),
    path('updateroute/<int:id>/', EditRouteInfo.as_view(), name="updateroute"),
    path('deleteroute/<int:id>/', DeleteRouteInfo.as_view(), name="deleteroute"),
    path('showrequest', ShowrequestView.as_view(), name="showrequest"),
    path('addmessage/<int:id>/', AddmessageView.as_view(), name="addmessage"),
    path('addpassview', AddpassView.as_view(), name="addpassview"),
    path('addbusstopage', AddBustopageView.as_view(), name="addbusstopage"),
    path('logout', logout, name="logout"),
    path('busstopageview', busstopageview, name="busstopageview"),
    path('NumberOfPassengerview', NumberOfPassengerview,
         name="NumberOfPassengerview"),
    path('editbusstopage/<int:id>/',
         EditBusstopageInfo.as_view(), name="editbusstopage"),
    path('deletebusstopage/<int:id>/',
         DeleteBusstopageInfo.as_view(), name="deletebusstopage"),
    path('editpasseneger/<int:id>/',
         EditPasenegerInfo.as_view(), name="editpasseneger"),
    path('deletepassinfo/<int:id>/',
         DeletePassenegerInfo.as_view(), name="deletepassinfo"),
]
