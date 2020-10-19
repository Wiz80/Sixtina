from django.shortcuts import render
from Clothes.models import Ropa_Hombre
import math
# Create your views here.
def camisetas(request):
    todos = Ropa_Hombre.objects.all()
    camisetas = []
    for todo in todos:
        if todo.is_camiseta:
            camisetas.append(todo)
    return render(request, 'camisetas.html', {
        'camisetas': camisetas,
        'contador' : range(2)
    })

def camiseta(request,id):
    rango = range(4)
    camiseta = Ropa_Hombre.objects.get(is_camiseta = True,Idn = id)
    fotos = [camiseta.imagen_1, camiseta.imagen_2, camiseta.imagen_3, camiseta.imagen_4]
    for foto in fotos:
        if foto is 'null':
            fotos.remove(foto)
    colores = camiseta.Colores.split(',')
    return render(request, 'camiseta.html',{
        'camiseta': camiseta,
        'fotos': fotos,
        'colores': colores
    })
