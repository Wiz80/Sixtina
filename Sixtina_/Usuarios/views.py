from django.shortcuts import render, HttpResponse, redirect
from Usuarios.models import Usuario
from Usuarios.forms import FormUsuario
from Usuarios.forms import FormLogin
import hashlib

# Create your views here.
def login(request):
    if request.method == 'POST':
        formulario = FormLogin(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            email = data_form.get('email')
            contraseña = data_form.get('contraseña')
            cifrado = hashlib.sha256()
            cifrado.update(contraseña.encode('utf8'))
            try:
                user = Usuario.objects.get(email=email, contraseña=cifrado.hexdigest())
            except:
                user = False
            if user:
                return redirect('/',{
                    'user':user.nombre.upper()
                })
            else:
                return render(request, 'login.html', {
                    'form': formulario,
                    'msg': 'Su E-mail o contraseña no coinciden'
                })
    else:
        formulario = FormLogin()
    return render(request, 'login.html',{
        'form': formulario
    })


def nuevo_usuario(request):

    if request.method == 'POST':
        formulario = FormUsuario(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            email = data_form.get('email')
            contraseña = data_form.get('contraseña')
            cifrado = hashlib.sha256()
            cifrado.update(contraseña.encode('utf8'))
            nombre = data_form.get('nombre')
            documento = data_form.get('documento')
            numero_documento = data_form.get('numero_documento')
            departamento = data_form.get('departamento')
            direccion = data_form.get('direccion')
            ciudad = data_form.get('ciudad')
            info = data_form.get('info')
            usuarios = Usuario.objects.all()
            user = Usuario(
                nombre = nombre,
                documento = documento,
                numero_documento = numero_documento,
                email = email,
                contraseña = cifrado.hexdigest(),
                departamento = departamento,
                ciudad = ciudad,
                direccion = direccion,
                info = info
            )
            is_already = False
            if usuarios:
                for usuario in usuarios:
                    if usuario.email == user.email:
                        is_already = True
                        break

            if is_already:
                formulario = FormUsuario()
                return render(request, 'create_usuario.html',{
                    'form': formulario,
                    'msg': 'El usuario ya tiene una cuenta en Sixtina.com'
                })
            else:
                user.save()
                return render(request, 'index.html',{
                    'user': user.nombre.upper()
                })
    else:
        formulario = FormUsuario()

    return render(request, 'create_usuario.html',{
        'form' : formulario
    })
