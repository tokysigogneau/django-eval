from django.contrib import admin

from .models import Service, Reservation, Skill, UserSkill

class ServiceAdmin (admin.ModelAdmin):
    list_display = ["service_owner", "service_skill", "is_available"]

class ReservationAdmin (admin.ModelAdmin):
    list_display = ["reservation_title","service_owner", "service_client"]

admin.site.register(Service,ServiceAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Skill)
admin.site.register(UserSkill)