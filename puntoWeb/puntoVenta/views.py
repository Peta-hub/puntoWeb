from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponse, redirect
from django.utils.functional import empty
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from puntoVenta.forms import FormularioLogin, MaterialForm, VentaForm, DetalleForm
from puntoVenta.forms import ClienteForm, ProductoForm, ProveedorForm, RecuperarForm
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.db.models import Sum
# Create your views here.
from puntoVenta.models import Clientes, Productos, Proveedores, Recuperar, Materiales, Ventas, Detalles
from . import decorators
from puntoVenta.forms import UserForm

from puntoVenta.forms import CompraForm
from puntoVenta.models import Compras


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
                do_login(request, user)
                return redirect('clientes')
        else:
            print("el usuario cayo aqui")
            return render(request, 'puntoVentaTemplates/login.html',{"form": FormularioLogin, "errores": "Usuario y/o contraseña inválidos."})
    elif request.method == "GET":
        return render(request, "puntoVentaTemplates/login.html", {"form": FormularioLogin})


def logout(request):
    do_logout(request)
    return redirect('login')

def recuperarContraseña(request):
    if request.method == 'POST':
        nomuser = request.POST.get("username")
        if User.objects.filter(username=nomuser).exists():
            usuario = User.objects.get(username=nomuser)
            pregunta = Recuperar.objects.get(user=usuario)
            return render(request, "puntoVentaTemplates/recuperarContraseña2.html",{"pregunta":pregunta,"usuario":usuario,"form":RecuperarForm})
        else:
            print("el usuario cayo aqui")
            return render(request, 'puntoVentaTemplates/recuperarContraseña.html',{"form": FormularioLogin, "errores": "Usuario inválido."})
    return render(request, "puntoVentaTemplates/recuperarContraseña.html", {"form": FormularioLogin})


def recuperarContraseña2(request, pk=0):
    if request.method == 'POST':
        usuario = User.objects.get(id=pk)
        respuesta = request.POST.get("respuesta")
        if Recuperar.objects.filter(respuesta=respuesta).exists():
           pregunta = Recuperar.objects.get(respuesta=respuesta)
           if pregunta.user.username == usuario.username:
               user_form = UserForm(instance=usuario)
               return render(request,"puntoVentaTemplates/cambiarContraseña.html",{"form":user_form,"usuario":usuario})
        else:
            print("el usuario cayo aqui")
            question = Recuperar.objects.get(user=usuario)
            return render(request, 'puntoVentaTemplates/recuperarContraseña2.html',{"form": RecuperarForm, "errores": "Respuesta invalida.","usuario":usuario, "pregunta":question})
    return render(request, "puntoVentaTemplates/recuperarContraseña2.html", {"form": RecuperarForm})


def cambiar_contrasena(request, pk=0):
    usuario = User.objects.get(id=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=usuario)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
        else:
            print(user_form.errors)
            print("error")


