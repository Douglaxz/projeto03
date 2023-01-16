from django.contrib import admin
from django.urls import path
from galeria.views import index, imagem
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('imagem/',imagem,name='imagem')
]
