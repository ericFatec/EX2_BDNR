from my_types import ( UsuarioCadastroDTO, VendedorCadastroDTO, TipoUsuario )
from entities import ( Usuario )
from utils import UsuarioMapper

from ..vendedor import VendedorHandler

def register(data: UsuarioCadastroDTO) -> Usuario:
    usuario = UsuarioMapper.toEntity(data)
    usuario.save()
    
    if TipoUsuario.VENDEDOR.value in data.tipos:
        vendedorCadastro = VendedorCadastroDTO(
            id_usuario = "",
            nome_loja = data.nome_loja.strip() 
                            if data.nome_loja and data.nome_loja.strip() 
                                else f'Loja de {usuario.nome}'
        )   

        VendedorHandler.register(usuario, vendedorCadastro)
    
    return usuario