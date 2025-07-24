# app/models/__init__.py
from .cliente import Cliente
from .projeto import Projeto
from .tarefa import Tarefa
from .usuario import Usuario
from .papel import Papel, Permissao
from .servidor import Servidor
from .aplicacao import Aplicacao
from .dominio import Dominio
from .certificado_ssl import CertificadoSSL
from .conexao import Conexao
from .time import Time
from .credencial import Credencial
from .fluxo_automacao import FluxoAutomacao
from .instancia_api_whatsapp import InstanciaAPIWhatsApp
from .numero_whatsapp import NumeroWhatsApp # Adicione esta linha
