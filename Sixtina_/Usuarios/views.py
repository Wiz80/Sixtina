from django.shortcuts import render
from Usuarios.models import Usuario
# Create your views here.
def login(request):
    return render(request, 'login.html')

def crear_usuario(request):
    return render(request, 'crear.html')

def save_usuario(request):
    if request.method == 'GET':
        nombre = request.GET['nombre']
        apellidos = request.GET['apellidos']
        documento = request.GET['documento']
        email = request.GET['email']
        contraseña = request.GET['contraseña']
        departamento = request.GET['departamento']
        municipio = request.GET['municipio']
        direccion = request.GET['direccion']

        usuario = Usuario(
            nombre = nombre,
            apellidos = apellidos,
            documento = documento,
            email = email,
            contraseña = contraseña,
            departamento = departamento,
            municipio = municipio,
            direccion = direccion
        )
        usuario.save()
        return HttpResponse(f"<h1>Hola {nombre} </h1>")
    else:
        return HttpResponse("<h1>NO SE HA CREADO EL USUARIO</h1>")
