
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('crear/edificio', views.crear_edificio, name='crear_edificio'),
        path('crear/departamento', views.crear_departamento, name='crear_departamento'),
        path('edicio/<int:id>', views.listar_edificio, name='listar_edificio'),
        path('editar/edicio/<int:id>', views.editar_edificio, name='editar_edificio'),
        path('eliminar/edificio/<int:id>', views.eliminar_edificio, 
            name='eliminar_edificio'),
        path('crear/nuevo/departamento_edificio/<int:id>', 
            views.crear_departamento_edificio,
             name='crear_departamento_edificio'),
 ]
