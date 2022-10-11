from operator import index
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pathlib import Path
from AppProject.models import *
from AppProject.forms import form_user
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.

def create_user(request):
    if request.method == 'POST':
        user = User(name= request.POST["name"], lastName= request.POST["lastName"], email= request.POST["email"])
        user.save()
        users = User.objects.all()
        return render(request, "CRUD/read_user.html", {"user": users})
        #return redirect("/")

    return render(request, "CRUD/create_user.html")
    

def read_user(request):
    users = User.objects.all() #trae todo
    return render (request, "CRUD/read_user.html", {"user":users})

def update_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        formulario=form_user(request.POST)
        
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            user.name=informacion['name']
            user.lastName=informacion['lastName']
            user.email=informacion['email']
            user.save()
            read_user(request)
            users=User.objects.all()
            return render(request, "CRUD/read_user.html", {"user": users})
            
    else:
            formulario=form_user(initial={'name':user.name, 'lastName':user.lastName, 'email':user.email})
    return render(request,"CRUD/update_user.html", {"formulario": formulario})

def delete_user(request, user_id):
    user = User.objects.get(id = user_id)
    user.delete()
    users = User.objects.all()    
    return render(request, "CRUD/read_user.html", {"user": users})

def create_driver(request):
    if request.method == 'POST':
        driver = Driver(name= request.POST["name"], lastName= request.POST["lastName"], email= request.POST["email"], registry= request.POST["registry"])
        driver.save()
        return redirect("/")
    return render(request, "CRUD/create_driver.html")

def create_movile(request):
    if request.method == 'POST':
        movile = Movile(carPatent= request.POST["carPatent"], carBrand= request.POST["carBrand"], year=request.POST["carYear"])
        movile.save()
        return redirect("/")
    return render(request, "CRUD/create_movile.html")

def home(request):
    doc=loader.get_template("index.html")
    doc2=doc.render()
    return HttpResponse (doc2)

def search_user(request):
    if request.GET["email"]:
        email = request.GET["email"]
        user = User.objects.filter(email__icontains = email) 
        return render(request, "index.html", {"users": user})
    else:
        respuesta = "No hay registro"
    return HttpResponse(respuesta)
