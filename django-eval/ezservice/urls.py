from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "ezservice"

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("login/", views.log_in, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("my_skills/", views.my_skills, name="my_skills"),
    path("add-skill/", views.add_skill, name="add_skill"),
    path("book/<int:service_id>/", views.book_service, name="book_service"),
    path("my_reservations/", views.my_reservations, name="my_reservations"),
    path("<str:skill_name>/", views.service_owner, name="service_owner"),
]