from django.shortcuts import render,redirect, HttpResponse
from django.urls import reverse_lazy
from django.views import View
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.hashers import make_password
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from Web2.models import universitario
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    user = grupo.objects.filter(user_id=request.user.id)
    datos = universitario.objects.all()
    return render(request,'index.html',{'mg':user,'uni':datos})

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
    coment = comentarios.objects.all()
    datos = propuesta.objects.all()
    print(datos)
    user = request.user
    contexto = {
        'user': user,
        'pro':datos,
        'coment':coment
    }
    form = comentarioform(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.datos = datos
            form2.save()
        else:
            form = comentarioform()
    return render(request,'feed.html',contexto)

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
    datos = universitario.objects.all()
    datos2 = lider.objects.all()
    user = request.user
    contexto = {
        'user': user,
        'uni':datos,
        'lider':datos2
    }
    return render(request,'coordinador.html',contexto)

@login_required
def form_propuestas(request):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':  
        form = propuestaForm(request.POST, request.FILES)     
        if form.is_valid():
            form2 = form.save(commit = False)
            form2.user = user
            form2.save()
            return redirect('index')
    else:
        form = propuestaForm()
    return render(request,'form_propuestas.html',{'form':form})


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
        
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form2 = grupoForm(request.POST, request.FILES)
        if form2.is_valid():
            form3 = form2.save(commit=False)
            form3.user = user
            form3.save()
            return redirect('index.html')
    else:
        form2 = grupoForm()
        
    uni = universitario.objects.filter(user_id = request.user.id)
    usuario = User.objects.filter()
    ziplista = zip(uni,usuario)
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form3 = liderform(request.POST)
        if form3.is_valid():
            form4 = form3.save(commit=False)
            form4.user = user
            form4.save()
            return redirect('index.html')
    else:
        form3 = liderform()
    return render(request,'perfil.html',{'form':form,'form2':form2,'zipl':ziplista,'un':uni,'form3':form3})

#uni = universitario.objects.all()
#user = request.user


def salir(request):
    logout(request)
    return redirect("index")
    
def ver_grupos(request):
    user = universitario.objects.all()
    grupos = grupo.objects.all()
    uni = request.user
    ziplista = zip(user,grupos)
    contexto = {
        'zip':ziplista,
        'uni':uni
    }
    return render(request,'grupo.html',contexto)

def migrupo(request, username):
    user = User.objects.get(username=username)
    my = user.migrupo.all()
    propuesta = user.user.all()
    contexto = {
        'user':user,
        'pro':propuesta,
        'my':my
    }
    return render(request,'migrupo.html',contexto)

def editar_perfil(request,id):
    
    perfil= universitario.objects.get(id=id)
    if request.method == 'GET':
        form = UniversitarioForm(instance=perfil)
        contesto = {'form':form,'perfil':perfil}
    else:
        form = UniversitarioForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'editarperfil.html', contesto)

def eliminar_usuario(request,id):
    usuario = User.objects.get(id = id)
    User.delete()
    return redirect('index') 


def editaruni(request,id):
    
    perfil= universitario.objects.get(id=id)
    if request.method == 'GET':
        form = UniversitarioForm2(instance=perfil)
        contesto = {'form':form,'perfil':perfil}
    else:
        form = UniversitarioForm2(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'editaruni.html', contesto)


def seguir(request,pk):
    post = grupo.objects.get(pk=pk)
    seguir = False
    for seguir in post.seguir.filter(id=request.user.id):
        if seguir == request.user:
            seguir = True
            break
    if not seguir:
        post.seguir.add(request.user)
    if seguir:
        post.seguir.remove(request.user)
        
    next = request.POST.get('next','/')
    return HttpResponseRedirect(next)

def like(request,pk):
    post = propuesta.objects.get(pk=pk)
    like = False
    for like in post.like.filter(id=request.user.id):
        if like == request.user:
            like = True
            break
    if not like:
        post.like.add(request.user)
    if like:
        post.like.remove(request.user)
        
    next = request.POST.get('next','/')
    return HttpResponseRedirect(next)


def comentarioview(request):
    user = get_object_or_404(User,pk=request.user.pk)
    if request.method == 'POST':
        form = comentarioform(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.user = user
            comentario.save()
            return redirect('index.html')
    else:
        form = comentarioform()
        
    return render(request,'comentario.html',{'form':form})


def form_contacto(request):
    if request.method == 'POST':
        form = contacto_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = contacto_form()
    return render(request,'form_contacto.html',{'form':form})

def calificar(request):
    return render(request,'calificar.html')