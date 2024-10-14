import pytest
from projeto.models import Endereco
from projeto.models import Engenheiro

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro("Nome", "Telefone", "Email", "crea", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", "cidade"))
    return engenheiro

def test_validar_nome(pessoa_valida):
    assert pessoa_valida.nome == "Nome"

def test_validar_telefone(pessoa_valida):
    assert pessoa_valida.telefone == "Telefone"

def test_validar_email(pessoa_valida):
    assert pessoa_valida.email == "Email"

def test_validar_crea(pessoa_valida):
    assert pessoa_valida.crea == "crea"

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
        Engenheiro("", "Telefone", "Email", "crea", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", "cidade"))

def test_telefone_invalido(pessoa_valida):
   with pytest.raises(ValueError, match= "Digite apenas números."):
        Engenheiro("Nome", 147845, "email", "crea", 100,
                            Endereco("logradoouro", "numero", "complemento", "cep", "cidade"))
        
def test_email_invalido(pessoa_valida):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Engenheiro("nome", "telefone", "", "crea", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", "cidade"))
        
def test_logrdouro_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Logradouro não pode estar vazio"):
        Engenheiro("nome", "telefone", "email", "crea", 100,
                            Endereco("", "numero", "Caminho K", "cep", "cidade"))
        
def test_numero_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Número não pode estar vazio"):
        Engenheiro("nome", "telefone", "numero", "crea", 100,
                            Endereco("logradouro", "", "complemento", "cep", "cidade"))
        
def test_complemento_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Complemento não pode estar vazio"):
        Engenheiro("nome", "telefone", "email", "crea", 100,
                            Endereco("logradouro", "numero", "", "cep", "cidade"))
        
def test_cep_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "CEP não pode estar vazio"):
        Engenheiro("nome", "telefone", "email", "crea", 100,
                            Endereco("logradouro", "numero", "complemento", "", "cidade"))
        
def test_cidade_invalido(pessoa_valida):
    with pytest.raises(ValueError, match = "Cidade não pode estar vazio"):
        Engenheiro("Nome", "Telefone", "Email", "crea", 100,
                            Endereco("logradouro", "numero", "complemento", "cep", ""))
