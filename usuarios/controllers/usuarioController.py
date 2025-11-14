from django.shortcuts import render, redirect
from ..services.usuarioService import crear_usuario, listar_s
from ..services.roles import crear_rol

def controller_registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        rol = request.POST.get('rol', 'Usuario')

        resultado = crear_usuario(nombre, correo, password, rol)

        if 'error' in resultado:
            return render(request, 'registrar_usuario.html', {'error': resultado['error']})
        else:
            return redirect('listarUsuarios')

    return render(request, 'registrar_usuario.html')

def controller_listar_usuarios(request):
    usuarios = listar_s()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})

def controller_registrar_rol(request):
    if request.method == 'POST':
        nombre_rol = request.POST.get('nombre_rol')
        descripcion = request.POST.get('descripcion')

        result = crear_rol(nombre_rol, descripcion)

        if 'error' in result:
            return render(request, 'crear_rol.html', {'error': result['error']})
        else:
            return redirect('listarRoles')
    return render(request, 'crear_rol.html')