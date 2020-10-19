from django.shortcuts import render, HttpResponse
from Usuarios.models import Usuario
from .forms import UserForm
from django.contrib import messages

def hombre(request):
    user_register = UserForm()
    if request.method == 'POST':
        user_register = UserForm(request.POST)
        if user_register.is_valid():
            user_register.save()
            messages.success(request, 'Bienvenido, ya eres parte de Sixtina')

    return render(request, 'hombre.html',{
        'user_register': user_register
    })

def mujer(request):
    user_register = UserForm()
    if request.method == 'POST':
        user_register = UserForm(request.POST)
        if user_register.is_valid():
            user_register.save()
            messages.success(request, 'Bienvenido, ya eres parte de Sixtina')

    return render(request, 'mujer.html',{
        'user_register': user_register
    })
