from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "ezservice"

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("<str:skill_name>/", views.service_owner, name="service_owner"),
]