from my_types import (
    VendedorDTO,
    VendedorLoadedDTO,
    VendedorCadastroDTO,
    CrudInterface
)
from entities import ( Vendedor, Usuario )
from typing import Optional, List

from utils import VendedorMapper
from handlers import VendedorHandler

class __: pass

class VendedorCrud(
        CrudInterface[VendedorCadastroDTO, __, str]):
    
    def create(self, data: VendedorCadastroDTO) -> VendedorDTO:
        usuario = Usuario.objects(pk=data.id_usuario).first()
        return VendedorMapper.toDTO(VendedorHandler.register(usuario, data))
    
    def read(self, id: str) -> Optional[VendedorLoadedDTO]:
        vendedor = Vendedor.objects(pk=id).first()
        if not vendedor:
            return None
        return VendedorMapper.toLoadedDTO(vendedor)
    
    def update(self, id: str, nome_loja: str) -> VendedorDTO:
        vendedor = Vendedor.objects(pk=id).first()
        if not nome_loja.strip():
            raise ValueError("Nome da loja não pode ser vazio.")
        vendedor.nome_loja = nome_loja
        return VendedorMapper.toDTO(vendedor.save())
    
    def delete(self, id: str) -> None:
        vendedor = Vendedor.objects(pk=id).first()
        VendedorHandler.delete(vendedor)

    def list_all(self) -> List[VendedorDTO]:
        vendedores = Vendedor.objects()
        return [VendedorMapper.toDTO(vendedor) for vendedor in vendedores]