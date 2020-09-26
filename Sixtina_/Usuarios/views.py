from django.shortcuts import render, HttpResponse, redirect
from Usuarios.models import Usuario
from Usuarios.forms import FormUsuario
# Create your views here.
def login(request):
    return render(request, 'login.html')

def crear_usuario(request):
    return render(request, 'crear.html')

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
            ciudad = data_form.get('ciudad')
            info = data_form.get('info')

            user = Usuario(
                nombre = nombre,
                documento = documento,
                numero_documento = numero_documento,
                email = email,
                contraseña = contraseña,
                departamento = departamento,
                ciudad = ciudad,
                direccion = direccion,
                info = info
            )
            user.save()
            return render(request, 'index.html',{
                'user': user.nombre
            })
    else:
        formulario = FormUsuario()

    return render(request, 'create_usuario.html',{
        'form' : formulario
    })
