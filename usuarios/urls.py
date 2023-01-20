from django.urls import path
from usuarios.views import login, cadastro, logout, usuarios

#arquivos de rotas do app usuário
urlpatterns = [
    path('login', login,  name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout,  name='logout'),
    path('usuarios', usuarios,  name='usuarios'),
]
