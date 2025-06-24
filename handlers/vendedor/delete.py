from entities import ( Vendedor, Usuario )

def delete(vendedor: Vendedor) -> None:
    usuario = vendedor.usuario
    if usuario:
        usuario.tipos.remove("vendedor")
        usuario.save()
    vendedor.delete()