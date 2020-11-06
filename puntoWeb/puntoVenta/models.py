from django.db import models

# Create your models here.
class Usuarios(models.Model):
    usuario=models.CharField(max_length=15)
    contraseña=models.CharField(max_length=20)
    nombre=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=30)
    preguntaSecreta=models.CharField(max_length=35)
    respuesta=models.CharField(max_length=30)
    fechaCreacion=models.DateTimeField(auto_now_add=True)