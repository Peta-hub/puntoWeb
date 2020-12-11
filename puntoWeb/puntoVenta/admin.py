from django.contrib import admin
from puntoVenta.models import Recuperar,Clientes, Ventas, Detalles, Proveedores, Compras

# Register your models here.

admin.site.register(Recuperar)
admin.site.register(Clientes)
admin.site.register(Ventas)
admin.site.register(Detalles)
admin.site.register(Proveedores)
admin.site.register(Compras)