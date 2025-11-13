from usuarios.models import Usuario
from django.core.exceptions import ObjectDoesNotExist

def crear_usuario(nombre, correo, password, rol='Usuario'):
    if Usuario.objects.filter(correo=correo).exists():
        return {'error': 'El correo ya está registrado'}

    nuevo_usuario = Usuario(
        nombre=nombre,
        correo=correo,
        password=password,
        rol=rol
    )
    nuevo_usuario.save()
    return {'mensaje': 'Usuario registrado exitosamente', 'usuario': nuevo_usuario}

def listar_s():
    return Usuario.objects.all()

def obtener_usuario_por_correo(correo):
    try:
        return Usuario.objects.get(correo=correo)
    except ObjectDoesNotExist:
        return None