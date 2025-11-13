from django.shortcuts import render, redirect
from ..service.proyectoService import crear_proyecto, listar_proyectos

def controller_crear_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        creador = request.POST.get('creador')
        monto_requerido = request.POST.get('monto_requerido')

        resultado = crear_proyecto(nombre, descripcion, categoria, creador, monto_requerido)

        if 'error' in resultado:
            return render(request, 'crear_proyecto.html', {'error': resultado['error']})
        else:
            return redirect('listarProyectos')

    return render(request, 'crear_proyecto.html')

def controller_listar_proyectos(request):
    proyectos = listar_proyectos()
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})