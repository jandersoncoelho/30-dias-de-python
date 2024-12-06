from getpass import getpass
from pathlib import Path


def credenciais():
    email = input('Email: ')
    credencial = getpass('Credenciais: ')
    auth_code = input('Auth Code: ')
    permision_file = input('Arquivo de permissão (path): ')
    permission_path = Path(permision_file).resolve()

    if permission_path.exists() and permission_path.suffix == '.pub':
        print(f'{email=}, {credencial=}, {auth_code=}, {permission_path=}')
    else:
        print(
            'Arquivo de permissão não existe ou não é um arquivo de chave publica'
        )

        
def menu():
    menu = """
    O que deseja fazer?

    1. blah
    2. bleh
    3. blih
    4. bloh
    5. bluh
    """
    opção = input(menu)
    print(opção)
