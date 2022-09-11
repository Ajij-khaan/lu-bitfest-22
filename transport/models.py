from pyexpat import model
from statistics import mode
from tkinter import CASCADE
from typing import ValuesView
from django.db import models
from mainapp.models import TransportUser, ConsumerUser

# Create your models here.
Choice_Type = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Staff', 'Staff'),
)

Pickup_time = (
    ('8 AM', '8 AM'),
    ('9 AM', '9 AM'),
    ('10 AM', '10 AM'),
    ('11 AM', '11 AM'),
    ('12 PM', '12 PM'),
    ('1 PM', '1 PM'),

)


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

Pickup_time = (
    ('8 AM', '8 AM'),
    ('9 AM', '9 AM'),
    ('10 AM', '10 AM'),
    ('11 AM', '11 AM'),
    ('12 PM', '12 PM'),
    ('1 PM', '1 PM'),

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
    start_time = models.CharField(
        max_length=20, choices=Pickup_time, default='8 AM')

    def __str__(self):
        return f"Route - {self.Route_Number}- Time: {self.start_time}"


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


class SendMeessage(models.Model):
    request_user = models.ForeignKey(ConsumerUser, on_delete=models.CASCADE)

    root = models.ForeignKey(RouteInfo, on_delete=models.CASCADE)

    message = models.TextField()


class NumberOfPassenger(models.Model):
    role = models.CharField(
        max_length=20, choices=Choice_Type, default='Student')

    numberofpass = models.IntegerField()
    mainslot = models.ForeignKey(
        RouteInfo, on_delete=models.CASCADE, related_name="time_view")
    date_time = models.DateTimeField(auto_now_add=True)


class BusStopage(models.Model):
    route_number = models.IntegerField()
    label = models.CharField(
        max_length=20, choices=Pickup_type, default='Tilagor')
    lattitude = models.CharField(max_length=120)
