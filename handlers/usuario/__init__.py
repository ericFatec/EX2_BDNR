from . import (
    register,
    update,
    delete,
    favoritar
)

class UsuarioHandler:
    @staticmethod
    def register(*args, **kwargs):
        return register.register(*args, **kwargs)
    
    @staticmethod
    def update(*args, **kwargs):
        return update.update(*args, **kwargs)
    
    @staticmethod
    def delete(*args, **kwargs):
        return delete.delete(*args, **kwargs)
    
    @staticmethod
    def favoritar(*args, **kwargs):
        return favoritar.favoritar(*args, **kwargs)