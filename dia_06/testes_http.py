from datetime import datetime, timedelta
from typing import Literal, TypeAlias, get_args

from InquirerPy import inquirer
import httpx
import respx
import humanize
import time_machine

humanize.activate('pt_BR')
URL_COTAÇÃO = 'https://economia.awesomeapi.com.br/json/last/{}'
Moeda: TypeAlias = Literal['EUR', 'USD', 'BTC']
moedas = humanize.natural_list(get_args(Moeda)).replace(
    'and', 'ou'
)


def cotação(moeda: Moeda | None = None, verbose: bool = False):
    if not moeda:
        moeda = inquirer.select(
            'Selecione a moeda:', list(get_args(Moeda)),
        ).execute()
    
    code = f'{moeda}-BRL'

    try:
        response = httpx.get(URL_COTAÇÃO.format(code))
        data = response.json()[code.replace('-', '')]
        isotime = datetime.fromtimestamp(
            int(data['timestamp'])
        )

        if verbose:
            print(f'Requisição feita em: {datetime.now()}')

        return (
            f'Última cotação ({humanize.naturaltime(isotime)}): '
            f'{humanize.intcomma(float(data['high']))}'
        )

    except KeyError:
        return f'Código de moeda ({moeda}) inválido. Use {moedas}'

    except httpx.InvalidURL:
        return f'Código de moeda inválido. Use {moedas}'

    except httpx.ConnectError:
        return 'Erro de conexão, tente mais tarde.'

    except httpx.TimeoutException:
        return 'Erro de conexão, tente mais tarde.'


@respx.mock
def test_dolar():
    # Arange
    with time_machine.travel('2024-11-02', tick=False):
        mocked_response = httpx.Response(
            200, json={'USDBRL': {
                'high': 5.7945,
                'timestamp': datetime.now().timestamp()
            }}
        )
        respx.get(
            URL_COTAÇÃO.format('USD-BRL')
        ).mock(mocked_response)

        # Act
        result = cotação('USD')

    # Assert
    assert result == 'Última cotação (agora): 5,7945'


@respx.mock
@time_machine.travel('2024-11-02', tick=False)
def test_bitcoin():
    mocked_response = httpx.Response(
        200, json={'BTCBRL': {
            'high': 5.7945,
            'timestamp': (datetime.now() - timedelta(seconds=10)).timestamp()
        }}
    )
    respx.get(
        URL_COTAÇÃO.format('BTC-BRL')
    ).mock(mocked_response)

    result = cotação('BTC')

    assert result == 'Última cotação (há 10 segundos): 5,7945'


@respx.mock
def test_euro():
    # Arange
    with time_machine.travel('2024-11-02', tick=False):
        mocked_response = httpx.Response(
            200, json={'EURBRL': {
                'high': 5.7945,
                'timestamp': (
                    datetime.now() - timedelta(3)
                ).timestamp()
            }}
        )
        respx.get(
            URL_COTAÇÃO.format('EUR-BRL')
        ).mock(mocked_response)

        # Act
        result = cotação('EUR')

    # Assert
    assert result == 'Última cotação (há 3 dias): 5,7945'


@respx.mock
def test_moeda_errada():
    mocked_response = httpx.Response(200, json={})

    respx.get(
        URL_COTAÇÃO.format('MDT-BRL')
    ).mock(mocked_response)

    result = cotação('MDT')

    assert (
        result == "Código de moeda (MDT) inválido. Use EUR, USD ou BTC"
    )


def test_moeda_erro_na_URL():
    result = cotação('\x11')

    assert (
        result == "Código de moeda inválido. Use EUR, USD ou BTC"
    )


def test_erro_conexao(respx_mock):
    # Arange
    respx_mock.get(
        URL_COTAÇÃO.format('USD-BRL')
    ).mock(side_effect=httpx.ConnectError)

    # Act
    result = cotação('USD')

    # Assert
    assert result == 'Erro de conexão, tente mais tarde.'


def test_erro_timeout(respx_mock):
    # Arange
    respx_mock.get(
        URL_COTAÇÃO.format('USD-BRL')
    ).mock(side_effect=httpx.TimeoutException)

    # Act
    result = cotação('USD')

    # Assert
    assert result == 'Erro de conexão, tente mais tarde.'
