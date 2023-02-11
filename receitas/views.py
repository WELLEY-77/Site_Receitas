from django.shortcuts import render


def receita(request):
    return render(request, 'receitas/index.html')


def imagem(request):
    return render(request, 'receitas/receita.html')
