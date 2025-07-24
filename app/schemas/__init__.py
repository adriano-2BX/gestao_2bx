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
from .fluxo_automacao import FluxoAutomacao, FluxoAutomacaoCreate, FluxoAutomacaoUpdate, FluxoAutomacaoBase
from .instancia_api_whatsapp import InstanciaAPIWhatsApp, InstanciaAPIWhatsAppCreate, InstanciaAPIWhatsAppUpdate, InstanciaAPIWhatsAppBase
from .numero_whatsapp import NumeroWhatsApp, NumeroWhatsAppCreate, NumeroWhatsAppUpdate, NumeroWhatsAppBase
from .timesheet import Timesheet, TimesheetCreate, TimesheetUpdate, TimesheetBase
from .catalogo_servico import CatalogoServico, CatalogoServicoCreate, CatalogoServicoBase
from .assinatura import Assinatura, AssinaturaCreate, AssinaturaBase
from .fatura import Fatura, FaturaBase, ItemFatura, ItemFaturaBase
from .llm_modelo import LLMModelo, LLMModeloCreate, LLMModeloBase
from .llm_preco import LLMPreco, LLMPrecoCreate, LLMPrecoBase
from .llm_custo_uso import LLMCustoUso, LLMCustoUsoCreate, LLMCustoUsoBase
