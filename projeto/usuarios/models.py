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
    
class Doacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    data_doacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.descricao} ({self.quantidade})"

class PedidoItem(models.Model):
    solicitante = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pedidos_realizados")
    doacao = models.ForeignKey(Doacao, on_delete=models.CASCADE, related_name="pedidos_recebidos")
    quantidade = models.PositiveIntegerField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('confirmado', 'Confirmado'),
            ('negado', 'Negado'),
        ],
        default='pendente'
    )

    def __str__(self):
        return f"{self.solicitante.username} → {self.doacao.descricao} ({self.quantidade})"