from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import resolve_url as r
from core.forms import TransactionsFileForm
from core.models import Transaction
from datetime import datetime, timezone, timedelta

# Create your views here.
def input_file(request):
    """HTML input file form"""
    return render(
        request,
        'financial_transactions.html',
        context={'form': TransactionsFileForm()}
    )

def send_file(request):
    """Persist financial transactions and redirect with message"""
    form = TransactionsFileForm(request.POST, request.FILES)
    if not form.is_valid():
        return HttpResponseRedirect(r('input_file'))

    transactions = _read_file(form.cleaned_data['cnab_file'])
    for t in transactions:
        t.save()
        print(t.__dict__) 
    return HttpResponseRedirect(r('input_file'))

def _read_file(file: InMemoryUploadedFile):
    content = file.read().decode('utf-8')
    return [_read_line(line) for line in content.split('\n') if line.strip()]

def _read_line(line: str):
    return Transaction(
        tipo= line[0],                         # Tipo da transação
        datetime= datetime(
            year=int(line[1:5]),
            month=int(line[5:7]),
            day=int(line[7:9]),
            hour=int(line[42:44]),
            minute=int(line[44:46]),
            second=int(line[46:48]),
            tzinfo=timezone(timedelta(hours=-3))
        ),                                     # Data da ocorrência
        valor = int(line[9:19])/100,           # Valor da movimentação. Obs. O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo.
        cpf = line[19:30],                     # CPF do beneficiário
        cartao = line[30:42],                  # Cartão utilizado na transação
        dono_da_loja = line[48:62].rstrip(),   # Nome do representante da loja
        nome_loja = line[62:].rstrip()         # Nome da loja
    )
