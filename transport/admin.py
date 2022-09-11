from django.contrib import admin
from .models import BusInfo, RouteInfo, UpdateTransportProfile, UpdateStudentProfile, SendMeessage
# Register your models here.


@admin.register(BusInfo)
class BusInfoAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(RouteInfo)
class RouteInfoInfoAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(UpdateTransportProfile)
class UpdateTransportProfileInfoAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(UpdateStudentProfile)
class UpdateStudentProfileAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(SendMeessage)
class SendMeessageAdmin(admin.ModelAdmin):
    list_display = ['id']
