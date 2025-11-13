from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.registrar_usuario, name='crearUsuario'),
    path('listar/', views.listar_usuario, name='listarUsuarios'),
]