@decorators.no_admin
def adminPrincipalProductos(request):
    if request.method == "POST":
        producto_form = ProductoForm(request.POST, files=request.FILES)  #files es para poder subir imagenes
        print(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect("adminMain")
        else:
            producto_form = ProductoForm()
            productos = Productos.objects.all()
            return render(request, "puntoVentaTemplates/adminPrincipalProductos.html",{"form": producto_form, "productos": productos, "error": "*Porfavor introduzca un id diferente"})
    else:  # si es get, es decir cuando solo se entra a la pagina
        producto_form = ProductoForm()
        productos = Productos.objects.all()
    return render(request, "puntoVentaTemplates/adminPrincipalProductos.html", {"form": producto_form, "productos": productos})

@decorators.no_es_admin
def eliminar_producto(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    producto_form = None
    error = None
    try:
        producto = Productos.objects.get(codigo=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            producto_form = ProductoForm(instance=producto)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            producto = Productos.objects.get(codigo=pk)
            producto.delete()
            return redirect("adminMain")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_adminProductos.html', {'form': producto_form, 'error': error, "iduser": pk, 'producto': producto})

@decorators.no_es_admin
def editarProducto(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    producto_form = None
    error = None
    try:
        producto = Productos.objects.get(codigo=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            producto_form = ProductoForm(instance=producto)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            producto_form = ProductoForm(request.POST,instance=producto, files=request.FILES)
            if producto_form.is_valid():
                producto_form.save()
            return redirect("adminMain")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_adminPrincipal.html', {'form': producto_form,'error': error, "codigo":pk})




@decorators.no_admin
def adminDetallesProducto(request):
    if request.method == "POST":
        detalles_form = DetalleForm(request.POST)
        if detalles_form.is_valid():
            detalles_form.save()
            return redirect("adminDetaProducto")
        else:
            detalles_form = DetalleForm()
            detalles = Detalles.objects.all()
            return render(request, "puntoVentaTemplates/adminDetallesProducto.html",{"form": detalles_form, "detalles": detalles, "error": "*Porfavor introduzca un id diferente"})
    else:  # si es get, es decir cuando solo se entra a la pagina
        detalles_form = DetalleForm()
        detalles = Detalles.objects.all()
    return render(request, "puntoVentaTemplates/adminDetallesProducto.html", {"form": detalles_form, "detalles": detalles})

@decorators.no_es_admin
def eliminar_detalle(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    detalles_form = None
    error = None
    try:
        detalle = Detalles.objects.get(codigo=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            detalles_form = DetalleForm(instance=detalle)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            detalle = Detalles.objects.get(codigo=pk)
            detalle.delete()
            return redirect("adminDetaProducto")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_adminDetalles.html', {'form': detalles_form, 'error': error, "iduser": pk, 'detalle': detalle})

@decorators.no_es_admin
def editarDetalle(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    detalles_form = None
    error = None
    print("hola soy la pk",pk)
    print(type(pk))
    try:
        detalle = Detalles.objects.get(codigo=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            detalles_form = DetalleForm(instance=detalle)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            detalles_form = DetalleForm(request.POST,instance=detalle)
            if detalles_form.is_valid():
                detalles_form.save()
            return redirect("adminDetaProducto")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_adminDetalles.html', {'form': detalles_form,'error': error, "codigo":pk})




@decorators.no_admin
def adminMateriales(request):
    if request.method == "POST":
        material_form = MaterialForm(request.POST)
        print(request.POST)
        if material_form.is_valid():
            material_form.save()
            return redirect("adminMateriales")
        else:
            material_form = MaterialForm()
            materiales = Materiales.objects.all()
            return render(request, "puntoVentaTemplates/adminMateriales.html",{"form": material_form, "materiales": materiales, "error": "*Porfavor introduzca un id diferente"})
    else:  # si es get, es decir cuando solo se entra a la pagina
        material_form = MaterialForm()
        materiales = Materiales.objects.all()
    return render(request, "puntoVentaTemplates/adminMateriales.html",{"form": material_form, "materiales": materiales})


@decorators.no_es_admin
def eliminar_material(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    material_form = None
    error = None
    try:
        material = Materiales.objects.get(id_Material=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            material_form = MaterialForm(instance=material)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            material = Materiales.objects.get(id_Material=pk)
            material.delete()
            return redirect("adminMateriales")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_adminMateriales.html', {'form': material_form, 'error': error, "iduser": pk, 'material': material})

@decorators.no_es_admin
def editarMaterial(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    material_form = None
    error = None
    try:
        material = Materiales.objects.get(id_Material=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            material_form = MaterialForm(instance=material)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            material_form = MaterialForm(request.POST,instance=material)
            if material_form.is_valid():
                material_form.save()
            return redirect("adminMateriales")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_adminMateriales.html', {'form': material_form,'error': error, "id_Material":pk})




@decorators.no_admin
def adminUsuarios(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        recuperar_form = RecuperarForm(request.POST)
        if form.is_valid() and recuperar_form.is_valid():
            user = form.save()
            recuperar = recuperar_form.save(commit=False) #hacer modificacion antes de salvar
            recuperar.user = user
            recuperar.save()
            return redirect("adminUsuarios")
        else:
            print(recuperar_form.errors)
    else:
        form = UserForm()
        recuperar_form = RecuperarForm()
        preguntas = Recuperar.objects.all()
        contexto = {"form":form,"recuperar_form":recuperar_form,"usuarios":preguntas}
        return render(request,"puntoVentaTemplates/adminUsuarios.html",contexto)

@decorators.no_es_admin
def eliminar_usuario(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    user_form = None
    error = None
    try:
        usuario = User.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            user_form = UserForm(instance=usuario)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            usuario = User.objects.get(id=pk)
            usuario.delete()
            return redirect("adminUsuarios")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_adminUsuarios.html', {'form': user_form, 'error': error, "iduser": pk, 'usuario': usuario})

@decorators.no_es_admin
def editarUsuario(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    usuario = User.objects.get(id=pk)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=usuario)
        recuperar_form = RecuperarForm(request.POST, instance=usuario.recuperar)
        if user_form.is_valid() and recuperar_form.is_valid():
            user_form.save()
            recuperar_form.save()
            return redirect('adminUsuarios')
        else:
            print("error")
    else:
        print(request.user)
        user_form = UserForm(instance=usuario)
        recuperar_form = RecuperarForm(instance=usuario.recuperar)
        return render(request, "puntoVentaTemplates/actualizar_adminUser.html", {'form': user_form,'form2': recuperar_form, 'iduser':pk })



@decorators.no_admin
def adminReportes(request):
    return render(request, "puntoVentaTemplates/adminReportes.html")

@decorators.no_admin
def adminReportesCompras(request):
    compras_form = CompraForm()
    compras = Compras.objects.all()
    suma = Compras.objects.all().aggregate(Sum('precio'))
    return render(request, "puntoVentaTemplates/adminReportesCompras.html", {"form": compras_form, "compras": compras,"total": suma})

@decorators.no_admin
def adminReportesVentas(request):
    ventas_form = VentaForm()
    ventas = Ventas.objects.all()
    suma = Ventas.objects.all().aggregate(Sum('precio'))
    return render(request, "puntoVentaTemplates/adminReportesVentas.html", {"form": ventas_form, "ventas": ventas,"total": suma})


#---------------------------- USUARIOS --------------------------------------#

def userClientes(request):
    if request.method == "POST":
        cliente_form = ClienteForm(request.POST)
        print(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect("clientes")
        else:
            cliente_form = ClienteForm()
            clientes = Clientes.objects.all()
            return render(request, "puntoVentaTemplates/userClientes.html", {"form": cliente_form, "clientes": clientes, "error": "*Porfavor introduzca un id diferente"})
    else: # si es get, es decir cuando solo se entra a la pagina
        cliente_form = ClienteForm()
        clientes = Clientes.objects.all()
    return render(request, "puntoVentaTemplates/userClientes.html", {"form": cliente_form, "clientes":clientes})


def eliminar_cliente(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    cliente_form = None
    error = None
    try:
        cliente = Clientes.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            cliente_form = ClienteForm(instance=cliente)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:                                      #cuando se llega con POST
            cliente = Clientes.objects.get(id=pk)
            cliente.delete()
            return redirect("clientes")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_userClientes.html', {'form': cliente_form, 'error': error, "iduser": pk,'cliente':cliente })


def editarCliente(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    cliente_form = None
    error = None
    try:
        cliente = Clientes.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            cliente_form = ClienteForm(instance=cliente)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:
            cliente_form = ClienteForm(request.POST,instance=cliente)
            if cliente_form.is_valid():
                cliente_form.save()
            return redirect("clientes")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_userClientes.html', {'form': cliente_form,'error': error, "iduser":pk})




def userProductos(request):
    if request.method == "POST":

        if request.POST["nombre"]:

            nombre = request.POST["nombre"]

            productos = Productos.objects.filter(nombre__icontains=nombre)

            producto_form = ProductoForm()

            return render(request, "puntoVentaTemplates/userProductos.html", {"form": producto_form,"productos": productos, "query": nombre})

    else:
     producto_form = ProductoForm()
     return render(request, "puntoVentaTemplates/userProductos.html", {"form": producto_form})


def userCompras(request):
    if request.method == "POST":
        compras_form = CompraForm(request.POST)
        if compras_form.is_valid():
            compras_form.save()
        return redirect("compras")
    else:  # si es get, es decir cuando solo se entra a la pagina
        compras_form = CompraForm()
        compras = Compras.objects.all()
    return render(request, "puntoVentaTemplates/userCompras.html", {"form": compras_form, "compras": compras})


def eliminar_compra(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    compra_form = None
    error = None
    try:
        compra = Compras.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            compra_form = CompraForm(instance=compra)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            compra = Compras.objects.get(id=pk)
            compra.delete()
            return redirect("compras")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_userCompras.html', {'form': compra_form, 'error': error, "iduser": pk, 'compra': compra})


def editarCompra(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    compras_form = None
    error = None
    print("hola soy la pk",pk)
    print(type(pk))
    try:
        compra = Compras.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            compras_form = CompraForm(instance=compra)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            compras_form = CompraForm(request.POST,instance=compra)
            if compras_form.is_valid():
                compras_form.save()
            return redirect("compras")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_userCompras.html', {'form': compras_form,'error': error, "id_Compra":pk})


#El campo se manda a llamar con el nombre que tiene en la base de datos

def userVentas(request):
    if request.method == "POST":
        ventas_form = VentaForm(request.POST)
        print(request.POST)
        if request.POST.get("paga"):
            print("no aqui")
            if ventas_form.is_valid():
                paga = request.POST.get("paga")
                print(paga)
                venta = ventas_form.save(commit=False)
                precio_total = request.session.get('precio_total', False)
                cantidad = request.session.get('cantidad', False)
                nombre = request.session.get('nombre', False)
                cambio = int(paga) - int(precio_total)
                if cambio < 0:
                    ventas = Ventas.objects.all()
                    flag = True
                    return render(request, "puntoVentaTemplates/userVentas.html",{"form": ventas_form, "total": precio_total, "flag": flag, "ventas": ventas,"cantidad": cantidad, "nombre": nombre, "error": "*Por favor introduzca un numero mayor"})
                venta.precio = precio_total #Aqui se guarda algo individualmente en la bd
                venta.cambio = cambio
                print(venta)
                print(precio_total)
                venta.save()
            return redirect("ventas")
        else:
            cantidad = 0
            print("aqui")
            id_producto = request.POST.get("producto")
            print(id_producto)
            cantidad = request.POST.get("cantidad")

            product = Productos.objects.get(codigo=id_producto)
            nombre = product.nombre
            precio_producto = product.precio
            print(type(precio_producto))
            print(type(cantidad))
            precio_total = int(cantidad) * precio_producto
            print(precio_total)
            request.session['id_producto'] = id_producto
            request.session['nombre'] = nombre
            request.session['precio_total'] = precio_total
            request.session['cantidad'] = cantidad
            flag = True
            ventas = Ventas.objects.all()
            return render(request, "puntoVentaTemplates/userVentas.html", {"form": ventas_form, "total": precio_total, "flag": flag, "ventas": ventas, "cantidad": cantidad, "nombre": nombre})
    else:  # si es get, es decir cuando solo se entra a la pagina
        ventas_form = VentaForm()
        ventas = Ventas.objects.all()
        flag = False
    return render(request, "puntoVentaTemplates/userVentas.html", {"form": ventas_form, "ventas": ventas, "flag": flag})


def eliminar_venta(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    venta_form = None
    error = None
    try:
        venta = Ventas.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            venta_form = VentaForm(instance=venta)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            venta = Ventas.objects.get(id=pk)
            venta.delete()
            return redirect("ventas")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_userVentas.html',{'form': venta_form, 'error': error, "iduser": pk, 'venta': venta})


def editarVenta(request,pk=""):  # se editara un cliente desde una url, esta funcion recibe el id de un cliente para editarlo
    ventas_form = None
    error = None
    print("hola soy la pk",pk)
    print(type(pk))
    try:
        venta = Ventas.objects.get(id=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            ventas_form = VentaForm(instance=venta)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Autor que busco el usuario por eso se pone la variable de arriba
        else:
            ventas_form = VentaForm(request.POST,instance=venta)
            if ventas_form.is_valid():
                ventas_form.save()
            return redirect("ventas")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/actualizar_userVentas.html', {'form': ventas_form,'error': error, "id":pk})





def userProveedores(request):
    if request.method == "POST":
        proveedor_form = ProveedorForm(request.POST)
        print(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect("proveedores")
        else:
            proveedor_form = ProveedorForm()
            proveedores = Proveedores.objects.all()
            return render(request, "puntoVentaTemplates/userProveedores.html",{"form": proveedor_form, "proveedores": proveedores, "error": "*Porfavor introduzca un id diferente"})
    else:  # si es get, es decir cuando solo se entra a la pagina
        proveedor_form = ProveedorForm()
        proveedores = Proveedores.objects.all()
    return render(request, "puntoVentaTemplates/userProveedores.html", {"form": proveedor_form, "proveedores": proveedores})



def eliminar_proveedor(request,pk=""):  # se eliminara un objeto de la bd ESTA FUNCION NO DEVUELVE NINGUNA PAGINA SOLO ELIMINA AL AUTOR Y REDIRIJE A LA PAGINA QUE LOS LISTA PARA QUE YA NO APAREZCA
    proveedor_form = None
    error = None
    try:
        proveedor = Proveedores.objects.get(id_Proveedor=pk)  # SON LAS MISMAS CONSULTAS QUE HACEMOS EN SHELL
        if request.method == "GET":
            proveedor_form = ProveedorForm(instance=proveedor)  # creamos un formulario y lo renderizamos , decimos que la instancia que utilizara es el Cliente que busco el usuario por eso se pone la variable de arriba
        else:  # cuando se llega con POST
            proveedor = Proveedores.objects.get(id_Proveedor=pk)
            proveedor.delete()
            return redirect("proveedores")
    except ObjectDoesNotExist as e:
        error = e
    return render(request, 'puntoVentaTemplates/eliminar_userProveedores.html', {'form': proveedor_form, 'error': error, "iduser": pk, 'proveedor': proveedor})

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
