from django.shortcuts import render, HttpResponse
from Usuarios.models import Usuario

user = Usuario.objects.get(nombre = 'default')
usuarios = Usuario.objects.all()
def index(request):
    is_already = False
    for usuario in usuarios:
        if user.email == usuario.email:
            is_already = True
            break
    if is_already:
        return render(request, 'index.html',{
            'user': user
        })
    else:
        return render(request, 'index.html',{
            'user': user
        })
def hombre(request):
    is_real = False
    for usuario in usuarios:
        if user.nombre == usuario.nombre:
            is_real = True
            break
    if is_real:
        return render(request, 'hombre.html',{
            'user': user
        })
    else:
        return render(request, 'hombre.html',{
            'user': user
        })

def mujer(request):
    is_real = False
    for usuario in usuarios:
        if user.nombre == usuario.nombre:
            is_real = True
            break
    if is_real:
        return render(request, 'mujer.html',{
            'user': user
        })
    else:
        return render(request, 'hombre.html',{
            'user': user
        })
