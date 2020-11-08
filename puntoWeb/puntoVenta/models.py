from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Usuarios(models.Model):
#     usuario=models.CharField(max_length=15)
#     contraseña=models.CharField(max_length=20)
#     nombre=models.CharField(max_length=20)
#     apellidos=models.CharField(max_length=30)
#     preguntaSecreta=models.CharField(max_length=35)
#     respuesta=models.CharField(max_length=30)
#     fechaCreacion=models.DateTimeField(auto_now_add=True)

class Recuperar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Si eliminan al usuario ligado tambien se eliminan sus campos en esta tabla
    pregunta_secreta = models.CharField("Pregunta Secreta", max_length=35, blank=False, null=False, default=0)
    respuesta = models.CharField("Respuesta de la pregunta secreta", max_length=30, blank=True, null=True, default=0)