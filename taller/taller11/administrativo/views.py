from django.shortcuts import render, redirect
from administrativo.models import *

# Create your views here.
def index(request):
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numero_edificios': len(edificios)}
    return render(request, 'index.html', informacion_template)

def crear_edificio(request):
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio.html', diccionario)


def crear_departamento(request):
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEdificio.html', diccionario)

def obtener_edificio(request, id):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    edificio = Edificio.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'edificio': edificio}
    return render(request, 'obtenerEdificio.html', informacion_template)