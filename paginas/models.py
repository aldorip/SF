# clientes/models.py
from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    pontos = models.IntegerField(default=0)
    saldo = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome
