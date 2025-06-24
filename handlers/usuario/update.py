from my_types import ( UsuarioAtualizarDTO )
from entities import ( Usuario )
from utils import UsuarioMapper

from .syncName import (sync_name)

def update(usuario: Usuario, data: UsuarioAtualizarDTO) -> Usuario:
    UsuarioMapper.updateUser(usuario, data)

    if data.nome.strip():
        sync_name(id, data.nome.strip())
    
    return usuario.save()