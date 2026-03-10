from django.contrib.auth.models import User
from django.db import models


class Skill (models.Model):
    skill_name = models.CharField(max_length=200)

    def __str__(self):
        return self.skill_name

class UserSkill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Service(models.Model):
    service_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    service_skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    date = models.DateTimeField ("service_date")
    description = models.CharField(max_length=400)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.service_owner.username


class Reservation (models.Model):
    reservation_title = models.CharField(max_length=200)
    #related name is necessary or else it will not work, the FK need to be different
    service_owner = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='owner_reservation')
    service_client = models.ForeignKey(User, default='1',on_delete=models.CASCADE, related_name='client_reservation')

    def __str__(self):
        return self.reservation_title