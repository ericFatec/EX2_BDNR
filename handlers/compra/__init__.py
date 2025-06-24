from . import (
    register,
    update,
    delete,
    confirmPayment
)

class CompraHandler:
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
    def confirm_payment(*args, **kwargs):
        return confirmPayment.confirm_payment(*args, **kwargs)