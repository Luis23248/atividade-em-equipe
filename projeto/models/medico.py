from projeto.models import Endereco
from projeto.abstract import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = crm

    def salarioFinal() -> float:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (f"CRM: {self.crm}")