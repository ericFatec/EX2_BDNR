from my_types import (
    CompraDTO,
    CompraCadastroDTO,
    CompraAtualizarDTO,
    CrudInterface
)
from entities import ( Compra, Usuario )
from typing import Optional, List

from utils import CompraMapper
from handlers import CompraHandler

class CompraCrud(
        CrudInterface[CompraCadastroDTO, CompraAtualizarDTO, str]):
    
    def create(self, data: CompraCadastroDTO) -> CompraDTO:
        usuario = Usuario.objects(pk=data.id_usuario).first()
        return CompraMapper.toDTO(CompraHandler.register(usuario, data))
    
    def read(self, id: str) -> Optional[CompraDTO]:
        compra = Compra.objects(pk=id).first()
        if not compra:
            return None
        return CompraMapper.toDTO(compra)
    
    def update(self, id: str, data: CompraAtualizarDTO) -> CompraDTO:
        compra = Compra.objects(pk=id).first()
        return CompraMapper.toDTO(
            CompraHandler.update(compra, data)
        )
    
    def confirm_payment(self, id: str) -> CompraDTO:
        compra = Compra.objects(pk=id).first()
        return CompraMapper.toDTO(
            CompraHandler.confirm_payment(compra)
        )
    
    def delete(self, id: str) -> None:
        compra = Compra.objects(pk=id).first()
        CompraHandler.delete(compra)

    def list_all(self) -> List[CompraDTO]:
        compras = Compra.objects()
        return [CompraMapper.toDTO(compra) for compra in compras]