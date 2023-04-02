from django.db import models
from datetime import datetime

class Receita(models.Model):
    nome_receita = models.CharField('Nome da Receita', max_length=100)
    ingredientes = models.TextField('Igredientes')
    modo_preparo = models.TextField('Modo de Preparo')
    tempo_preparo = models.IntegerField('Tempo de Preparo')
    rendimento = models.CharField('Remdimento', max_length=100)
    categoria = models.CharField('Categoria', max_length=100)
    date_receita = models.DateTimeField(' Data da Receita ', default=datetime.now, blank=True)
