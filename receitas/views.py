from django.shortcuts import render


def receita(request):

    receitas = {
        1:'Sopa de legumes',
        2:'Sorvete',
        3:'Lasanha',
        4:'Bolo de chocolate',
    }

    dados = {
        'nomes_da_receita':receitas,
    }

    return render(request, 'receitas/index.html', dados)


def imagem(request):
    return render(request, 'receitas/receita.html')
