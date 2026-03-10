from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Service, Reservation


def index(request):
    services_list = Service.objects.all()
    context = {"services_list": services_list}

    return render(request, "ezservice/index.html", context)

def services (request, service_id):
    return  HttpResponse("You're looking at list of services %s." %  service_id)

def detail(request, service_id):
    try:
        service = Service.objects.get(pk=service_id)
    except Service.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "ezservice/detail.html", {"service": service})