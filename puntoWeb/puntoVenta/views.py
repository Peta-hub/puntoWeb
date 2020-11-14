from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from puntoVenta.forms import FormularioLogin
from puntoVenta.forms import ClienteForm
from django.contrib.auth import authenticate, login as do_login


# Create your views here.
from puntoVenta.models import Clientes


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



def userProductos(request):
    return render(request, "puntoVentaTemplates/userProductos.html")


def userCompras(request):
    return render(request, "puntoVentaTemplates/userCompras.html")


def userVentas(request):
    return render(request, "puntoVentaTemplates/userVentas.html")



def adminPrincipalProductos(request):
    return render(request, "puntoVentaTemplates/adminPrincipalProductos.html")


def userClientes(request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        print(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
        return redirect("clientes")
    else: # si es get
        cliente_form = ClienteForm()
        clientes = Clientes.objects.all()
    return render(request, "puntoVentaTemplates/userClientes.html", {"form": cliente_form, "clientes":clientes})


def eliminar_cliente(request,pk):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    cliente = Clientes.objects.get(id=pk)
    cliente.delete()
    return redirect("clientes")


def editarCliente(request,pk=""):  # se editara un autor desde una url, esta funcion recibe el id de un autor para editarlo
    cliente_form = None
    error = None
    try:
        cliente = Clientes.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            cliente_form = ClienteForm(instance=cliente)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            cliente_form = ClienteForm(request.POST,instance=cliente)
            if cliente_form.is_valid():
                cliente_form.save()
            return redirect("clientes")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_userClientes.html', {'form': cliente_form,'error': error, "iduser":pk})