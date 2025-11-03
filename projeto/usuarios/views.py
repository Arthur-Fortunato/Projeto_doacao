from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ItemSolicitado
from django.contrib import messages

@login_required(login_url='login')
def load_pagina_doador(request):
    return render(request, "usuarios/doadores.html")

@login_required(login_url='login')
def load_pagina_destinatario(request):
    if request.method == 'POST':
        nome_item = request.POST.get('nome_item')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')

        if nome_item and categoria and quantidade:
            ItemSolicitado.objects.create(
                usuario     = request.user,
                nome_item   = nome_item,
                categoria   = categoria,
                quantidade  = int(quantidade)
            )
            messages.success(request, "Item solicitado com sucesso!")
            return redirect('usuarios:receptor')

    itens = ItemSolicitado.objects.filter(usuario=request.user).order_by('-data_solicitacao')
    return render(request, "usuarios/destinatario.html", {"itens": itens})

@login_required(login_url='login')
def editar_item(request, id):
    item = get_object_or_404(ItemSolicitado, id=id, usuario=request.user)

    if request.method == 'POST':
        item.nome_item = request.POST.get('nome_item')
        item.categoria = request.POST.get('categoria')
        item.quantidade = request.POST.get('quantidade')
        item.save()
        messages.success(request, "Item atualizado com sucesso!")
        return redirect('usuarios:receptor')

    return render(request, 'usuarios/editar_item.html', {'item': item})


@login_required(login_url='login')
def excluir_item(request, id):
    item = get_object_or_404(ItemSolicitado, id=id, usuario=request.user)
    item.delete()
    messages.success(request, "Item excluído com sucesso!")
    return redirect('usuarios:receptor')