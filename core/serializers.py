from rest_framework import serializers
from core.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "tipo",
            "data_e_hora",
            "valor",
            "cpf",
            "cartao",
            "dono_da_loja",
            "nome_loja",
        ]
