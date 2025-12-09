from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ItemSolicitado, Doacao, PedidoItem
from django.contrib import messages

@login_required(login_url='login')
def load_pagina_doador(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        descricao = request.POST.get('descricao')
        quantidade = request.POST.get('quantidade')
        if not tipo or not descricao or not quantidade:
            return redirect('/usuarios/doador/?status=error&msg=Preencha todos os campos.')
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                return redirect('/usuarios/doador/?status=error&msg=Quantidade inválida.')
        except:
            return redirect('/usuarios/doador/?status=error&msg=Quantidade inválida.')

        Doacao.objects.create(
            usuario=request.user,
            tipo=tipo,
            descricao=descricao,
            quantidade=quantidade
        )
        return redirect('/usuarios/doador/?status=success&msg=Doação cadastrada!')

    doacoes = Doacao.objects.filter(usuario=request.user).order_by('-data_doacao')
    pedidos = PedidoItem.objects.filter(
        doacao__usuario=request.user
    ).order_by('-data_pedido')

    return render(request, "usuarios/doadores.html", {
        "doacoes": doacoes,
        "pedidos": pedidos 
    })


@login_required(login_url='login')
def excluir_doacao(request, id):
    doacao = get_object_or_404(Doacao, id=id, usuario=request.user)
    doacao.delete()
    return redirect('/usuarios/doador/?status=error&msg=Doação excluída!')

@login_required(login_url='login')
def editar_doacao(request, id):
    doacao = get_object_or_404(Doacao, id=id, usuario=request.user)
    if request.method == "POST":
        tipo = request.POST.get("tipo")
        descricao = request.POST.get("descricao")
        quantidade = request.POST.get("quantidade")
        if not tipo or not descricao or not quantidade:
            return redirect(f'/usuarios/doador/?status=error&msg=Preencha todos os campos.')
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except:
            return redirect(f'/usuarios/doador/?status=error&msg=Quantidade inválida.')

        doacao.tipo = tipo
        doacao.descricao = descricao
        doacao.quantidade = quantidade
        doacao.save()
        return redirect('/usuarios/doador/?status=info&msg=Doação atualizada!')

    return redirect('/usuarios/doador')

@login_required(login_url='login')
def solicitacoes_recebidas(request):
    pedidos = PedidoItem.objects.filter(
        doacao__usuario=request.user
    ).order_by('-data_pedido')

    return render(request, "usuarios/solicitacoes_recebidas.html", {
        "pedidos": pedidos
    })

@login_required(login_url='login')
def confirmar_pedido(request, id):
    pedido = get_object_or_404(PedidoItem, id=id, doacao__usuario=request.user)
    pedido.status = "confirmado"
    pedido.save()

    return redirect("/usuarios/solicitacoes/?status=success&msg=Solicitação confirmada!")


@login_required(login_url='login')
def negar_pedido(request, id):
    pedido = get_object_or_404(PedidoItem, id=id, doacao__usuario=request.user)
    pedido.status = "negado"
    pedido.save()

    return redirect("/usuarios/solicitacoes/?status=error&msg=Solicitação negada!")


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
    
    return redirect('/usuarios/destinatario/?status=error&msg=Item excluído!')

@login_required(login_url='login')
def itens_disponiveis(request):
    itens = Doacao.objects.exclude(usuario=request.user).order_by('-data_doacao')
    return render(request, "usuarios/itens_disponiveis.html", {"itens": itens})

@login_required(login_url='login')
def solicitar_item(request, id):
    item = get_object_or_404(Doacao, id=id)
    if request.method == "POST":
        qtd = request.POST.get("quantidade")
        try:
            qtd = int(qtd)
            if qtd <= 0:
                raise ValueError
        except:
            return redirect(f"/usuarios/itens-disponiveis/?status=error&msg=Quantidade inválida")

        PedidoItem.objects.create(
            solicitante = request.user,
            doacao = item,
            quantidade = qtd
        )
        return redirect("/usuarios/itens-disponiveis/?status=success&msg=Pedido enviado!")

    return redirect("/usuarios/itens-disponiveis")
