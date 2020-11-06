from django.shortcuts import render, HttpResponse
from puntoVenta.models import Usuarios

# Create your views here.

def login(request):

    return render(request, "puntoVentaTemplates/login.html")

def IngresarComo(request):

    user = request.GET["usuario"]
    password = request.GET["contraseña"]

    Vecusers = Usuarios.objects.filter( usuario__icontains=user)  # icontains es select * from SepoApp_usuarios where usuario=user

    for usuarios in Vecusers:
        Usuario = usuarios.usuario
        pclave = usuarios.contraseña

        if Usuario == user and password == pclave:

            if password == 'lamont':
                return render(request, "puntoVentaTemplates/userClientes.html")
            if password == 'emmm66':
                return render(request, "puntoVentaTemplates/adminPrincipalProductos.html")

        else:
            return render(request, "puntoVentaTemplates/login.html")



def userClientes(request):

    return render(request, "puntoVentaTemplates/userClientes.html")


def userProductos(request):
    return render(request, "puntoVentaTemplates/userProductos.html")


def userCompras(request):
    return render(request, "puntoVentaTemplates/userCompras.html")


def userVentas(request):
    return render(request, "puntoVentaTemplates/userVentas.html")



def adminPrincipalProductos(request):
    return render(request, "puntoVentaTemplates/adminPrincipalProductos.html")