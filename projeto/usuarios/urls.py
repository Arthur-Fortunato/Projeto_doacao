from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('doador/', views.load_pagina_doador, name="doador"),
    path('destinatario/', views.load_pagina_destinatario, name="receptor"),
    path('destinatario/editar/<int:id>/', views.editar_item, name='editar_item'),
    path('destinatario/excluir/<int:id>/', views.excluir_item, name='excluir_item'),
    path('itens-disponiveis/', views.itens_disponiveis, name='itens_disponiveis'),
    path('solicitar/<int:id>/', views.solicitar_item, name='solicitar_item'),
    path('doador/excluir/<int:id>/', views.excluir_doacao, name='excluir_doacao'),
    path('doador/editar/<int:id>/', views.editar_doacao, name='editar_doacao'),
    path('solicitacoes/', views.solicitacoes_recebidas, name='solicitacoes'),
    path('solicitacoes/confirmar/<int:id>/', views.confirmar_pedido, name='confirmar_pedido'),
    path('solicitacoes/negar/<int:id>/', views.negar_pedido, name='negar_pedido')
]