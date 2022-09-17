from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'iniciar_sesion.html')

def registro(request):
    return render(request,'registrarse.html')

def cerrar(request):
    return render(request,'cerrar.html')
