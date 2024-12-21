"""

CSV =

Album: Labirinto da ...
Data: 2024
Musica: Adeus adeus
letra: A vida permeava...

Labirinto da ...,2024,Adeus adeus,A vida permeava...
"""

from csv import DictWriter

import dateparser
from httpx import get
from parsel import Selector


def letra(url: str) -> str:
    """Pega a letra de um música."""
    response = get(url)
    s = Selector(response.text)
    letra = '\n'.join(s.css('[data-lyrics-container]::text').getall())
    return letra


def faixas(url: str) -> list[tuple[str, str]]:
    response = get(url)
    s = Selector(response.text)

    musicas = s.css('div.chart_row-content')

    return [
        (musica.css('h3::text').get().strip(), musica.css('a').attrib['href'])
        for musica in musicas
    ]


def discos(url: str) -> list[tuple[str | None, ...]]:
    response = get(url)
    s = Selector(response.text)

    discos = s.css('.ZvWhZ')

    resultado = []

    for disco in discos:
        disco_url = disco.css('.kqeBAm').attrib['href']
        disco_nome = disco.css('.gpuzaZ::text').get()
        disco_ano = disco.css('.cedmJJ::text').get()

        resultado.append(
            (disco_url, disco_nome, disco_ano)
        )

    return resultado


url = 'https://genius.com/artists/Dead-fish/albums'


with open('deadfish.csv', 'w') as f:
    writer = DictWriter(f, ['album', 'data', 'musica', 'letra'])
    writer.writeheader()
    for disco in discos(url):
        for faixa in faixas(disco[0]):
            row = {
                'album': disco[1],
                'data': dateparser.parse(disco[2]),
                'musica': faixa[0],
                'letra': letra(faixa[1])
            }
            print(row)
            writer.writerow(row)
