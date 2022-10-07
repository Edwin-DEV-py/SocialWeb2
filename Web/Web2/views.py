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

def index(request):
    return render(request,'index.html')

def login(request):
    form = formLogin(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Iniciaste sesion')
            return redirect('index.html')
        else:
            messages.warning(request,'datos no validos')
            return redirect('registro.html')
    return render(request,'login.html',{'form':form})

def feed(request):
    return render(request,'feed.html')

def registro(request):
    if request.method == 'POST':
        form = formRegistro(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            username = form.cleaned_data['username']
            messages.success(request,f'Usuario {username} creado')
            return redirect('index.html')
    else:
        form = formRegistro()
    contexto = {'form':form}
    return render(request,'registro.html',contexto)

def coordinador(request):
    return render(request,'coordinador.html')

def form_propuestas(request):
    return render(request,'form_propuestas.html')

def grupo(request):
    return render(request,'grupo.html')

def perfil(request):
    return render(request,'perfil.html')