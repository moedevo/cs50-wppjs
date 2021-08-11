from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "hellodjango/index.html")

def greet(request, name):
    return render(request, "hellodjango/greet.html", {
        "name": name.capitalize()
    })