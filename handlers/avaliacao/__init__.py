from . import (
    register,
    update,
    delete
)

class AvalHandler:
    @staticmethod
    def register(*args, **kwargs):
        return register.register(*args, **kwargs)
    
    @staticmethod
    def update(*args, **kwargs):
        return update.update(*args, **kwargs)
    
    @staticmethod
    def delete(*args, **kwargs):
        return delete.delete(*args, **kwargs)