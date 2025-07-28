from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render(request,'home.html')

def store(request):
    return HttpRequest("Welcome")

def search(request):
    return HttpRequest("Test")

def login(request):
    return HttpRequest("Login")

def register(request):
    return HttpRequest("Register")

def cart(request):
    return HttpRequest('Cart')