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

    lista_receita = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']

        if nome_a_buscar:
            lista_receita = lista_receita.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas' : lista_receita
    }



    return render(request, 'receitas/buscar.html', dados)