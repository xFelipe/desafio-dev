from django.shortcuts import render
from django.http.response import HttpResponse
from movimentacoes_financeiras.core.forms import FinancialTransactionsFileForm

# Create your views here.
def read_file(request):
    return render(
        request,
        'financial_transactions.html',
        context={'form': FinancialTransactionsFileForm()}
    )
