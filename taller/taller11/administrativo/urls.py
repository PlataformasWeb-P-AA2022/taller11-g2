
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('crear/edificio', views.crear_edificio, name='crear_edifico'),
        path('crear/departamento', views.crear_departamento, name='crear_departamento'),
        path('edicio/<int:id>', views.obtener_edificio, name='obtener_edificio')
 ]
