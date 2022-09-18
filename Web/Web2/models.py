from django.db import models


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
class Usuario(models.Model):
    id_usuario= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True,max_length=100)
    fecha = models.DateTimeField(verbose_name="Fecha")
    password = models.CharField(max_length=100)
    tipo_usuario=models.CharField(max_length=13,choices=lista1)
    universidad = models.CharField(max_length=80,null=True)
    facultad = models.CharField(max_length=50,null=True)
    promedio = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    semestre = models.CharField(max_length=2,choices=lista2,null=True)
    identificacion = models.CharField(max_length=10)

