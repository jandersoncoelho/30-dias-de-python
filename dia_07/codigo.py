from dataclasses import dataclass


def romeu_e_julieta(val: int):  # SUT
    """
    Param:
       val: int (numero)

    Se val for divisível por 3 -> 'Queijo'
    Se val for divisível por 5 -> 'Goiabada'
    Se val for divisível por 3 e 5 -> 'Romeu e Julieta'
    Se val não for divisível por 3 ou 5 -> val
    """
    match val % 3 == 0, val % 5 == 0:
        case [True, False]:
            return 'Queijo'

        case [False, True]:
            return 'Goiabada'

        case [True, True]:
            return 'Romeu e Julieta'

        case _:
            return val


# Caso 2 Schema ---------------------------


@dataclass
class Tarefa:
    id: int
    nome: str
    status: str = 'a fazer'


# Caso 3 DOC ---------------------------


class ListaDeTarefas:
    def __init__(self) -> None:
        self.tarefas: list[Tarefa] = []
        self.contador_de_id = 1

    def cria_tarefa(self, nome, status='a fazer') -> Tarefa:
        # Tarefa = DOC
        t = Tarefa(self.contador_de_id, nome, status)

        self.tarefas.append(t)
        self.contador_de_id += 1

        return t

    def atualiza_tarefa(
        self,
        identificador: int,
        nome: str | None = None,
        status: str | None = None
    ) -> None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                if nome:
                    tarefa.nome = nome
                if status:
                    tarefa.status = status
                break

    def deletar_tarefa(self, identificador: int) -> None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                self.tarefas.remove(tarefa)
                break

    def recuperar_tarefa(self, identificador: int) -> Tarefa | None:
        for tarefa in self.tarefas:
            if tarefa.id == identificador:
                return tarefa
        return None
