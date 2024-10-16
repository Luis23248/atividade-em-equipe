from projeto.models.endereco import Endereco
from projeto.abstract.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, salario: float, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = crea

    def salarioFinal() -> float:
        pass

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (f"CREA: {self.crea}")