from django.shortcuts import render
from .models import Receita


def receita(request):

    receitas = Receita.objects.all()
                 
    dados = {
        'receitas':receitas,
    }

    return render(request, 'receitas/index.html', dados)


def imagem(request):
    return render(request, 'receitas/receita.html')
