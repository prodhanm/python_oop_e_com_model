from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("<h1>Hello, world. You're at the e_com_store.</h1>")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("<h1>About page</h1>")