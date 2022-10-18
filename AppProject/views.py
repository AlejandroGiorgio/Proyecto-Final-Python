from operator import index
from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from pathlib import Path
from AppProject.models import *
from AppProject.forms import form_user, UserRegisterForm, UserEditForm, ChangePasswordForm, AddAvatar
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required
def create_user(request):
    if request.method == 'POST':
        user = Passenger(name= request.POST["name"], lastName= request.POST["lastName"], email= request.POST["email"])
        user.save()
        users = Passenger.objects.all()
        return render(request, "CRUD/read_user.html", {"user": users})
        #return redirect("/")

    return render(request, "CRUD/create_user.html")
    
@login_required
def read_user(request):
    users = Passenger.objects.all() #trae todo
    return render (request, "CRUD/read_user.html", {"user":users})

@login_required
def update_user(request, user_id):
    user = Passenger.objects.get(id=user_id)

    if request.method == 'POST':
        formulario=form_user(request.POST)
        
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            user.username=informacion['name']
            user.lastName=informacion['lastName']
            user.email=informacion['email']
            user.save()
            read_user(request)
            users=Passenger.objects.all()
            return render(request, "CRUD/read_user.html", {"user": users})
            
    else:
            formulario=form_user(initial={'name':user.username, 'lastName':user.lastName, 'email':user.email})
    return render(request,"CRUD/update_user.html", {"formulario": formulario})

@login_required
def delete_user(request, user_id):
    user = Passenger.objects.get(id = user_id)
    user.delete()
    users = Passenger.objects.all()    
    return render(request, "CRUD/read_user.html", {"user": users})

@login_required
def create_driver(request):
    if request.method == 'POST':
        driver = Driver(name= request.POST["name"], lastName= request.POST["lastName"], email= request.POST["email"], registry= request.POST["registry"])
        driver.save()
        return redirect("/")
    return render(request, "CRUD/create_driver.html")

@login_required
def create_movile(request):
    if request.method == 'POST':
        movile = Movile(carPatent= request.POST["carPatent"], carBrand= request.POST["carBrand"], year=request.POST["carYear"])
        movile.save()
        return redirect("/")
    return render(request, "CRUD/create_movile.html")

@login_required
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

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')

            user = authenticate(username = user, password = pwd)

            if user is not None:
                login(request, user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None
                return render(request, 'index.html', {'avatar': avatar})
            else:
                return render(request, "login.html", {'form':form})
        else:
            return render(request, "login.html", {'form':form})
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return redirect("/AppProject/login")
        else:
            return render(request, "register.html", {'form': form})
   

    form = UserRegisterForm()
    return render(request, "register.html", {'form': form})

@login_required
def editUser(request):
    user = request.user
    user_basic_info = User.objects.get(id = user.id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance = user)
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get ('username')
            user_basic_info.email = form.cleaned_data.get ('email')
            user_basic_info.first_name = form.cleaned_data.get ('first_name')
            user_basic_info.last_name = form.cleaned_data.get ('last_name')
            user_basic_info.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'index.html', {'avatar': avatar})
        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'index.html', {'form':form, 'avatar': avatar})
        
    else:
        form = UserEditForm(initial = {'email': user.email, 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name })
    return render(request, 'editUser.html', {'form': form, 'user':user})

@login_required
def profileView(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return render(request, 'profile.html', {'avatar': avatar})

@login_required
def changepass(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'profile.html', {'avatar': avatar})
    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, 'changepass.html', {'form': form, 'user': user})

@login_required
def SubmitAvatar (request):
    if request.method == 'POST':
        form =AddAvatar(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user=User.objects.get(username=request.user)
            avatar=Avatar(user=user, image=form.cleaned_data['avatar'], id=request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user=request.user.id)
            try:
                avatar=avatar[0].image.url
            except:
                avatar= None
            return render(request, 'profile.html', {'avatar':avatar})
        else:
            try:
                avatar=Avatar.objects.filter(user = request.user.id)
                form = AddAvatar()
            except:
                form = AddAvatar()
        return render(request, 'addAvatar.html', {'form': form})