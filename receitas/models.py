from django.db import models
from datetime import datetime
from pessoas.models import Pessoa
from django.contrib.auth.models import User


class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField('Nome da Receita', max_length=100)
    ingredientes = models.TextField('Igredientes')
    modo_preparo = models.TextField('Modo de Preparo')
    tempo_preparo = models.IntegerField('Tempo de Preparo')
    rendimento = models.CharField('Remdimento', max_length=100)
    categoria = models.CharField('Categoria', max_length=100)
    date_receita = models.DateTimeField(' Data da Receita ', default=datetime.now, blank=True)
    publicada = models.BooleanField('Publicada', default=False)
    foto_receita = models.ImageField('Imagem da Receita', blank=True, upload_to='fotos/%d/%m/%Y')

    def __str__(self):
        return self.pessoa

