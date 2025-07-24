# app/schemas/__init__.py
from .cliente import Cliente, ClienteCreate, ClienteUpdate, ClienteBase
from .projeto import Projeto, ProjetoCreate, ProjetoUpdate, ProjetoBase
from .tarefa import Tarefa, TarefaCreate, TarefaUpdate, TarefaBase
from .usuario import Usuario, UsuarioCreate, UsuarioBase
from .token import Token, TokenData
from .servidor import Servidor, ServidorCreate, ServidorUpdate, ServidorBase
from .aplicacao import Aplicacao, AplicacaoCreate, AplicacaoUpdate, AplicacaoBase
from .dominio import Dominio, DominioCreate, DominioUpdate, DominioBase
from .certificado_ssl import CertificadoSSL, CertificadoSSLCreate, CertificadoSSLUpdate, CertificadoSSLBase
from .conexao import Conexao, ConexaoCreate, ConexaoBase
from .permissao import Permissao, PermissaoCreate, PermissaoBase
from .papel import Papel, PapelCreate, PapelUpdate, PapelBase, LinkPermissaoToPapel
from .time import Time, TimeCreate, TimeUpdate, TimeBase, LinkUsuarioToTime
from .credencial import Credencial, CredencialCreate, CredencialUpdate, CredencialRevelada
from .fluxo_automacao import FluxoAutomacao, FluxoAutomacaoCreate, FluxoAutomacaoUpdate, FluxoAutomacaoBase # Adicione esta linha
