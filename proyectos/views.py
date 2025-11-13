from .controller.proyectoController import controller_crear_proyecto, controller_listar_proyectos

def crear_proyecto_view(request):
    return controller_crear_proyecto(request)

def listar_proyectos_view(request):
    return controller_listar_proyectos(request)