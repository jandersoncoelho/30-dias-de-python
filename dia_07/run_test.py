from codigo import ListaDeTarefas
from codigo import Tarefa
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


def test_lista_de_tarefas_atualiza_tarefa():
    """Testa se o nome da tarefa é atualizado corretamente."""
    # arrange
    ldt = ListaDeTarefas()
    nome_antigo = 'test'
    nome_novo = 'test2'
    tarefa_criada = ldt.cria_tarefa(nome_antigo)

    # act
    ldt.atualiza_tarefa(tarefa_criada.id, nome=nome_novo)

    # assert
    tarefa_atualizada = ldt.recuperar_tarefa(tarefa_criada.id)  # type: ignore
    assert tarefa_atualizada is not None
    assert tarefa_atualizada.nome == nome_novo  # type: ignore
    assert tarefa_atualizada.nome != nome_antigo  # type: ignore


def test_lista_de_tarefas_atualiza_status_da_tarefa():
    """Testa se o status da tarefa é atualizado corretamente."""
    # arrange
    ldt = ListaDeTarefas()
    status_antigo = 'a fazer'
    status_novo = 'feito'
    tarefa_criada = ldt.cria_tarefa('test name')

    # act
    ldt.atualiza_tarefa(tarefa_criada.id, status=status_novo)

    # assert
    tarefa_atualizada = ldt.recuperar_tarefa(tarefa_criada.id)  # type: ignore
    assert tarefa_atualizada is not None
    assert tarefa_atualizada.status == status_novo  # type: ignore
    assert tarefa_atualizada.status != status_antigo  # type: ignore


def test_lista_de_tarefas_nao_deve_atualizar_tarefa_inexistente():
    """Testa que nada acontece ao tentar atualizar uma tarefa que não existe."""
    # arrange
    ldt = ListaDeTarefas()

    # act
    ldt.atualiza_tarefa(999, nome='novo nome')

    # assert
    assert ldt.recuperar_tarefa(999) is None


def test_lista_de_tarefas_deletar_tarefa():
    """Testa se uma tarefa é deletada com sucesso."""
    # arrange
    ldt = ListaDeTarefas()
    tarefa1 = ldt.cria_tarefa('tarefa 1')
    tarefa2 = ldt.cria_tarefa('tarefa 2')

    # act
    ldt.deletar_tarefa(tarefa1.id)

    # assert
    assert ldt.recuperar_tarefa(tarefa1.id) is None
    assert ldt.recuperar_tarefa(tarefa2.id) is not None
    assert len(ldt.tarefas) == 1


def test_lista_de_tarefas_nao_deve_deletar_tarefa_inexistente():
    """Testa que nada muda ao tentar deletar uma tarefa que não existe."""
    # arrange
    ldt = ListaDeTarefas()
    ldt.cria_tarefa('minha tarefa')

    # act
    ldt.deletar_tarefa(999)

    # assert
    assert len(ldt.tarefas) == 1


def test_lista_de_tarefas_atualiza_nome_e_status_da_tarefa():
    """Testa se o nome e o status da tarefa são atualizados corretamente."""
    # arrange
    ldt = ListaDeTarefas()
    nome_antigo = 'nome antigo'
    status_antigo = 'a fazer'
    tarefa_criada = ldt.cria_tarefa(nome_antigo, status_antigo)

    nome_novo = 'nome novo'
    status_novo = 'feito'

    # act
    ldt.atualiza_tarefa(tarefa_criada.id, nome=nome_novo, status=status_novo)

    # assert
    tarefa_atualizada = ldt.recuperar_tarefa(tarefa_criada.id)
    assert tarefa_atualizada is not None
    assert tarefa_atualizada.nome == nome_novo
    assert tarefa_atualizada.status == status_novo
