from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

