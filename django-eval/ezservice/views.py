from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Service, Reservation, Skill, UserSkill


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

def my_skills(request):
    my_skills_list = UserSkill.objects.filter(
        user=request.user
    )

    return render(request,
                  "ezservice/my_skills.html",
                  {"my_skills_list": my_skills_list}
                  )

#This function allow the user to set a list of skills he owns
#Not to create a skill
@login_required
def add_skill(request):
    if request.method == "POST":
        skill_id = request.POST.get("skill")
        skill = Skill.objects.get(id=skill_id)

        # check if skill already exist in the list : only add if it's not there yet
        UserSkill.objects.get_or_create(
            user=request.user,
            skill=skill
        )

        return redirect("ezservice:my_skills")

    skills = Skill.objects.all()
    return render(request, "ezservice/add_skill.html", {"skills": skills})

def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("ezservice:index")
        else:
            return render(request, "ezservice/login.html", {
                "error": "Invalid username or password."
            })

    return render(request, "ezservice/login.html")

def logout_view(request):
    logout(request)
    return redirect("ezservice:index")
