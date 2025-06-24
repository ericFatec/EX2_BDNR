from mongoengine import (
    Document,
    StringField,
    DecimalField,
    ListField,
    EmbeddedDocumentListField,
    ReferenceField
)

# from .usuario import Usuario
# from .avaliacao import Avaliacao
from .venda import Venda

class Vendedor(Document):
    usuario = ReferenceField('Usuario', required=True)
    nome_loja = StringField(required=True)
    produtos = ListField(ReferenceField('Produto'))
    total_avaliacao = DecimalField(precision=1, min_value=0, max_value=5)
    avaliacoes = ListField(ReferenceField('Avaliacao'))
    vendas = EmbeddedDocumentListField(Venda)

    meta = {
        "collection": "vendedores"
    }