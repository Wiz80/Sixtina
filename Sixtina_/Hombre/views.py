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
