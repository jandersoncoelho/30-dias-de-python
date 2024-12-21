import time


def calculo_idade(dado):
    """Chama o banco e faz um conta."""
    return dado

def verifica_idade():
    if calculo_idade(10) >= 18:
        return 'maior'
    else:
        return 'menor'

calculo_idade = lambda x: 10  # stub

print(verifica_idade())
