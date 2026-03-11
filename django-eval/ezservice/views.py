from django.contrib.auth.decorators import login_required
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

@login_required
def detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, "ezservice/detail.html", {"service": service})

@login_required
def service_owner(request, skill_name):
    service_owner_list = Service.objects.filter(
        service_skill__skill_name=skill_name,
        is_available=True)
    return render(request,
                  "ezservice/service_owner.html",
                  {"service_owner_list": service_owner_list}
                  )
