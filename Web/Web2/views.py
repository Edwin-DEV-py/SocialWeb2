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
    return render(request,'login.html')

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