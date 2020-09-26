from django.shortcuts import render, HttpResponse

user = 'non'
def index(request):
    return render(request, 'index.html',{
        'user': user
    })
