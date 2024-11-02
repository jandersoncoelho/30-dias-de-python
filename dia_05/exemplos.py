from dataclasses import dataclass, field
from datetime import datetime
from time_machine import travel

db = []

@dataclass
class User:
    name: str
    created_at: datetime = field(default_factory=datetime.now)


def create_user(name: str) -> User:
    user = User(name=name)

    db.append(user)

    return user
    

@travel('2024-11-02', tick=False)
def test_create_user():
    # arrange
    user_name = 'test'
    user = User(user_name)

    # act
    result = create_user(user_name)

    # assert
    assert result == user
    

# -----------------

def tarefa_periodica():
    """Tarefa executada de hora em hora."""

    if datetime.now().hour == 5:
        print('Enviando relatório!')
        1 / 0
        return True
    else:
        print('Coleta dos dados')
        return True


@travel('2024-11-02 05:01', tick=False)
def test_tarefa_periodica():
    assert tarefa_periodica()


def tempo():
    print(datetime.now())
    with travel('2024-11-02 05:01', tick=False):
        print(datetime.now())
    print(datetime.now())
        
