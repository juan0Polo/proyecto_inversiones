from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_proyecto_view, name='crearProyecto'),
    path('listar/', views.listar_proyectos_view, name='listarProyectos'),
]