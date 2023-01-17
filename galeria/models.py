from django.db import models

from datetime import datetime

# Create your models here.

# construção da tabela em sql lite
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALÁXIA","Galáxia"),
        ("PLANETA","Planeta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank="False")
    legenda = models.CharField(max_length=150, null=False, blank="False")
    descricao = models.TextField(max_length=300, null=False, blank="False")   
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) 
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome