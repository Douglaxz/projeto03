from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

# construção da tabela em sql lite
class Fotografia(models.Model):

    # campo do select com essas opções
    OPCOES_CATEGORIA = [
        ("MÓVEIS","Moveis"),
        ("CELULARES","Celulares"),
        ("INFORMÁTICA","Informática"),
        ("CASA","CASA"),
    ]

    nome = models.CharField(max_length=100, null=False, blank="False")
    legenda = models.CharField(max_length=150, null=False, blank="False")
    descricao = models.TextField(max_length=300, null=False, blank="False")   
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True) 
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateField(default=datetime.now, blank=False)
    preco = models.IntegerField(null=False, blank="False",default=0)
    # vinculação com a tabela usuários
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.nome

    