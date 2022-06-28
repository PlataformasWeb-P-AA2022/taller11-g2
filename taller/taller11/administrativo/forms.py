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

