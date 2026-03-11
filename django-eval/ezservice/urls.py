from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "ezservice"

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("login/", views.log_in, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("<str:skill_name>/", views.service_owner, name="service_owner"),
]