from my_types import ( UsuarioCadastroDTO, UsuarioDTO, UsuarioLoadedDTO, UsuarioAtualizarDTO, EnderecoDTO )
from entities import ( Usuario, Endereco, Vendedor )

from .vendedorMapper import VendedorMapper
from .produtoMapper import ProdutoMapper
from .avaliacaoMapper import AvaliacaoMapper
from .compraMapper import CompraMapper

class UsuarioMapper:
    @staticmethod
    def toEntity(data: UsuarioCadastroDTO) -> Usuario:
        tipos = list({tipo.value for tipo in data.tipos})
        endereco = UsuarioMapper._clean_endereco(Endereco(**data.endereco.model_dump()))

        usuario = Usuario(
            nome = data.nome.strip() if data.nome and data.nome.strip() else None,
            email = data.email.strip() if data.email and data.email.strip() else None,
            senha = data.senha.strip() if data.senha and data.senha.strip() else None,
            endereco = endereco,
            tipos = tipos,
            favoritos = [],
            compras = [],
            avaliacoes = []
        )

        return usuario
    
    @staticmethod
    def toDTO(usuario: Usuario) -> UsuarioDTO:
        vendedor = Vendedor.objects(usuario=usuario).first()

        usuarioDTO = UsuarioDTO(
            _id = str(usuario.pk),
            nome = usuario.nome,
            email = usuario.email,
            endereco = EnderecoDTO(**usuario.endereco.to_mongo().to_dict()),
            tipos = usuario.tipos,
            compras = len(usuario.compras),
            avaliacoes = len(usuario.avaliacoes),
            perfil_vendedor = VendedorMapper.toPerfil(vendedor)
        )

        return usuarioDTO
    
    @staticmethod
    def toLoadedDTO(usuario: Usuario) -> UsuarioLoadedDTO:
        vendedor = Vendedor.objects(usuario=usuario).first()

        favoritos = usuario.favoritos or []
        favoritos_dto = [ProdutoMapper.toFavorite(prod) for prod in favoritos]

        compras = usuario.compras or []
        compras_dto = [CompraMapper.toDTO(c) for c in compras]

        avaliacoes = usuario.avaliacoes or []
        avaliacoes_user = [AvaliacaoMapper.toAvalUser(a) for a in avaliacoes]

        usuarioLoaded = UsuarioLoadedDTO(
            _id = str(usuario.pk),
            nome = usuario.nome,
            email = usuario.email,
            senha = usuario.senha,
            endereco = EnderecoDTO(**usuario.endereco.to_mongo().to_dict()),
            tipos = usuario.tipos,
            favoritos = favoritos_dto,
            compras = compras_dto,
            avaliacoes = avaliacoes_user,
            perfil_vendedor = VendedorMapper.toPerfil(vendedor)
        )

        return usuarioLoaded
    
    @staticmethod
    def updateUser(usuario: Usuario, data: UsuarioAtualizarDTO) -> Usuario:
        if data.nome and data.nome.strip():
            usuario.nome = data.nome.strip()
        if data.email and data.email.strip():
            usuario.email = data.email.strip()
        if data.senha and data.senha.strip():
            usuario.senha = usuario.senha.strip()
        if data.endereco:
            if data.endereco.cep and data.endereco.cep.strip():
                usuario.endereco.cep = data.endereco.cep.strip()
            if data.endereco.numero and data.endereco.numero.strip():
                usuario.endereco.numero = data.endereco.numero.strip()

        return usuario
    
    @staticmethod
    def _clean_endereco(endereco: Endereco) -> Endereco:
        endereco.cep = endereco.cep.strip() if endereco.cep else ""
        endereco.numero = endereco.numero.strip() if endereco.numero else ""

        if not endereco.cep:
            raise ValueError("CEP no endereço não pode ser vazio.")
        if not endereco.numero:
            raise ValueError("Número no endereço não pode ser vazio.")

        return endereco