from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Olá mundo, somos o grupo 6")
