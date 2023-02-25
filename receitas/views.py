from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Receita


def receita(request):

    receitas = Receita.objects.all()
                 
    dados = {
        'receitas':receitas,
    }

    return render(request, 'receitas/index.html', dados)


def imagem(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }
    return render(request, 'receitas/receita.html', receita_a_exibir)
