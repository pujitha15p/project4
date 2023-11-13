from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def silk(request):
    return HttpResponse('<marqee><h1>no need silk</marqee></h1>')

def varma(request):
    return HttpResponse('<marqee><h1>worth varma</marqee></h1>')