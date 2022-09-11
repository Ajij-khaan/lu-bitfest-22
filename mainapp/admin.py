from django.contrib import admin
from .models import TransportUser, ConsumerUser

# Register your models here.


@admin.register(TransportUser)
class TransportUserAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ConsumerUser)
class ConsumerUserAdmin(admin.ModelAdmin):
    list_display = ['id']
