from django.contrib.auth.models import User
from django.db import models

class Reservation (models.Model):
    service_owner = models.ForeignKey(User, on_delete=models.CASCADE())
    service_client = models.ForeignKey(User, on_delete=models.CASCADE())


class Service(models.Model):
    service_owner = models.ForeignKey(User, on_delete=models.CASCADE())
    name = models.CharField(max_length=200)
    date = models.DateTimeField ("service_date")
    description = models.CharField(max_length=200)



