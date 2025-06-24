from my_types import ( ProdutoCadastroDTO )
from entities import ( Produto, Vendedor)
from utils import ProdutoMapper


def register(vendedor: Vendedor, data: ProdutoCadastroDTO) -> Produto:
    produto = ProdutoMapper.toEntity(data)
    produto.vendedor = vendedor
    produto.save()

    return produto