from django.shortcuts import render, HttpResponse

user = 'non'
def index(request):
    return render(request, 'index.html',{
        'user': user
    })

def hombre(request):
    return render(request, 'hombre.html',{
        'user': user
    })

def mujer(request):
    return render(request, 'mujer.html',{
        'user': user
    })
