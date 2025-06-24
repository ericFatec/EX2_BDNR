from . import (
    register,
    delete
)

class VendedorHandler:
    @staticmethod
    def register(*args, **kwargs):
        return register.register(*args, **kwargs)
    
    @staticmethod
    def delete(*args, **kwargs):
        return delete.delete(*args, **kwargs)