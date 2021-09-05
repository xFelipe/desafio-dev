from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def read_file(request):
    return HttpResponse('Hello world!')
