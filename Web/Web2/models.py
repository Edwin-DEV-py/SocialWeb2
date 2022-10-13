from distutils.command.upload import upload
from email.policy import default
from operator import index
from django.db import models
import random,string
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

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
        
class universitario(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='universitario')
    tipo_usuario=models.CharField(max_length=13,choices=lista1)
    universidad = models.CharField(max_length=80,null=True,blank=True)
    facultad = models.CharField(max_length=50,null=True,blank=True)
    promedio = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    semestre = models.CharField(max_length=2,choices=lista2,null=True,blank=True)
    identificacion = models.CharField(max_length=10,null=True,blank=True)
    lider = models.CharField(max_length=1,null = True, default="0")
    
    
class grupo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='migrupo')
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 50, null=False)
    Descripcion = models.CharField(max_length = 150)
    
    # def following(self):
    #    user_ids = Relacion.objects.filter(from_user = self.user)\
    #                        .values_list('to_user_id',flat=True)
    #    return User.objects.filter(id__in=user_ids)
    # 
    # def followers(self):
    #    user_ids = Relacion.objects.filter(to_user = self.user)\
    #                        .values_list('from_user_id',flat=True)
    #    return User.objects.filter(id__in=user_ids)
    #liked
    def __str__(self):
    	return f'Perfil de {self.user.username}'

    

class propuesta(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 50, null=False)
    Descripcion = models.CharField(max_length = 300)
    link = models.CharField(max_length = 200)
    diapostivas = models.FileField(upload_to="diapositivas/")
    
    def __str__(self):
	    return (self.Descripcion,self.titulo,self.link,self.diapostivas)
 
 
 
#class Relacion(models.Model):
#    from_user = models.ForeignKey(User,related_name='relacion',on_delete=models.CASCADE)
#    to_user = models.ForeignKey(User,related_name='relacion_a',on_delete=models.CASCADE)
#    
#    def __str__(self):
#        return f'{self.from_user} to {self.to_user}'
#    
#    class Meta:
#        indexes = [
#            models.Index(fields=['from_user','to_user'])
#        ]