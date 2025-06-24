from entities import ( Compra )

def delete(compra: Compra) -> None:
    compra.delete()