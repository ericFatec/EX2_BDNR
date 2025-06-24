from entities import ( Avaliacao, Usuario, Produto, Vendedor )

def delete(avaliacao: Avaliacao) -> None:
    avaliacao.delete()