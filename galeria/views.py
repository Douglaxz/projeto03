from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from galeria.models import Fotografia
from django.contrib import messages
from django.contrib.auth.models import auth
from galeria.forms import CadastroForms


def index(request):
    #if not request.user.is_authenticated:
    #    messages.error(request, "Usuário não logado")
    #    return redirect('login')
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request,'galeria/index.html',{"cards":fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request,'galeria/imagem.html',{"fotografia":fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request,'galeria/buscar.html',{"cards":fotografias})

def anuncio(request):
    usuario_id = request.user.id
    anuncios = Fotografia.objects.order_by("-data_fotografia").filter(usuario_id=usuario_id)
    return render(request,'galeria/anuncio.html',{"anuncios":anuncios})

def visualizar_anuncio(request, foto_id):
    anuncio = Fotografia.objects.order_by("-data_fotografia").filter(id=foto_id).first()    
    return render(request,'galeria/visualizar_anuncio.html',{"anuncio":anuncio})

def alterar_anuncio(request,foto_id):
    anuncio = Fotografia.objects.order_by("-data_fotografia").filter(id=foto_id).first()    

    if "nome" in request.GET:
        anuncio.nome = request.GET["nome"]
    if "legenda" in request.GET:
        anuncio.legenda = request.GET["legenda"]        
    if "descricao" in request.GET:
        anuncio.descricao = request.GET["descricao"] 
    if "categoria" in request.GET:
        anuncio.categoria = request.GET["categoria"]               
    if "preco" in request.GET:
        anuncio.preco = request.GET["preco"]                       
    if "publicada" in request.GET:
        anuncio.publicada = request.GET["publicada"]
    if "usuario_id" in request.GET:
        anuncio.usuario_id = request.GET["usuario_id"]                     
    anuncio.save()
    

    return redirect('visualizar_anuncio',foto_id)
    
