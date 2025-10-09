from django.urls import path
from . import views

urlpatterns = [
    path('doador/', views.load_pagina_doador, name="doador"),
    path('destinatario/', views.load_pagina_destinatario, name="destinatario")
]