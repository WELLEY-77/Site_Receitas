from django.db import models

class Pessoa(models.Model):
    nome = models.CharField('Nome da Pessoa', max_length=100)
    email = models.CharField('E-mail', max_length=150)