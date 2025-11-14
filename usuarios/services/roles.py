from usuarios.models import Roles
from django.core.exceptions import ObjectDoesNotExist

def crear_rol(nombre_rol, descripcion='Nuevo rol'):
    if Roles.objects.filter(nombre_rol=nombre_rol).exists():
        return{"error": "Este rol ya existe"}

    nuevo_rol = Roles(
        nombre_rol = nombre_rol,
        descripcion = descripcion
    )
    nuevo_rol.save()
    return("Usuario creado con exito")