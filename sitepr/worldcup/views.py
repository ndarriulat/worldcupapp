from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello,world. Esta e a pagina de entrada da app votacao.")