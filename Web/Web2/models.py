from distutils.command.upload import upload
from email.policy import default
from django.db import models
import random,string
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class Manager(BaseUserManager):
    def create_user(self,email,username,password = None):
        if not email:
            raise ValueError('El usuario debe introducir un correo')
        
        usuario = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self,username,email,password):
        usuario = self.create_user(
            email,
            username = username
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

#edwin@gmail.com  == emi123

lista1=[
    ('universitario','Uni'),
    ('Normal','Nor')
]

lista2=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
]
        
class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre',max_length=254,unique=True)
    email = models.EmailField('Correo',max_length=254,unique=True,primary_key=True,null=False)
    nombre2 = models.CharField(max_length=30,null=True,blank=True)
    apellido1 = models.CharField(max_length=30)
    apellido2 = models.CharField(max_length=30)
    fecha = models.DateTimeField(verbose_name="Fecha",null=True,blank=True)
    tipo_usuario=models.CharField(max_length=13,choices=lista1)
    universidad = models.CharField(max_length=80,null=True,blank=True)
    facultad = models.CharField(max_length=50,null=True,blank=True)
    promedio = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    semestre = models.CharField(max_length=2,choices=lista2,null=True,blank=True)
    identificacion = models.CharField(max_length=10,null=True,blank=True)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)
    objects = Manager()
    
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return f'Perfil de {self.nombre1},{self.apellido1}'
    
    def has_perm(self,perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador
    