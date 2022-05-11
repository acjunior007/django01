from multiprocessing import context
from django.shortcuts import render

from core.models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programacao com Django Frameword',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, id):
    print(f'Id: {id}')
    prod = Produto.objects.get(id=id)
    context = {
        'produto': prod
    }
    return render(request, 'produto.html', context)
