# install pytest + httpx
import httpx


# Fake é um duble de testes
class FakeResponse:
    def __init__(self, url, status_code):
        self.status_code = status_code

    def json(self):
        return {'data': 'fake data'}


def fetch_data(url):
    try:
        response = httpx.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return {}
    except httpx.RequestError:
        return {}


def test_fetch_data_deve_retornar_200(monkeypatch):
    # httpx.get = blah
    monkeypatch.setattr(
        httpx, 'get', lambda url: FakeResponse(url, 200)
    )

    result = fetch_data('https://dunossauro.com')

    assert result == {'data': 'fake data'}


def test_fetch_data_deve_retornar_500(monkeypatch):
    # httpx.get = blah
    monkeypatch.setattr(
        httpx, 'get', lambda url: FakeResponse(url, 500)
    )

    result = fetch_data('https://dunossauro.com')

    assert result == {}


def test_fetch_data_deve_retornar_erro(monkeypatch):
    def patch_error(url):
        raise httpx.TimeoutException('deu ruim')

    # httpx.get = blah
    monkeypatch.setattr(
        httpx,
        'get',
        patch_error
    )

    result = fetch_data('https://dunossauro.com')

    assert result == {}
