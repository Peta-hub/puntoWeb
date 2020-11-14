from django import forms
from django.contrib.auth.forms import AuthenticationForm
from puntoVenta.models import Clientes


class FormularioLogin(AuthenticationForm):
    def __init__(self,*args,**kwargs): #es el metodo que ejecuta toda clase de python lo redifinimos
        super(FormularioLogin,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre del administrador global'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


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