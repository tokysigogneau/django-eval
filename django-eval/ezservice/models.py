from django.contrib.auth.models import User
from django.db import models


class Reservation (models.Model):
    #related name is necessary or else it will not work, the FK need to be different
    service_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_reservation')
    service_client = models.ForeignKey(User, default='No one',on_delete=models.CASCADE, related_name='client_reservation')


class Service(models.Model):
    service_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField ("service_date")
    description = models.CharField(max_length=200)
