from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Recuperar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) # Si eliminan al usuario ligado tambien se eliminan sus campos en esta tabla
    pregunta_secreta = models.CharField("Pregunta Secreta", max_length=35, blank=False, null=False, default=0)
    respuesta = models.CharField("Respuesta de la pregunta secreta", max_length=30, blank=True, null=True, default=0)



class Clientes(models.Model):
    id = models.CharField("Identificador", primary_key=True, max_length=4, blank=False, null=False, default="")
    nombre = models.CharField("Nombre cliente", max_length=16, blank=True, null=False, default="")
    apellidos = models.CharField("Apellidos cliente", max_length=16, blank=True, null=False, default="")
    direccion = models.CharField("Direccion cliente", max_length=16, blank=True, null=False, default="")
    telefono = models.CharField("Telefono cliente", max_length=16, blank=True, null=False, default="")


class Productos(models.Model):
    codigo = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre producto", max_length=20, blank=True, null=False, default="")
    categoria = models.CharField("Categoria", max_length=20, blank=True, null=False, default="")
    precio = models.IntegerField("Precio sugerido", blank=True, null=False, default="")

    def __str__(self):  # devuelve el nombre del objeto al verlo en la bd para que podamos ver de que objeto se trata!
        return self.nombre


class Proveedores(models.Model):
    id_Proveedor = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre producto", max_length=25, blank=True, null=False, default="")
    direccion = models.CharField("Direccion proveedor", max_length=30, blank=True, null=False, default="")
    telefono = models.CharField("Telefono proveedor", max_length=16, blank=True, null=False, default="")

    def __str__(self):
        return self.nombre


class Materiales(models.Model):
    id_Material = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    nombre = models.CharField("Nombre producto", max_length=30, blank=True, null=False, default="")
    medidas = models.CharField("Telefono proveedor", max_length=16, blank=True, null=False, default="")
    precio = models.IntegerField("Precio sugerido", blank=True, null=False, default="")

    def __str__(self):  # devuelve el nombre del objeto al verlo en la bd para que podamos ver de que objeto se trata!
        return self.nombre


class Compras(models.Model):
    id = models.AutoField("Identificador", primary_key=True, blank=False, null=False)
    cantidad = models.IntegerField("Cantidad: ", blank=True, null=False, default="")
    precio = models.FloatField("Precio: ",blank=True, null=False, default=0)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    material = models.OneToOneField(Materiales, on_delete=models.CASCADE)
    proveedor = models.OneToOneField(Proveedores, on_delete=models.CASCADE)


class Ventas(models.Model):
    id = models.AutoField("Identificador", primary_key=True, blank=False, null=False)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad: ", blank=True, null=False, default="")
    paga = models.FloatField("Paga: ", blank=True, null=False, default=0)
    precio = models.FloatField("Precio: ", blank=True, null=False, default=0)
    cambio = models.FloatField("Cambio: ", blank=True, null=False, default=0)
    fecha_compra = models.DateTimeField(auto_now_add=True)


class Detalles(models.Model):
    codigo = models.CharField("Identificador", primary_key=True, max_length=4, blank=True, null=False, default="")
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    material = models.ForeignKey(Materiales, on_delete=models.CASCADE)
    cantidad = models.IntegerField("Cantidad: ", blank=True, null=False, default="")