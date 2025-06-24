from mongoengine import (
    Document,
    StringField,
    DecimalField,
    IntField,
    ListField,
    ReferenceField
)

# from .vendedor import Vendedor
# from .avaliacao import Avaliacao

class Produto(Document):
    vendedor = ReferenceField('Vendedor', required=True)
    nome = StringField(required=True)
    descricao = StringField()
    preco = DecimalField(required=True, precision=2, min_value=0.01)
    estoque = IntField(required=True, min_value=0)
    total_avaliacao = DecimalField(precision=1, min_value=0, max_value=5)
    avaliacoes = ListField(ReferenceField('Avaliacao'))

    meta = {
        "collection": "produtos"
    }