from projeto.models import Endereco
from abc import ABC, abstractmethod


class Funcionario(ABC):

    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco):
        self.nome = nome
        self.telefone - telefone
        self.email = email
        self.salario = salario
        self.endereco = endereco

    @abstractmethod
    def salarioFinal() -> float:
        pass   



    def _verificar_salario(self, salario):
        if not isinstance(salario, float):
            raise TypeError("Salario deve ser número.")
        return salario
   
    def _verificar_nome(self, nome):
        if not isinstance(nome, str) or not nome.strip():
            raise TypeError("O nome não pode estar vazio.")
        return nome
    
    def _verificar_telefone(self, telefone):
        if not  isinstance(telefone, str):
            raise TypeError("Telefone deve ser apenas números.")
        return telefone
    
    def _verificar_email(self, email):
        if not isinstance(email, str):
            raise TypeError("E-mail não deve estar vázio.")
        return email
    


    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nEndereço: {self.endereco}"
        )     