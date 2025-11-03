from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path('doador/', views.load_pagina_doador, name="doador"),
    path('destinatario/', views.load_pagina_destinatario, name="receptor"),
    path('destinatario/editar/<int:id>/', views.editar_item, name='editar_item'),
    path('destinatario/excluir/<int:id>/', views.excluir_item, name='excluir_item')
]