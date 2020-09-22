from django.shortcuts import render

# Create your views here.
def user(request):
    return render(request, 'login.html')

def crear(request):
    return render(request, 'crear.html')
