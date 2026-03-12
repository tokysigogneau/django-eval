from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Service, Reservation, Skill, UserSkill

'''
this function takes request in parameter.
It display a list of all the skills the website allow to share, and a list of skills the user selected.
The context contains 2 elements because we have 2 list of elements we want to display, so we return them both.
'''
def index(request):
    skills_list = Skill.objects.all()
    my_skills_list = UserSkill.objects.filter(
        user=request.user
    )

    #the context contains 2 elements, so I put them in a list
    context = {"skills_list": skills_list, "my_skills_list": my_skills_list}

    return render(request,
                  "ezservice/index.html",
                  context)

@login_required
def create_service(request):
    if request.method == "POST":
        skill_id = request.POST.get("skill")
        date = request.POST.get("date")
        description = request.POST.get("description")

        skill = Skill.objects.get(id=skill_id)

        Service.objects.create(
            service_owner=request.user,
            service_skill=skill,
            date=date,
            description=description,
            is_available=True
        )

        return redirect("ezservice:index")

    # list of skills
    # the user can select skill from the list, he can't create a skill he wants
    skills = Skill.objects.all()
    return render(request,
                  "ezservice/create_service.html",
                  {"skills": skills})

def my_services (request):
    my_services = Service.objects.filter(service_owner=request.user)
    return render(request,
                  "ezservice/my_services.html",
                  {"my_services": my_services})

'''
This function takes a request and a service_id in parameter.
It allows the user to book a specific service.
It create a new data object " reservation " from user and the service details.
get_or_create() function is used to first check if it already exists or not, 
and create only if it doesn't exist
And at the end, it change the service is_available status to False.
'''
@login_required
def book_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    Reservation.objects.get_or_create(
        reservation_title=f"Réservation de {service.service_skill.skill_name}",
        service_owner=service,
        service_client=request.user
    )

    service.is_available= False
    service.save()

    return redirect("ezservice:my_reservations")

'''
This function take a request in parameter.
It give a list of reservations the user made with other users.
'''
@login_required
def my_reservations(request):
    reservations = Reservation.objects.filter(service_client=request.user)
    return render(request,
                  "ezservice/my_reservations.html",
                  {"reservations": reservations})


@login_required
def detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request,
                  "ezservice/detail.html",
                  {"service": service})

'''
This function takes a request and a skill_name in parameter.
It display a list of all the service request for the selected service. made with : filter() 
It will not display the service made by the connected user. made with exclude()
'''
@login_required
def service_owner(request, skill_name):
    service_owner_list = Service.objects.filter(
        service_skill__skill_name=skill_name,
        is_available=True).exclude(service_owner = request.user)

    return render(request,
                  "ezservice/service_owner.html",
                  {"service_owner_list": service_owner_list}
                  )

@login_required
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
    return render(request,
                  "ezservice/add_skill.html",
                  {"skills": skills})

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

@login_required
def logout_view(request):
    logout(request)
    return redirect("ezservice:index")
