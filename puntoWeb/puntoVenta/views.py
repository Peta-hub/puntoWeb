from django.contrib.auth import authenticate
from django.shortcuts import render, HttpResponse, redirect
from puntoVenta.forms import FormularioLogin
from django.contrib.auth import authenticate, login as do_login

# Create your views here.



def login(request):
    if request.method == 'POST':
        nomuser = request.POST.get("username")
        conuser = request.POST.get("password")
        user = authenticate(request, username=nomuser, password=conuser)
        if user is not None:
            if user.is_superuser:
                try:
                    do_login(request, user)
                    return redirect('admin')
                except Exception:
                    return render(request, 'puntoVentaTemplates/login.html',{"form": FormularioLogin, "errores": "Error al iniciar sesión"})
            else:
                return redirect('clientes')
        else:
            print("el usuario cayo aqui")
            return render(request, 'puntoVentaTemplates/login.html',{"form": FormularioLogin, "errores": "Usuario y/o contraseña inválidos."})
    elif request.method == "GET":
        return render(request, "puntoVentaTemplates/login.html", {"form": FormularioLogin})




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