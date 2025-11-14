from proyectos.models import Proyecto
from django.core.exceptions import ObjectDoesNotExist

def crear_proyecto(nombre, descripcion, categoria, creador, monto_requerido, estado='En revisión', usuario=None):
    if Proyecto.objects.filter(nombre=nombre, creador=creador).exists():
        return {'error': 'Ya existe un proyecto con este nombre para este creador.'}
    
    nuevo_proyecto = Proyecto(
        nombre=nombre,
        descripcion=descripcion,
        categoria=categoria,
        creador=creador,
        monto_requerido=monto_requerido,
        estado=estado,
    )
    nuevo_proyecto.save()
    return {'mensaje': 'Proyecto creado exitosamente', 'proyecto': nuevo_proyecto}


def listar_proyectos():
    return Proyecto.objects.all()


def obtener_proyecto_por_id(id):
    try:
        return Proyecto.objects.get(id=id)
    except ObjectDoesNotExist:
        return None