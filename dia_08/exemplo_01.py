from contextlib import contextmanager
import builtins


def spy_print(message):
    spy_print.message = f'Spy diz: {message}'


@contextmanager
def patch_print():
    # Arange / Setup
    print_original = builtins.print
    builtins.print = spy_print

    yield spy_print # Durante do with

    # Teardonw / limpeza
    builtins.print = print_original
    


def batata():
    print('Estou frita!')


with patch_print() as spy:  # Spy é um duble de testes
    batata()


print(spy.message)

# assert spy.message == 'Estou frita'
