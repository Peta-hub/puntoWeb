from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from puntoVenta.forms import FormularioLogin
from puntoVenta.forms import ClienteForm, ProductoForm, ProveedorForm, RecuperarForm
from django.contrib.auth import authenticate, login as do_login


# Create your views here.
from puntoVenta.models import Clientes, Productos, Proveedores, Recuperar


def login(request):
    if request.method == 'POST':
        nomuser = request.POST.get("username")
        conuser = request.POST.get("password")
        user = authenticate(request, username=nomuser, password=conuser)
        if user is not None:
            if user.is_superuser:
                try:
                    do_login(request, user)
                    return redirect('adminMain')
                except Exception:
                    return render(request, 'puntoVentaTemplates/login.html',{"form": FormularioLogin, "errores": "Error al iniciar sesión"})
            else:
                return redirect('clientes')
        else:
            print("el usuario cayo aqui")
            return render(request, 'puntoVentaTemplates/login.html',{"form": FormularioLogin, "errores": "Usuario y/o contraseña inválidos."})
    elif request.method == "GET":
        return render(request, "puntoVentaTemplates/login.html", {"form": FormularioLogin})


def recuperarContraseña(request):

    return render(request, "puntoVentaTemplates/recuperarContraseña.html", {"form": FormularioLogin})

def recuperarContraseña2(request):

    return render(request, "puntoVentaTemplates/recuperarContraseña2.html", {"form": RecuperarForm})


def adminPrincipalProductos(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST)
        print(request.POST)
        if producto_form.is_valid():
            producto_form.save()
        return redirect("adminMain")
    else:  # si es get, es decir cuando solo se entra a la pagina
        producto_form = ProductoForm()
        productos = Productos.objects.all()
    return render(request, "puntoVentaTemplates/adminPrincipalProductos.html", {"form": producto_form, "productos": productos})

def eliminar_producto(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    producto = Productos.objects.get(codigo=pk)
    producto.delete()
    return redirect("adminMain")

def editarProducto(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    producto_form = None
    error = None
    try:
        producto = Productos.objects.get(codigo=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            producto_form = ProductoForm(instance=producto)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            producto_form = ProductoForm(request.POST,instance=producto)
            if producto_form.is_valid():
                producto_form.save()
            return redirect("adminMain")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_adminPrincipal.html', {'form': producto_form,'error': error, "codigo":pk})







def adminDetallesProducto(request):
    return render(request, "puntoVentaTemplates/adminDetallesProducto.html")

def adminMateriales(request):
    return render(request, "puntoVentaTemplates/adminMateriales.html")

def adminUsuarios(request):
    return render(request, "puntoVentaTemplates/adminUsuarios.html")


def adminReportes(request):
    return render(request, "puntoVentaTemplates/adminReportes.html")



#---------------------------- USUARIOS --------------------------------------#

def userClientes(request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        print(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
        return redirect("clientes")
    else: # si es get, es decir cuando solo se entra a la pagina
        cliente_form = ClienteForm()
        clientes = Clientes.objects.all()
    return render(request, "puntoVentaTemplates/userClientes.html", {"form": cliente_form, "clientes":clientes})


def eliminar_cliente(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    cliente = Clientes.objects.get(id=pk)
    cliente.delete()
    return redirect("clientes")


def editarCliente(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
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




def userProductos(request):
    return render(request, "puntoVentaTemplates/userProductos.html")


def userCompras(request):
    return render(request, "puntoVentaTemplates/userCompras.html")


def userVentas(request):
    return render(request, "puntoVentaTemplates/userVentas.html")


def userProveedores(request):
    if request.method == "POST":
        proveedor_form = ProveedorForm(request.POST)
        print(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
        return redirect("proveedores")
    else:  # si es get, es decir cuando solo se entra a la pagina
        proveedor_form = ProveedorForm()
        proveedores = Proveedores.objects.all()
    return render(request, "puntoVentaTemplates/userProveedores.html", {"form": proveedor_form, "proveedores": proveedores})

def eliminar_proveedor(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    proveedor = Proveedores.objects.get(id_Proveedor=pk)
    proveedor.delete()
    return redirect("proveedores")

def editarProveedor(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    proveedor_form = None
    error = None
    try:
        proveedor = Proveedores.objects.get(id_Proveedor=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            proveedor_form = ProveedorForm(instance=proveedor)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            proveedor_form = ProveedorForm(request.POST,instance=proveedor)
            if proveedor_form.is_valid():
                proveedor_form.save()
            return redirect("proveedores")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_userProveedores.html', {'form': proveedor_form,'error': error, "id_Proveedor":pk})