from datetime import datetime
from typing import Literal, TypeAlias, get_args
import httpx
import respx
import humanize

humanize.activate('pt_BR')
URL_COTAÇÃO = 'https://economia.awesomeapi.com.br/json/last/{}'
Moeda: TypeAlias = Literal['EUR', 'USD', 'BTC']
moedas = humanize.natural_list(get_args(Moeda)).replace(
    'and', 'ou'
)


def cotação(moeda: Moeda):
    code = f'{moeda}-BRL'
    try:
        response = httpx.get(URL_COTAÇÃO.format(code))
        data = response.json()[code.replace('-', '')]
        isotime = datetime.fromtimestamp(
            int(data['timestamp'])
        )
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
    mocked_response = httpx.Response(
        200, json={'USDBRL': {
            'high': 5.7945, 'timestamp': 0
        }}
    )
    respx.get(
        URL_COTAÇÃO.format('USD-BRL')
    ).mock(mocked_response)

    # Act
    result = cotação('USD')

    # Assert
    assert result == 'Última cotação (há 54 anos): 5,7945'


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
