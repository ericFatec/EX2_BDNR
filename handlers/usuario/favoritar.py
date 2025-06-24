from entities import Usuario, Produto

def favoritar(usuario: Usuario, id_produto: str) -> None:
    produto = Produto.objects(pk=id_produto).first()
    usuario.favoritos.append(produto)
    usuario.save()