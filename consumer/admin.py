from django.contrib import admin
from .models import RequestBus
# Register your models here.


@admin.register(RequestBus)

class RequestBusAdmin(admin.ModelAdmin):
    list_display = ['id']