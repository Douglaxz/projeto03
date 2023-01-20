from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# controle dos arquivos de rota, puxando de todos os app (galeria e usuário)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)