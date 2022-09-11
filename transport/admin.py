from django.contrib import admin
from .models import BusInfo
# Register your models here.


@admin.register(BusInfo)
class BusInfoAdmin(admin.ModelAdmin):
    list_display = ['id']
