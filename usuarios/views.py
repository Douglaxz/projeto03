from django.shortcuts import render
from usuarios.forms import LoginsForms

def login(request):
    form = LoginsForms
    return render(request,"usuarios/login.html",{"form":form})

def cadastro(request):
    return render(request,"usuarios/cadastro.html")
