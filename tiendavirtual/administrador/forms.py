from django import forms
from django.contrib.auth.models import User
from tienda.models import Empleado,Tiendas,Localizacion
from productos.models import Producto


class RegistrarTiendaForm(forms.ModelForm):
    class Meta:
        model = Tiendas
        fields = ["nombre", "direccion", "localizacion", "horario_atencion", "telefono", "imagen"]
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'validate',
                       'required': True},
            ),
            'direccion': forms.Textarea(
                attrs={'class': 'descripcion materialize-textarea',
                       'required': True}
            ),
            'horario_atencion': forms.TextInput(
                attrs={'class': 'validate',
                       'required': True}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'validate',
                       'required': True}
            ),
            'horario_atencion': forms.TextInput(
                attrs={'class': 'validate',
                       'required': False}
            ),
            'telefono': forms.TextInput(
                attrs={'class': 'validate',
                       'required': False}
            ),
            'imagen': forms.FileInput(
                attrs={'class': 'validate',
                       'required': False}
            ),
        }

class RegistrarLocalizacionForm(forms.ModelForm):
    class Meta:
        model = Localizacion
        fields = ["latitud", "longitud"]
        widgets = {
            'latitud': forms.TextInput(
                attrs={'class': 'validate latitud',
                       'required': False}
            ),
            'longitud': forms.TextInput(
                attrs={'class': 'validate longitud',
                       'required': False}
            ),
        }

class RegistrarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "precio", "descripcion","imagen","categoria","subcategoria","estado"]
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'validate',
                       'required': False}
            ),
            'precio': forms.TextInput(
                attrs={'class': 'validate',
                       'required': False}
            ),
            'descripcion': forms.Textarea(
                attrs={'class': 'validate',
                       'required': False}
            ),
            'imagen': forms.FileInput(
                attrs={'class': 'validate',
                       'required': False}
            ),
            'descripcion': forms.TextInput(
                attrs={'class': 'validate',
                       'required': False}
            ),            
        }