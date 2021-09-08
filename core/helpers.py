from collections.abc import Callable
from datetime import datetime, timezone, timedelta
from numbers import Number
from typing import NamedTuple
from django.core.files.uploadedfile import InMemoryUploadedFile
from core.models import Transaction


class TransactionType(NamedTuple):
    name: str
    operation: Callable[[Number], Number]


def positive(n: Number):
    return abs(n)


def negative(n: Number):
    return -abs(n)


TRANSACTION_TYPES = {
    1: TransactionType("Débito", positive),
    2: TransactionType("Boleto", negative),
    3: TransactionType("Financiamento", negative),
    4: TransactionType("Crédito", positive),
    5: TransactionType("Recebimento Empréstimo", positive),
    6: TransactionType("Vendas", positive),
    7: TransactionType("Recebimento TED", positive),
    8: TransactionType("Recebimento DOC", positive),
    9: TransactionType("Aluguel", negative),
}


def format_transactions(ordered_transactions: list) -> list[dict]:
    formated_transactions = []
    for t in ordered_transactions:
        transaction_value = TRANSACTION_TYPES[t.tipo].operation(t.valor)
        previous_total = sum([
            ft['valor'] for ft in formated_transactions
            if ft['nome_loja']==t.nome_loja
        ])
        formated_transactions.append(
            {
                "id": t.id,
                "tipo": TRANSACTION_TYPES[t.tipo].name,
                "data_e_hora": t.data_e_hora,
                "valor": transaction_value,
                "cpf": t.cpf,
                "cartao": t.cartao,
                "dono_da_loja": t.dono_da_loja,
                "nome_loja": t.nome_loja,
                "saldo_em_conta": previous_total + transaction_value
            }
        )
    return formated_transactions


def read_file(file: InMemoryUploadedFile):
    content = file.read().decode("utf-8")
    return [_read_line(line) for line in content.split("\n") if line.strip()]


def _read_line(line: str):
    return Transaction(
        tipo=line[0],  # Tipo da transação
        data_e_hora=datetime(
            year=int(line[1:5]),
            month=int(line[5:7]),
            day=int(line[7:9]),
            hour=int(line[42:44]),
            minute=int(line[44:46]),
            second=int(line[46:48]),
            tzinfo=timezone(timedelta(hours=-3)),
        ),  # Data da ocorrência
        valor=int(line[9:19])
        / 100,  # Valor da movimentação. Obs. O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
        cpf=line[19:30],  # CPF do beneficiário
        cartao=line[30:42],  # Cartão utilizado na transação
        dono_da_loja=line[48:62].rstrip(),  # Nome do representante da loja
        nome_loja=line[62:].rstrip(),  # Nome da loja
    )
