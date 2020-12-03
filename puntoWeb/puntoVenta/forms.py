from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from puntoVenta.models import Clientes, Productos, Proveedores, Recuperar, Materiales, Compras, Ventas, Detalles



class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs): #es el metodo que ejecuta toda clase de python lo redifinimos
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña del administrador',
            'first_name': 'Nombre real del administrador',
            'last_name': 'Apellidos del administrador',
            'email': 'Correo del administrador',
        }

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre de usuario',
                    'id': 'usr'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la contraseña del administrador',
                    'id': 'pwd'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del administrador',
                    'id': 'nombres'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese los apellidos del administrador',
                    'id': 'apellidos'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo del administrador',
                    'id': 'correo'
                }
            ),
        }


    def save(self, commit=True):
        user = super().save(commit=False)  # MML se redefine la forma en que se guarda la contraseña
        pwd_hash = make_password(self.cleaned_data['password'])
        user.password = pwd_hash
        if commit:
            user.save()
        return user



class RecuperarForm(forms.ModelForm):
    class Meta:
        model = Recuperar
        fields = ('user', 'pregunta_secreta', 'respuesta')
        label = {
            'user': 'user',
            'pregunta_secreta': 'pregunta_secreta',
            'respuesta': 'Respuesta',
        }
        widgets = {
            'user': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'identificador',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'pregunta_secreta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'pregunta_secreta',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'respuesta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'respuesta',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
        }




class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('id', 'nombre', 'apellidos', 'direccion', 'telefono')
        label = {
            'id': 'id',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
        }
        widgets = {
            'id': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'identificador',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'style': 'background-color: #FEFCAE',
                    'size': '25'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'apellidos',
                    'style': 'background-color: #FEFCAE',
                    'size': '30'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'style': 'background-color: #FEFCAE',
                    'size': '30'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                    'style': 'background-color: #FEFCAE',
                    'size': '15'
                }
            ),
        }




class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = ('id_Proveedor', 'nombre', 'direccion', 'telefono')
        label = {
            'id_Proveedor': 'id_Proveedor',
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
        }
        widgets = {
            'id_Proveedor': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'identificador',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'style': 'background-color: #FEFCAE',
                    'size': '25'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'style': 'background-color: #FEFCAE',
                    'size': '30'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                    'style': 'background-color: #FEFCAE',
                    'size': '20'
                }
            ),
        }





class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ('codigo', 'nombre', 'categoria', 'precio')
        label = {
            'codigo': 'Codigo',
            'nombre': 'Nombre',
            'categoria': 'Categoria',
            'precio': 'Precio',
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'identificador',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'style': 'background-color: #FEFCAE',
                    'size': '25'
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                    'style': 'background-color: #FEFCAE',
                    'size': '30'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'style': 'background-color: #FEFCAE',
                    'size': '20'
                }
            ),
        }




class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = ('id_Material', 'nombre', 'medidas', 'precio')
        label = {
            'id_Material': 'id_Material',
            'nombre': 'Nombre',
            'medidas': 'Medidas',
            'precio': 'precio',
        }
        widgets = {
            'id_Material': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'identificador',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'style': 'background-color: #FEFCAE',
                    'size': '25'
                }
            ),
            'medidas': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'medidas',
                    'style': 'background-color: #FEFCAE',
                    'size': '30'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'style': 'background-color: #FEFCAE',
                    'size': '20'
                }
            ),
        }




class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalles
        fields = ('codigo', 'producto', 'material', 'cantidad')
        label = {
            'codigo': 'id_Material',
            'producto': 'Producto',
            'material': 'Material',
            'cantidad': 'cantidad',
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'identificador',
                    'style': 'background-color: #FEFCAE',
                    'size': '10'
                }
            ),
            'producto': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'material': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                    'style': 'background-color: #FEFCAE',
                    'size': '20'
                }
            ),
        }




class CompraForm(forms.ModelForm):
    class Meta:
        model = Compras
        fields = ('cantidad', 'precio', 'material', 'proveedor')
        label = {
            'cantidad': 'Cantidad: ',
            'precio': 'Precio: ',
            'material': 'Material: ',
            'proveedor': 'Proveedor: ',
        }
        widgets = {
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                    'style': 'background-color: #FEFCAE',
                    'size': '2'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'precio',
                    'style': 'background-color: #FEFCAE',
                    'size': '2'
                }
            ),
            'material': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'proveedor': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }



class VentaForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ('cantidad', 'precio', 'producto', 'cambio','paga')
        label = {
            'cantidad': 'Cantidad: ',
            'precio': 'Precio: ',
            'material': 'Material: ',
            'proveedor': 'Proveedor: ',
        }
        widgets = {
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cantidad',
                    'style': 'background-color: #FEFCAE',
                    'size': '2'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'precio',
                    'style': 'background-color: #FEFCAE',
                    'size': '4'
                }
            ),
            'producto': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'cambio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'cambio',
                    'style': 'background-color: #FEFCAE',
                    'size': '2'
                }
            ),
            'paga': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'paga',
                    'style': 'background-color: #FEFCAE',
                    'size': '4'
                }
            ),
        }

    def save(self, commit=True):
        venta = super().save(commit=False)

        valor = (self.cleaned_data['precio'])
        pagar = (self.cleaned_data['paga'])


        cambio = float(pagar) - float(valor)

        venta.cambio = cambio
        if commit:
            venta.save()
        return venta