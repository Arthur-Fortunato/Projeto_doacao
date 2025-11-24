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
        qtd_str   = request.POST.get('quantidade')

        try:
            quantidade = int(qtd_str)
        except (TypeError, ValueError):
            return redirect('/usuarios/destinatario/?status=error&msg=Quantidade inválida.')

        if quantidade < 1:
            return redirect('/usuarios/destinatario/?status=error&msg=A quantidade mínima é 1.')

        ItemSolicitado.objects.create(
            usuario    = request.user,
            nome_item  = nome_item,     
            categoria  = categoria,      
            quantidade = quantidade
        )

        return redirect('/usuarios/destinatario/?status=success&msg=Item adicionado!')

    itens = ItemSolicitado.objects.filter(usuario=request.user).order_by('-data_solicitacao')
    return render(request, "usuarios/destinatario.html", {"itens": itens})

@login_required(login_url='login')
def editar_item(request, id):
    item = get_object_or_404(ItemSolicitado, id=id, usuario=request.user)

    if request.method == 'POST':
        nome_item = request.POST.get('nome_item')
        categoria = request.POST.get('categoria')
        qtd_str = request.POST.get('quantidade')

        try:
            quantidade = int(qtd_str)
        except (TypeError, ValueError):
            return redirect(f'/usuarios/destinatario/?status=error&msg=Quantidade inválida.')

        if quantidade < 1:
            return redirect(f'/usuarios/destinatario/?status=error&msg=A quantidade mínima é 1.')

        item.nome_item = nome_item
        item.categoria = categoria
        item.quantidade = quantidade
        item.save()

        return redirect('/usuarios/destinatario/?status=info&msg=Item atualizado!')

    return render(request, 'usuarios/editar_item.html', {'item': item})


@login_required(login_url='login')
def excluir_item(request, id):
    item = get_object_or_404(ItemSolicitado, id=id, usuario=request.user)
    item.delete()
    
    return redirect('/usuarios/destinatario/?status=info&msg=Item excluído!')