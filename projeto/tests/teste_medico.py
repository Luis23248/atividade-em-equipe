import pytest
from projeto.models.endereco import Endereco
from projeto.models.medico import Medico

@pytest.fixture
def pessoa_valida():
    medico = Medico("Nome", "Telefone", "Email", "CRM", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", "cidade"))
    return medico

def test_validar_nome(pessoa_valida):
    assert pessoa_valida.nome == "Nome"

def test_validar_telefone(pessoa_valida):
    assert pessoa_valida.telefone == "Telefone"

def test_validar_email(pessoa_valida):
    assert pessoa_valida.email == "Email"

def test_validar_CRM(pessoa_valida):
    assert pessoa_valida.CRM == "CRM"

def test_validar_salario(pessoa_valida):
    assert pessoa_valida.salario == 100

def test_validar_logradouro(pessoa_valida):
    assert pessoa_valida.endereco.logradouro == "logradouro"

def test_validar_numero(pessoa_valida):
    assert pessoa_valida.endereco.numero == "numero"

def test_validar_complemento(pessoa_valida):
    assert pessoa_valida.endereco.complemento == "complemento"

def test_validar_cep(pessoa_valida):
    assert pessoa_valida.endereco.cep == "cep"

def test_validar_cidade(pessoa_valida):
    assert pessoa_valida.endereco.cidade == "cidade"


def test_nome_vazio(pessoa_valida):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
       Medico("", "Telefone", "Email", "CRM", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", "cidade"))

def test_telefone_invalido(pessoa_valida):
   with pytest.raises(ValueError, match= "Digite apenas números."):
       Medico("Nome", 147845, "email", "CRM", 100,
                            Endereco("logradoouro", "numero", "complemento", "cep", "cidade"))
        
def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
       Medico("nome", "telefone", "", "CRM", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", "cidade"))
        
def test_logrdouro_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Logradouro não pode estar vazio"):
       Medico("nome", "telefone", "email", "CRM", 100,
                            Endereco("", "numero", "Caminho K", "cep", "cidade"))
        
def test_numero_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Número não pode estar vazio"):
       Medico("nome", "telefone", "numero", "CRM", 100,
                            Endereco("logradouro", "", "complemento", "cep", "cidade"))
        
def test_complemento_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Complemento não pode estar vazio"):
       Medico("nome", "telefone", "email", "CRM", 100,
                            Endereco("logradouro", "numero", "", "cep", "cidade"))
        
def test_cep_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "CEP não pode estar vazio"):
       Medico("nome", "telefone", "email", "CRM", 100,
                            Endereco("logradouro", "numero", "complemento", "", "cidade"))
        
def test_cidade_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Cidade não pode estar vazio"):
       Medico("Nome", "Telefone", "Email", "CRM", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", ""))
