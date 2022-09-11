from statistics import mode
from django.db import models


Choice_Type = (
    ('Student', 'Student'),
    ('Teacher', 'Teacher'),
    ('Staff', 'Staff'),
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


class TransportUser(models.Model):
    username = models.CharField(max_length=100)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

    @staticmethod
    def get_transport_by_username(username):
        try:
            return TransportUser.objects.get(username=username)
        except:
            return False


class ConsumerUser(models.Model):
    role = models.CharField(
        max_length=20, choices=Choice_Type, default='Student')
    user_name = models.CharField(max_length=100)
    id_no = models.IntegerField(null=True, blank=True)
    contact_number = models.IntegerField()
    pickup_stopage = models.CharField(
        max_length=20, choices=Pickup_type, default='Surma Tower')
    password = models.CharField(max_length=100)
    cpassword = models.CharField(max_length=100)

    @staticmethod
    def get_consumer_by_username(user_name):
        try:
            return ConsumerUser.objects.get(user_name=user_name)
        except:
            return False
