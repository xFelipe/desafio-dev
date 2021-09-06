from django import forms
from core.models import Transaction

class TransactionsFileForm(forms.Form):
    cnab_file = forms.FileField(
        label='Selecione um arquivo CNAB'
    )


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['tipo', 'datetime', 'valor', 'cpf',
                  'cartao', 'dono_da_loja', 'nome_loja']
