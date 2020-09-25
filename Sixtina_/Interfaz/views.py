from django.shortcuts import render, HttpResponse

user = None
def index(request):
    return render(request, 'index.html',{
        'user':user
    })
