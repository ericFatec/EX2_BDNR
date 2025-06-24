from mongoengine import ( CASCADE, PULL, NULLIFY )

from .endereco import Endereco
from .usuario import Usuario
from .vendedor import Vendedor
from .avaliacao import Avaliacao
from .compra import Compra
from .produto import Produto
from .produtoCompra import ProdutoCompra
from .venda import Venda

__all__ = [
    "Usuario",
    "Vendedor",
    "Endereco",
    "Avaliacao",
    "Compra",
    "Produto",
    "ProdutoCompra",
    "Venda"
]

Usuario.register_delete_rule(Vendedor, 'usuario', CASCADE)
Avaliacao.register_delete_rule(Vendedor, 'avaliacoes', PULL)
Produto.register_delete_rule(Vendedor, 'produtos', PULL)

Produto.register_delete_rule(Usuario, 'favoritos', PULL)
Compra.register_delete_rule(Usuario, 'compras', PULL)
Avaliacao.register_delete_rule(Usuario, 'avaliacoes', PULL)

Vendedor.register_delete_rule(Produto, 'vendedor', CASCADE)
Avaliacao.register_delete_rule(Produto, 'avaliacoes', PULL)

Usuario.register_delete_rule(Compra, 'usuario', CASCADE)

Usuario.register_delete_rule(Avaliacao, 'usuario', NULLIFY)
Produto.register_delete_rule(Avaliacao, 'produto', CASCADE)