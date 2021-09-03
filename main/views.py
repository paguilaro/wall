from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        name = request.POST['name']
