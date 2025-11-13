from .controllers.usuarioController import controller_registro_usuario, controller_listar_usuarios
from django.shortcuts import render


# def index(request):
#     return render(request, 'index.html')

def listar_usuario(request):
    return controller_listar_usuarios(request)

def registrar_usuario(request):
    return controller_registro_usuario(request)