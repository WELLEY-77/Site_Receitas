from django.shortcuts import render


def receita(request):
    return render(request, 'receitas/index.html')
