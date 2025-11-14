from .controllers.usuarioController import controller_registro_usuario, controller_listar_usuarios, controller_registrar_rol
from django.shortcuts import render


# def index(request):
#     return render(request, 'index.html')

def listar_usuario(request):
    return controller_listar_usuarios(request)

def registrar_usuario(request):
    return controller_registro_usuario(request)

def reg_rol(request):
    return controller_registrar_rol(request)

def listar_roles(request):
    return render(request, 'listar_roles.html')