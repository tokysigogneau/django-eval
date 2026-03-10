from django.contrib import admin

from .models import Service, Reservation, Skill, UserSkill

admin.site.register(Service)
admin.site.register(Reservation)
admin.site.register(Skill)
admin.site.register(UserSkill)