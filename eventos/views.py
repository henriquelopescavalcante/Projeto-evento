import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from eventos.models import Evento, Categoria
from eventos.forms import InscricaoForm


def inicio(request):
    eventos = Evento.objects.filter(destaque=True)
    contexto = {
        'ano': dt.datetime.now().year,
        'categorias': Categoria.objects.all(),
        'eventos': eventos,
    }
    return render(request, 'inicio.html', contexto)


def inscricao(request):
    contexto = {
        'categorias': [],
    }
    if request.method == 'POST':
        form = InscricaoForm(request.POST)
        if form.is_valid():
            form.save()
            contexto['sucesso'] = True
    else:
        form = InscricaoForm()
    contexto['form'] = form
    return render(request, 'inscricao.html', contexto)


def categoria(request, id):
    categoria_selecionada = Categoria.objects.get(id=id)
    contexto = {
        'categorias': Categoria.objects.all(),
        'categoria_selecionada': categoria_selecionada,
        'eventos': Evento.objects.filter(categoria=categoria_selecionada),
    }
    return render(request, 'categoria.html', contexto)
