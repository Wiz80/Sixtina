from django.shortcuts import render

# Create your views here.
def compra_articulo(request):
    return render(request, 'compra.html')
