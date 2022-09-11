from django.db import models
from mainapp.models import TransportUser, ConsumerUser

# Create your models here.


Pickup_type = (
    ('Tilagor', 'Tilagor'),
    ('Balucor', 'Balucor'),
    ('Eidgah', 'Eidgah'),
    ('Electric Supply', 'Electric Supply'),
    ('Amberkhana', 'Amberkhana'),
    ('Subid Bazar', 'Subid Bazar'),
    ('Madina Market', 'Madina Market'),
    ('Akhalia', 'Akhalia'),
    ('Sust Gate', 'Sust Gate'),
    ('Temukhi', 'Temukhi'),
    ('Kamal Bazar', 'Kamal Bazar'),
    ('Surma Tower', 'Surma Tower'),
    ('Lamabazar', 'Lamabazar'),
    ('Rikabi Bazar', 'Rikabi Bazar'),
    ('Humayun Cattar', 'Humayun Cattar'),
    ('Sibgonj', 'Sibgonj'),

)


Choice_deaprtment = (
    ('CSE', 'CSE'),
    ('EEE', 'EEE'),
    ('Civil', 'Civil'),
    ('BBA', 'BBA'),
    ('Law', 'Law'),
    ('Architecture', 'Architecture'),
    ('English', 'English'),
)


class BusInfo(models.Model):
    license_number = models.CharField(max_length=100)
    codename = models.CharField(max_length=100)
    capacity = models.IntegerField()
    drive_name = models.CharField(max_length=100)
    driver_contact = models.IntegerField()
    is_active = models.BooleanField(default=False)


class RouteInfo(models.Model):
    Route_Number = models.IntegerField()
    label = models.CharField(
        max_length=20, choices=Pickup_type, default='Tilagor')
    lattitude = models.FloatField()
    start_time = models.TimeField(auto_now=False, auto_now_add=False)


class UpdateTransportProfile(models.Model):
    user_transport = models.OneToOneField(
        ConsumerUser, on_delete=models.CASCADE, blank=True, )
    department = models.CharField(
        max_length=100, choices=Choice_deaprtment, default='CSE')
    codename = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)


class UpdateStudentProfile(models.Model):
    user_consumer = models.OneToOneField(
        ConsumerUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    batch = models.IntegerField()
    section = models.CharField(max_length=100)
