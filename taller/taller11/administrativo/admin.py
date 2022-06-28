from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Departamento, Edificio
admin.site.register(Edificio)
admin.site.register(Departamento)