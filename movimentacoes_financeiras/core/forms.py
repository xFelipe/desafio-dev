from django import forms

class FinancialTransactionsFileForm(forms.Form):
    cnab_file = forms.FileField(
        label='Selecione um arquivo CNAB',
        required=True
    )