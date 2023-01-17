from django.db import models

# Create your models here.

# construção da tabela em sql lite
class Fotografia(models.Model):
    nome = models.CharField(max_length=100,null=False, blank="False")
    legenda = models.CharField(max_length=150,null=False, blank="False")
    descricao = models.TextField(max_length=300,null=False, blank="False")
    foto = models.CharField(max_length=100,null=False, blank="False")

    def __str__(self) -> str:
        return f"Fotografia [nome={self.nome}]"