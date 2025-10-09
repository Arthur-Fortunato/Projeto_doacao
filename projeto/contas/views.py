from django.shortcuts import render

def load_pagina_login(request):
    return render(request, "contas/login.html")

def load_pagina_cadastro(request):
    return render(request, "contas/cadastro.html")