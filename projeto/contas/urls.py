from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.load_pagina_login, name="login"),
    path('cadastro/', views.load_pagina_cadastro, name="cadastro")
]