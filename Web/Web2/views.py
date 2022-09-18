from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')


def registro(request):
    form = RegistroForm
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['nombre']
            messages.success(request,f'Usuario {nombre} creado')
            return redirect('index.html')
        else:
            form = RegistroForm()
    contexto = {'form':form}   
    return render(request,'registro.html',contexto)