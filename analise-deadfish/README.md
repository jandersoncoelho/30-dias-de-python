# Análise das letras do Dead Fish

## Técnica

- Captura dos dados
  - Baixar todas as letras!
    - httpx + parsel - Genius ([Dead Fish Albums and Discography](https://genius.com/artists/Dead-fish/albums))
  - Persistir
    - CSV
- Organização
  - Dataframe - Polars / Pandas
- Limpeza / tratamento
  - Dataframe
  - Repo de stopwords
- Olhar os dados!
  - Spacy
  - WordCloud

# Análise: Perguntas

- Quais são as palavras mais usadas?
  
  - Por disco
  
  - Por década
  
  - Em que contexto?

- Análise léxica
  
  - Quantas palavras únicas por música? (média por disco?)
  
  - Quantas palavras únicas por disco?
  
  - Dispersão (onde a palavra ocorre no disco?)

- Gramatica
  
  - Tag

- Ver
  
  - Nuvem de palavras
  
  - Concord
