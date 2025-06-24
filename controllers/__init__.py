from .userControllers import router as user_router
from .vendedorControllers import router as vendedor_router
from .produtoControllers import router as produto_router
from .compraControllers import router as compra_router
from .avaliacaoControllers import router as avaliacao_router

__all__ = [
    "user_router",
    "vendedor_router",
    "produto_router",
    "compra_router",
    "avaliacao_router"
]