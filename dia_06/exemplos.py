from pathlib import Path
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from InquirerPy.validator import PasswordValidator

# email = inquirer.text(
#     'Email:',
#     validate=lambda text: '@' in text,
#     invalid_message='Email precisa conter @.'
# ).execute()


# credencial = inquirer.text(
#     'Senha: ',
#     is_password=True,
#     transformer=lambda text: len(text) * '&',
#     validate=PasswordValidator(
#         cap=True, special=True, number=True, length=8,
#         message='A senha precisa de um caractere especial, uma maiúscula e um número'
#     ),
# ).execute()


# auth_code = inquirer.text(
#     'Auth code:',
#     validate=lambda code: len(code) == 6 and code.isdigit(),
#     invalid_message='O código tem 6 dígitos',
#     transformer=lambda code: f'{code[:3]}-{code[3:]}'
# ).execute()


# permision_file = inquirer.filepath(
#     'Arquivo de credenciais:',
#     default=str(Path().home()),
#     validate=lambda path: Path(path).resolve().suffix == '.pub',
#     invalid_message='Precisa ser u arquivo .pub'
# ).execute()


opção = inquirer.fuzzy(
    '=== Calculadora ===', choices=[
        Choice(value='*', name='Multiplicar'),
        Choice(value='+', name='Somar'),
        Choice(value='-', name='Subtrair'),
        Choice(value='/', name='Dividir'),
        Choice(value=None, name='Sair!')
    ]
).execute()

print(opção)
