from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Service, Reservation, Skill


def index(request):
    skills_list = Skill.objects.all()
    context = {"skills_list": skills_list}

    return render(request, "ezservice/index.html", context)

def services (request, service_id):
    return  HttpResponse("You're looking at list of services %s." %  service_id)

def detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, "ezservice/detail.html", {"service": service})