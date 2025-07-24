from .cliente import Cliente, ClienteCreate, ClienteUpdate, ClienteBase
from .projeto import Projeto, ProjetoCreate, ProjetoUpdate, ProjetoBase
from .tarefa import Tarefa, TarefaCreate, TarefaUpdate, TarefaBase
from .usuario import Usuario, UsuarioCreate, UsuarioBase
from .token import Token, TokenData
from .servidor import Servidor, ServidorCreate, ServidorUpdate, ServidorBase
from .aplicacao import Aplicacao, AplicacaoCreate, AplicacaoUpdate, AplicacaoBase
from .dominio import Dominio, DominioCreate, DominioUpdate, DominioBase
from .certificado_ssl import CertificadoSSL, CertificadoSSLCreate, CertificadoSSLUpdate, CertificadoSSLBase # Adicione esta linha
from .conexao import Conexao, ConexaoCreate, ConexaoBase # Adicione esta linha
from .permissao import Permissao, PermissaoCreate, PermissaoBase # Adicione esta linha
from .papel import Papel, PapelCreate, PapelUpdate, PapelBase, LinkPermissaoToPapel # Adicione esta linha
from .time import Time, TimeCreate, TimeUpdate, TimeBase, LinkUsuarioToTime # Adicione esta linha
