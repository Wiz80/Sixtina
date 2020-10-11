from django.shortcuts import render

# Create your views here.
def ropa(request):
    return render(request, 'ropa.html')

def template_ropa(request):
    return render(request, 'template-ropa.html')
