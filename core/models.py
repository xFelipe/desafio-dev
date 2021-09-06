from django.db import models
from core.helpers import TransactionType, positive, negative

TRANSACTION_TYPES = {
    1: TransactionType("Débito", positive),
    2: TransactionType("Boleto", negative),
    3: TransactionType("Financiamento", negative),
    4: TransactionType("Crédito", positive),
    5: TransactionType("Recebimento Empréstimo", positive),
    6: TransactionType("Vendas", positive),
    7: TransactionType("Recebimento TED", positive),
    8: TransactionType("Recebimento DOC", positive),
    9: TransactionType("Aluguel", negative)
}

class Transaction(models.Model):
    tipo = models.IntegerField()
    datetime =  models.DateTimeField('data e hora')
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    cpf = models.CharField(max_length=11)
    cartao = models.CharField(max_length=12)
    dono_da_loja =  models.CharField(max_length=14)
    nome_loja = models.CharField(max_length=19)
