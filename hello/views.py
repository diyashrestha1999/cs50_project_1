from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def brian(request):
    return HttpResponse("hello brian")

def david(request):
    return HttpResponse("hello david")
def greet(request,name):
    return render(request, "hello/greet.html",{"name":name.capitalize()})