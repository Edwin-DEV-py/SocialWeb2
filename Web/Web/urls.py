"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from django.contrib import admin
from django.urls import path
from Web2.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('perfil/', perfil,name="perfil"),
    path('', index,name="index"),
    path('index.html',index,name="inicio"),
    path('admin/', admin.site.urls),
    path('registro.html',registro_usuario,name="registro"),
    path('editarperfil/<int:id>/',editar_perfil,name="editar"),
    path('index/', index,name="index"),
    path('login.html', login_usuario,name="login"),
    path('feed/', feed,name="feed"),
    path('coordinador/', coordinador,name="coordinador"),
    path('form_propuestas/', form_propuestas,name="form_propuestas"),
    path('grupo/', ver_grupos,name="ver_grupos"),
    path('migrupo/<str:username>/', migrupo,name="migrupo"),
    path('cerrar.html',salir,name="cerrar"),
    path('eliminar_usuario',eliminar_usuario,name="eliminar_usuario"),
    path('editaruni/<int:id>/',editaruni,name="editarU"),
    path('grupo.html/<int:pk>/seguir',seguir,name="seguir"),
    path('form_contacto/', form_contacto,name="form_contacto"),
    path('comentario/', comentarioview,name="comentario"),
    #path('feed/\\(\\?P(?P<pk>[^/]+)\\[0\\-9\\]\\+\\)/comentario/\\Z',feed,name="comentario"),
    #path('follow/<str:username>/',follow,name="follow"),
    #path('unfollow/<str:username>/',unfollow,name="unfollow"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)