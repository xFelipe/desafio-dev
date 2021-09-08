from django.shortcuts import HttpResponseRedirect, render
from django.shortcuts import resolve_url as r
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from core.forms import TransactionForm, TransactionsFileForm
from core.models import Transaction
from core.helpers import format_transactions, read_file
import logging


class TransactionsListApi(APIView):
    """View to list all transactions or input transactions"""

    renderer_classes = [JSONRenderer]

    def get(self, request):
        transactions = format_transactions(Transaction.objects.all())
        return JsonResponse({"transactions": transactions}, safe=True)

    def post(self, request):
        print({"files": request.FILES, "data": request.data})
        form = TransactionsFileForm(request.POST, request.FILES)
        try:
            form.is_valid()
            transactions = read_file(form.cleaned_data["cnab_file"])
        except Exception as e:
            logging.exception(e)
            return JsonResponse(
                {"erro": "Formatação de arquivo inválida."}, safe=True, status=400
            )
        for t in transactions:
            t.save()
            logging.info(t.__dict__)
        return JsonResponse({"message": f"{len(transactions)} Transações salvas com sucesso!"}, safe=True, status=201)


# Create your views here.
def get_transactions(request):
    """HTML input file form"""
    transactions = format_transactions(Transaction.objects.all().order_by('nome_loja', 'data_e_hora'))
    # transactions = format_transactions(Transaction.objects.all().order_by('data_e_hora'))
    return render(
        request,
        "financial_transactions.html",
        context={"form": TransactionsFileForm(), "transactions": transactions},
    )


def post_file(request):
    """Read and persist financial transactions and redirect with status message"""
    form = TransactionsFileForm(request.POST, request.FILES)
    try:
        form.is_valid()
        transactions = read_file(form.cleaned_data["cnab_file"])
    except Exception as e:
        messages.add_message(request, messages.ERROR, 'Formatação de arquivo inválida.')
        logging.exception(e)
        return HttpResponseRedirect(r("get_transactions"))

    for t in transactions:
        t.save()
        logging.info(t.__dict__)

    messages.add_message(request, messages.SUCCESS, 'Transações inseridas com sucesso!')
    return HttpResponseRedirect(r("get_transactions"))
