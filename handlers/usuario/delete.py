from entities import ( Usuario )

from .syncName import sync_name

def delete(usuario: Usuario) -> None:
    
    sync_name(usuario.pk, "Usuário Deletado")
    
    usuario.delete()