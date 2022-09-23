from operator import index
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pathlib import Path
from AppProject.models import *
from AppProject.forms import *
path=Path(__file__).parent.resolve()
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        user = User(name= request.POST["nombre"], lastName= request.POST["apellido"], email= request.POST["email"])
        user.save()
        users = User.objects.all() #trae todo
        return render (request, "CRUD/read_user.html", {"user":users})

    return render(request, "CRUD/create_user.html")

def read_user(request):
    users = User.objects.all() #trae todo
    return render (request, "CRUD/read_user.html", {"user":users})

def update_user(request, user_email):
    user = User.objects.get(email=user_email)

    if request.method == 'POST':
        formulario=form_user(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            user.nombre=informacion['nombre']
            user.apellido=informacion['apellido']
            user.email=informacion['email']
            user.save()
            user=User.objects.all()
            read_user()
        else:
            formulario=form_user(initial={'nombre':user.name, 'apellido':user.lastName, 'email':user.email})

def delete_user(request, user_email):
    user = User.objects.get(email = user_email)
    user.delete()

    users = User.objects.all()    
    return render(request, "CRUD/read_user.html", {"users": users})

def create_driver(request):
    if request.method == 'POST':
        user = Driver(name= request.POST["nombre"], lastName= request.POST["apellido"], email= request.POST["email"], id=request.POST["ID"])
        user.save()
    return render(request, "CRUD/create_driver.html")

def create_movile(request):
    if request.method == 'POST':
        user = Movile(carPatent= request.POST["patente"], carBrand= request.POST["marca"], year=request.POST["año"])
        user.save()
    return render(request, "CRUD/create_movile.html")

def home(request):
    doc=loader.get_template("index.html")
    doc2=doc.render()
    return HttpResponse (doc2)