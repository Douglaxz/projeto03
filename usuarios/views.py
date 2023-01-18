from django.shortcuts import render, redirect
from usuarios.forms import LoginsForms,CadastroForms
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib  import messages

def login(request):
    form = LoginsForms()
    if request.method == 'POST':
        form = LoginsForms(request.POST)
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha,
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"{nome} Logado com sucesso!")
                return redirect('index')
            else:
                messages.error(request, "Erro ao efetuar login!")
                return redirect('login')

    return render(request,"usuarios/login.html",{"form":form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            nome = form["nome_cadastro"].value()
            email = form["email_cadastro"].value()
            senha = form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existe !")
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save
            messages.success(request, f"Usuário {nome} criado com sucesso!")
            return redirect('login')
    return render(request,"usuarios/cadastro.html",{"form":form})
    



def logout(request):
    auth.logout(request)            
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect('login')
    




    return render(request,"usuarios/cadastro.html",{"form":form})
