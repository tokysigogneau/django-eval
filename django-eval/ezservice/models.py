from django.contrib.auth.models import User
from django.db import models

class Service(models.Model):
    service_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    date = models.DateTimeField ("service_date")
    description = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation (models.Model):
    reservation_title = models.CharField(max_length=200)
    #related name is necessary or else it will not work, the FK need to be different
    service_owner = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='owner_reservation')
    service_client = models.ForeignKey(User, default='1',on_delete=models.CASCADE, related_name='client_reservation')

    def __str__(self):
        return self.reservation_title