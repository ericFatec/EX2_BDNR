from my_types import (
    ProdutoDTO,
    ProdutoLoadedDTO,
    ProdutoCadastroDTO,
    ProdutoAtualizarDTO,
    CrudInterface
)
from entities import ( Produto, Vendedor )
from typing import Optional, List

from utils import ProdutoMapper
from handlers import ProdutoHandler

class ProdutoCrud(
        CrudInterface[ProdutoCadastroDTO, ProdutoAtualizarDTO, str]):
    
    def create(self, data: ProdutoCadastroDTO) -> ProdutoDTO:
        vendedor = Vendedor.objects(pk=data.id_vendedor).first()
        return ProdutoMapper.toDTO(ProdutoHandler.register(vendedor, data))
    
    def read(self, id: str) -> Optional[ProdutoLoadedDTO]:
        produto = Produto.objects(pk=id).first()
        if not produto:
            return None
        return ProdutoMapper.toLoadedDTO(produto)
    
    def update(self, id: str, data: ProdutoAtualizarDTO) -> ProdutoDTO:
        produto = Produto.objects(pk=id).first()
        return ProdutoMapper.toDTO(
            ProdutoHandler.update(produto, data)
        )
    
    def delete(self, id: str) -> None:
        produto = Produto.objects(pk=id).first()
        ProdutoHandler.delete(produto)

    def list_all(self) -> List[ProdutoDTO]:
        produtos = Produto.objects()
        return [ProdutoMapper.toDTO(produto) for produto in produtos]