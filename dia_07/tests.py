from codigo import romeu_e_julieta


# Teste de comportamento

def test_romeu_e_julieta_deve_retornar_queijo():
    """
    Taxinomia dos testes

    AAA = Arrange Act Assert
    4 fases = SetUp / Exercise / Verify / TearDown
    """
    # Arranjo / Arrange / SetUp
    valor_de_input = 3
    esperado = 'Queijo'

    # Act / Exercise / Chamada do SUT
    resultado = romeu_e_julieta(valor_de_input)

    # Assert / Verificação
    assert resultado == esperado


def test_romeu_e_julieta_deve_retornar_goiabada():
    valor_de_input = 5
    esperado = 'Goiabada'

    resultado = romeu_e_julieta(valor_de_input)

    assert resultado == esperado


def test_romeu_e_julieta_deve_retornar_ReJ():
    valor_de_input = 15
    esperado = 'Romeu e Julieta'

    resultado = romeu_e_julieta(valor_de_input)

    assert resultado == esperado


def test_romeu_e_julieta_deve_retornar_val():
    valor_de_input = 1
    esperado = 1

    resultado = romeu_e_julieta(valor_de_input)

    assert resultado == esperado



# Testes caso 2

from codigo import Tarefa

def test_Tarefa_deve_conter_os_campos_id_nome_status():
    # arrange
    identificador = 1
    nome = 'Estudar Testes'
    status = 'fazendo'

    # Act
    t = Tarefa(identificador, nome, status)

    # Assert
    assert t.id == identificador
    assert t.nome == nome
    assert t.status == status


# Testes do caso 3
from codigo import ListaDeTarefas


def test_lista_de_tarefas_criar_tarefa():
    # arrange
    ldt = ListaDeTarefas()
    nome = 'test'

    # act
    t = ldt.cria_tarefa(nome)

    # assert
    assert ldt.recuperar_tarefa(t.id)
    assert t.nome == nome
    assert t.status == 'a fazer'


def test_list_de_tarefas_recuperar_tarefa():
    ldt = ListaDeTarefas()

    # garante que veio None
    assert not ldt.recuperar_tarefa(10)
