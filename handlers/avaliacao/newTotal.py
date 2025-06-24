from decimal import Decimal

def nova_nota(quantidade: int, current_avg: Decimal, nova_nota: int) -> Decimal:
    new_avg = (current_avg * Decimal(quantidade - 1) + Decimal(nova_nota)) / Decimal(quantidade)
    return new_avg

def nota_editada(quantidade: int, current_avg: Decimal, nova_nota: int, nota_anterior: int) -> Decimal:
    diff = Decimal(nova_nota) - Decimal(nota_anterior)
    new_avg = current_avg + diff / Decimal(quantidade)
    return new_avg