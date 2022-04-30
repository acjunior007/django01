from multiprocessing import context
from django.shortcuts import render

def index(request):
    context = {
        'curso': 'Programacao com Django Frameword'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')