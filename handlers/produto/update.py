from my_types import ( ProdutoAtualizarDTO )
from entities import ( Produto )
from utils import ProdutoMapper

def update(produto: Produto, data: ProdutoAtualizarDTO) -> Produto:
    ProdutoMapper.updateProduto(produto, data)
    
    return produto.save()