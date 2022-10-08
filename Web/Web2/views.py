from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import *
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=username,password = password)
            if usuario is not None:
                login(request,usuario)
                messages.success(request,f'bienvenido {username}')
                return redirect('index.html')
            else:
                messages.error(request,"Los datos son incorrectos")
    form = AuthenticationForm()
    return render(request,'login.html',{"form":form})

def feed(request):
    return render(request,'feed.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = registro(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('index.html')
    else:
        form = registro()
    contexto = {'form':form}
    return render(request,'registro.html',contexto)

def coordinador(request):
    return render(request,'coordinador.html')

def form_propuestas(request):
    return render(request,'form_propuestas.html')

def grupo(request):
    return render(request,'grupo.html')

@login_required
def perfil(request):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = UniversitarioForm(request.POST, request.FILES)
        if form.is_valid():
            form2 = form.save(commit = False)
            form2.user = user
            form2.save()
            return redirect('index.html')
    else:
        form = UniversitarioForm()
    tipo = universitario.objects.filter(user_id = request.user.id)   
    return render(request,'perfil.html',{'form':form,'tp':tipo})



def salir(request):
    logout(request)
    return redirect("index")
    

