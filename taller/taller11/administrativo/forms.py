from cProfile import label
from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Departamento, Edificio

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del edificio'),
            'direccion': _('Ingrese la direccion'),
            'ciudad': _('Ingrese la ciudad'),
            'tipo': _('Ingrese el tipo de edificio'),
        }
    
    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        print(valor)
        if valor.startswith("L"):
            raise forms.ValidationError("La ciudad no puede unicionar la letra L")
        return valor
    

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costoDepartamento', 'numeroCuartos', 'edificio']
        labels = {
            'nombrePropietario': _('Ingrese el nombre del propietario'),
            'costoDepartamento': _('Ingrese el costo del departamento'),
            'numeroCuartos': _('Ingrese el numero de cuartos'),
            'edificio': _('Ingrese el edificio'),
        }
    
    def clean_costoDepartamento(self):
        valor = self.cleaned_data['costoDepartamento']
        if valor > 100000:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a 100 mil")
        return valor

    def clean_numeroCuartos(self):
        valor = self.cleaned_data['numeroCuartos']
        if valor > 7 or valor == 1:
            raise forms.ValidationError("El numero de cuartos no puede ser 0 o mayor a 7")
        return valor

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre del propietario debe tener al menos 3 palabras")
        return valor
    
class DepartamentoEdificioForm(ModelForm):

    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['nombrePropietario', 'costoDepartamento', 'numeroCuartos', 'edificio']

    def clean_costoDepartamento(self):
        valor = self.cleaned_data['costoDepartamento']
        if valor > 100000:
            raise forms.ValidationError("El costo del departamento no puede ser mayor a 100 mil")
        return valor

    def clean_numeroCuartos(self):
        valor = self.cleaned_data['numeroCuartos']
        if valor > 7 or valor == 1:
            raise forms.ValidationError("El numero de cuartos no puede ser 0 o mayor a 7")
        return valor

    def clean_nombrePropietario(self):
        valor = self.cleaned_data['nombrePropietario']
        num_palabras = len(valor.split())

        if num_palabras < 3:
            raise forms.ValidationError("El nombre del propietario debe tener al menos 3 palabras")
        return valor