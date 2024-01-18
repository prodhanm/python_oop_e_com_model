from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, world. You're at the e_com_store.</h1>")
