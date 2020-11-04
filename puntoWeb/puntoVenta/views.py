from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):

    return render(request, "puntoVentaTemplates/login.html")

def userClientes(request):

    return render(request, "puntoVentaTemplates/userClientes.html")


def userProductos(request):
    return render(request, "puntoVentaTemplates/userProductos.html")


def userCompras(request):
    return render(request, "puntoVentaTemplates/userCompras.html")


def userVentas(request):
    return render(request, "puntoVentaTemplates/userVentas.html")