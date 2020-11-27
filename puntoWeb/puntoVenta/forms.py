from django import forms
from django.contrib.auth.forms import AuthenticationForm
from puntoVenta.models import Clientes, Productos, Proveedores, Recuperar, Materiales


class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs): #es el metodo que ejecuta toda clase de python lo redifinimos
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'



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
