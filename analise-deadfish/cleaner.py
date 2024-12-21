import polars as pl


df = pl.read_csv('deadfish.csv', try_parse_dates=True)

df = df.with_columns(
    df.get_column('album').str.to_lowercase(),
    df.get_column('musica').str.to_lowercase(),
    (
        df.get_column('letra')
        .str.replace_all(r'\[.*\]', '')
        .str.replace_all('\n', ' ')
        .str.replace_all('\u2005', ' ')
        .str.replace_all('\u205f', ' ')
        .str.replace_all('\x92', "'")
        .str.replace_all('  ', ' ')
        .str.strip_chars()
        .str.to_lowercase()
     )
)

df.write_csv('deadfish_limpo.csv')

# ---- DEBUG!

# printable = df.with_columns(
#     pl.col('letra')
#     .alias('printable')
#     .map_elements(lambda x: x.isprintable(), return_dtype=bool)
# )

# debug = printable.filter(pl.col('printable') == False)

# print(len(df), len(debug))
# print(repr(debug[0]['letra'][0]))

# print(printable)

# ---- FIM DEBUG!
