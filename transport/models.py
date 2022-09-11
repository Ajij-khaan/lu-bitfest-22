from django.db import models

# Create your models here.


class BusInfo(models.Model):
    license_number = models.CharField(max_length=100)
    codename = models.CharField(max_length=100)
    capacity = models.IntegerField()
    drive_name = models.CharField(max_length=100)
    driver_contact = models.IntegerField()
    is_active = models.BooleanField()
