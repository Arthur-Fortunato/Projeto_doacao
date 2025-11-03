from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from .models import Perfil

def cadastro_view(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("senha")
        status = request.POST.get("opcao")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Esse login já está em uso.")
            return render(request, "contas/cadastro.html")

        user = User.objects.create_user(username=username, password=password)
        Perfil.objects.create(user=user, status=status)

        login(request, user)
        messages.success(request, "Cadastro realizado com sucesso!")

        if status == "doador":
            return redirect("usuarios:doador")
        elif status == "receptor":
            return redirect("usuarios:receptor")
        return redirect("home")

    return render(request, "contas/cadastro.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("senha")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            try:
                perfil = Perfil.objects.get(user=user)
                if perfil.status == "doador":
                    return redirect("usuarios:doador")
                elif perfil.status == "receptor":
                    return redirect("usuarios:receptor")
            except Perfil.DoesNotExist:
                messages.warning(request, "Seu perfil não foi encontrado.")
                return redirect("home")
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return render(request, "contas/login.html")

    return render(request, "contas/login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def redefinir_senha(request):
    if request.method == "POST":
        username = request.POST.get("login")
        password = request.POST.get("senha")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  
        else:
            messages.error(request, "Usuário ou senha incorretos.")
            return render(request, "contas/login.html")

    return render(request, "contas/redefinicao.html")