from django.shortcuts import render, redirect
from administrativo.models import *
from administrativo.forms import *

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

    return render(request, 'crearDepartamento.html', diccionario)

def listar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificio': edificio}
    return render(request, 'listarEdificio.html', informacion_template)

def editar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)

def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def crear_departamento_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(request.POST, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}
    return(render(request, 'crearDepartamentoEdificio.html', diccionario))
