from django.db import models
from django.contrib.auth.models import User

class ItemSolicitado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_item = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, choices=[
        ('alimento', 'Alimento'),
        ('higiene', 'Higiene'),
        ('roupa', 'Roupa'),
        ('outros', 'Outros'),
    ])
    quantidade = models.PositiveIntegerField(default=1)
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_item} ({self.usuario.username})"