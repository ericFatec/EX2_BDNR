from entities import ( Produto )

def delete(produto: Produto) -> None:
    produto.delete()