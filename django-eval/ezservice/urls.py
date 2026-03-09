from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("ezservice.urls")),
    path("admin/", admin.site.urls),
]