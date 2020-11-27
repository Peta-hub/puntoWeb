from django.contrib.auth.models import User
from django.db import models

class Recuperar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Si eliminan al usuario ligado tambien se eliminan sus campos en esta tabla
    pregunta_secreta = models.CharField("Pregunta Secreta", max_length=35, blank=False, null=False, default=0)
    respuesta = models.CharField("Respuesta de la pregunta secreta", max_length=30, blank=True, null=True, default=0)


class Clientes(models.Model):
    id = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre cliente", max_length=16, blank=True, null=False, default="")
    apellidos = models.CharField("Apellidos cliente", max_length=16, blank=True, null=False, default="")
    direccion = models.CharField("Direccion cliente", max_length=16, blank=True, null=False, default="")
    telefono = models.CharField("Telefono cliente", max_length=16, blank=True, null=False, default="")

class Productos(models.Model):
    codigo = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre producto", max_length=20, blank=True, null=False, default="")
    categoria = models.CharField("Categoria", max_length=20, blank=True, null=False, default="")
    precio = models.IntegerField("Precio sugerido", blank=True, null=False, default="")

class Proveedores(models.Model):
    id_Proveedor = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre producto", max_length=25, blank=True, null=False, default="")
    direccion = models.CharField("Direccion proveedor", max_length=30, blank=True, null=False, default="")
    telefono = models.CharField("Telefono proveedor", max_length=16, blank=True, null=False, default="")

class Materiales(models.Model):
    id_Material = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre producto", max_length=30, blank=True, null=False, default="")
    medidas = models.CharField("Telefono proveedor", max_length=16, blank=True, null=False, default="")
    precio = models.IntegerField("Precio sugerido", blank=True, null=False, default="")
