

class Endereco:

    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade

    def _verificar_logradouro(self, logradouro):
                if not isinstance(logradouro, str) or not logradouro.strip():
                    raise ValueError("Logradouro não pode estar vazio")
                return logradouro

    def _verificar_numero(self, numero):
                    if not isinstance(numero, str) or not numero.strip():
                        raise ValueError("Número não pode estar vazio")
                    return numero
    
    def _verificar_complemento(self, complemento):
                if not isinstance(complemento, str) or not complemento.strip():
                    raise ValueError("Complemento não pode estar vazio")
                return complemento

    def _verificar_cep(self, cep):
                if not isinstance(cep, str) or not cep.strip():
                    raise ValueError("CEP não pode estar vazio")
                return cep
    
    def _verificar_cidade(self, cidade):
                if not isinstance(cidade, str) or not cidade.strip():
                    raise ValueError("Cidade não pode estar vazio")
                return cidade



    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCEP: {self.cep}"
            f"\nCidade: {self.cidade}"
        )   