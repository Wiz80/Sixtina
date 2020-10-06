from django.shortcuts import render, HttpResponse

def index(request):
    try:
        return render(request, 'index.html',{
            'user': user
        })
    except:
        return render(request, 'index.html')
