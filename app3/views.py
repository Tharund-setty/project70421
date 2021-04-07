from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def carry_input(request,input):
    return HttpResponse(f'<h1>The user input is {input}</h1>')




