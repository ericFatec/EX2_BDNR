from my_types import (
    UsuarioDTO,
    UsuarioLoadedDTO,
    UsuarioCadastroDTO,
    UsuarioAtualizarDTO,
    CrudInterface
)
from entities import ( Usuario )
from typing import Optional, List

from utils import UsuarioMapper
from handlers import UsuarioHandler

class UsuarioCrud(
        CrudInterface[UsuarioCadastroDTO, UsuarioAtualizarDTO, str]):

    def create(self, data: UsuarioCadastroDTO) -> UsuarioDTO:
        return UsuarioMapper.toDTO(UsuarioHandler.register(data))
    
    def read(self, id: str) -> Optional[UsuarioLoadedDTO]:
        usuario = Usuario.objects(pk=id).first()
        if not usuario:
            return None
        return UsuarioMapper.toLoadedDTO(usuario)
    
    def update(self, id: str, data: UsuarioAtualizarDTO) -> UsuarioDTO:
        usuario = Usuario.objects(pk=id).first()
        return UsuarioMapper.toDTO(
            UsuarioHandler.update(usuario, data)
        )
    
    def favoritar(self, id: str, id_produto: str) -> None:
        usuario = Usuario.objects(pk=id).first()
        UsuarioHandler.favoritar(usuario, id_produto)
    
    def delete(self, id: str) -> None:
        usuario = Usuario.objects(pk=id).first()
        UsuarioHandler.delete(usuario)

    def list_all(self) -> List[UsuarioDTO]:
        usuarios = Usuario.objects()
        return [UsuarioMapper.toDTO(usuario) for usuario in usuarios]