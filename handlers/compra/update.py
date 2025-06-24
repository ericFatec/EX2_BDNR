from my_types import ( CompraAtualizarDTO )
from entities import ( Compra )
from utils import CompraMapper

def update(compra: Compra, data: CompraAtualizarDTO) -> Compra:
    if compra.pagamento_confirmado:
        raise ValueError("A compra já foi paga e não pode ser alterada.")
    
    CompraMapper.updateCompra(compra, data)

    return compra.save()