from mongoengine import (
    Document,
    StringField,
    ListField,
    EmbeddedDocumentField,
    ReferenceField
)

from my_types import TipoUsuario
from .endereco import Endereco
# from .produto import Produto
# from .compra import Compra
# from .avaliacao import Avaliacao

class Usuario(Document):
    nome = StringField(required=True)
    email = StringField(required=True)
    senha = StringField(required=True)
    endereco = EmbeddedDocumentField(Endereco, required=True)
    tipos = ListField(StringField(choices=[t.value for t in TipoUsuario]), required=True)
    favoritos = ListField(ReferenceField('Produto'))
    compras = ListField(ReferenceField('Compra'))
    avaliacoes = ListField(ReferenceField('Avaliacao'))

    meta = {
        "collection": "usuarios"
    }