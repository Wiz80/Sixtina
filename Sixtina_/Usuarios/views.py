from django.shortcuts import render, HttpResponse
from Usuarios.models import Usuario
from Usuarios.forms import FormUsuario
# Create your views here.
def login(request):
    return render(request, 'login.html')

def crear_usuario(request):
    return render(request, 'crear.html')

def save_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        documento = request.POST['documento']
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        departamento = request.POST['departamento']
        municipio = request.POST['municipio']
        direccion = request.POST['direccion']

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

def nuevo_usuario(request):

    if request.method == 'POST':
        formulario = FormUsuario(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            email = data_form.get('email')
            contraseña = data_form.get('contraseña')
            nombre = data_form.get('nombre')
            documento = data_form.get('documento')
            numero_documento = data_form.get('numero_documento')
            departamento = data_form.get('departamento')
            direccion = data_form.get('direccion')
            usuario = Usuario(
                nombre = nombre,
                documento = documento,
                numero_documento = numero_documento,
                email = email,
                contraseña = contraseña,
                departamento = departamento,
                municipio = municipio,
                direccion = direccion
            )
            usuario.save()
            return HttpResponse(f"<h1>Hola {usuario.nombre} </h1>")
    else:
        formulario = FormUsuario()

    return render(request, 'create_usuario.html',{
        'form' : formulario
    })
