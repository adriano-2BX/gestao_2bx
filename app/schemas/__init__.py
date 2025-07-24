# app/schemas/__init__.py
from .cliente import Cliente, ClienteCreate, ClienteUpdate, ClienteBase
from .projeto import Projeto, ProjetoCreate, ProjetoUpdate, ProjetoBase
from .tarefa import Tarefa, TarefaCreate, TarefaUpdate, TarefaBase
from .usuario import Usuario, UsuarioCreate, UsuarioBase
from .token import Token, TokenData # Adicione esta linha
