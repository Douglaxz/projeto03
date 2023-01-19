from django.urls import path
from galeria.views import index, imagem, buscar, anuncio, visualizar_anuncio,alterar_anuncio

urlpatterns = [
    path('',index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name="buscar"),
    path('anuncio', anuncio, name="anuncio"),
    path('visualizar_anuncio/<int:foto_id>', visualizar_anuncio, name="visualizar_anuncio"),
    path('alterar_anuncio/<int:foto_id>', alterar_anuncio, name="alterar_anuncio"),
]