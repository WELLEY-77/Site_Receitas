from django.shortcuts import get_object_or_404, render
from .models import Receita


def receita(request):

    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
                 
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


def buscar(request):
    return render(request, 'receitas/buscar.html')