from django.shortcuts import render

def load_pagina_doador(request):
    return render(request, "usuarios/doadores.html")

def load_pagina_destinatario(request):
    return render(request, "usuarios/destinatario.html")