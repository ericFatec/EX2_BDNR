from my_types import (
    AvaliacaoDTO,
    AvaliacaoCadastroDTO,
    AvaliacaoAtualizarDTO,
    CrudInterface
)
from entities import ( Avaliacao )
from typing import Optional, List

from utils import AvaliacaoMapper
from handlers import AvalHandler

class AvalCrud(
        CrudInterface[AvaliacaoCadastroDTO, AvaliacaoAtualizarDTO, str]):
    
    def create(self, data: AvaliacaoCadastroDTO) -> AvaliacaoDTO:
        return AvaliacaoMapper.toDTO(AvalHandler.register(data))
    
    def read(self, id: str) -> Optional[AvaliacaoDTO]:
        avaliacao = Avaliacao.objects(pk=id).first()
        if not avaliacao:
            return None
        return AvaliacaoMapper.toDTO(avaliacao)
    
    def update(self, id: str, data: AvaliacaoAtualizarDTO) -> AvaliacaoDTO:
        avaliacao = Avaliacao.objects(pk=id).first()
        return AvaliacaoMapper.toDTO(
            AvalHandler.update(avaliacao, data)
        )
    
    def delete(self, id: str) -> None:
        avaliacao = Avaliacao.objects(pk=id).first()
        AvalHandler.delete(avaliacao)

    def list_all(self) -> List[AvaliacaoDTO]:
        avaliacoes = Avaliacao.objects()
        return [AvaliacaoMapper.toDTO(aval) for aval in avaliacoes]