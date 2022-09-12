from django.db import models
from transport.models import RouteInfo
from mainapp.models import ConsumerUser


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


class RequestBus(models.Model):
    user = models.ForeignKey(ConsumerUser, on_delete=models.CASCADE)
    root_bus = models.ForeignKey(
        RouteInfo, on_delete=models.CASCADE)
