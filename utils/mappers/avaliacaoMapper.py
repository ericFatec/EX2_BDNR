from my_types import ( AvaliacaoUsuario, AvaliacaoDTO, AvaliacaoCadastroDTO, AvaliacaoAtualizarDTO )
from entities import ( Avaliacao, Produto, Usuario )
from datetime import datetime

class AvaliacaoMapper:
    @staticmethod
    def toEntity(usuario: Usuario, produto: Produto, novaAvaliacao: AvaliacaoCadastroDTO) -> Avaliacao:
        avaliacao = Avaliacao(
            usuario = usuario,
            produto = produto,
            nota = novaAvaliacao.nota,
            mensagem = novaAvaliacao.mensagem.strip() if novaAvaliacao.mensagem and novaAvaliacao.mensagem.strip() else None,
            data_avaliacao = datetime.now()
        )

        return avaliacao

    @staticmethod
    def toDTO(avaliacao: Avaliacao) -> AvaliacaoDTO:
        avaliacaoVendedor = AvaliacaoDTO(
            _id = str(avaliacao.pk),
            nome_usuario = avaliacao.usuario.nome if avaliacao.usuario else "Usuário Deletado",
            nome_produto = avaliacao.produto.nome,
            nota = avaliacao.nota,
            mensagem = avaliacao.mensagem,
            data_avaliacao = avaliacao.data_avaliacao
        )

        return avaliacaoVendedor
    
    @staticmethod
    def updateAvaliacao(avaliacao: Avaliacao, data: AvaliacaoAtualizarDTO) -> Avaliacao:
        if data.nota is not None:
            avaliacao.nota = data.nota
        
        if data.mensagem and data.mensagem.strip():
            avaliacao.mensagem = data.mensagem.strip()
        
        return avaliacao

    @staticmethod
    def toAvalUser(avaliacao: Avaliacao) -> AvaliacaoUsuario:
        avaliacaoUsuario = AvaliacaoUsuario(
            _id = str(avaliacao.pk),
            nome_produto = avaliacao.produto.nome,
            nota = avaliacao.nota,
            mensagem = avaliacao.mensagem,
            data_avaliacao = avaliacao.data_avaliacao
        )

        return avaliacaoUsuario