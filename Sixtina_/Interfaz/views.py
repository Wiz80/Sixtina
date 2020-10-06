from django.shortcuts import render, HttpResponse
from Usuarios.models import Usuario

user = None
def index(request):
    try:
        if user is not None:
            
        return render(request, 'index.html',{
            'user':user
        })
    except:
        return render(request, 'index.html')

def hombre(request):
    try:
        return render(request, 'hombre.html',{
            'user': user
        })
    except:
        return render(request, 'hombre.html')

def mujer(request):
    try:
        return render(request, 'mujer.html',{
            'user': user
        })
    except:
        return render(request, 'mujer.html')
