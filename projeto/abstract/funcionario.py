from projeto.endereco import Endereco
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone - telefone
        self.email = email
        self.endereco = endereco
        