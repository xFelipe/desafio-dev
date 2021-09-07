from django.db import models


class Transaction(models.Model):
    tipo = models.IntegerField()
    data_e_hora = models.DateTimeField('data e hora')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    dono_da_loja = models.CharField('dono da loja', max_length=14)
    nome_loja = models.CharField('nome da loja', max_length=19)
