import humanize as h

# Tamanho de arquivos
val = -3_000_000_000_000_000
print(val)
h.naturalsize(val)

# Datas e Tempo
from datetime import datetime, timedelta
# dias
h.naturalday(datetime.now() + timedelta(1))

# datas
h.naturaldate(datetime.now() + timedelta(365))

# distancia
h.naturaldelta(timedelta(minutes=10))

# distancia precisa
h.precisedelta(
    timedelta(10, hours=10, seconds=10),
    minimum_unit='seconds'
)

h.activate('pt_BR')
h.deactivate()

# Números
h.fractional(1)
h.scientific(1.1827678)
h.metric(10, 'KV/h')
h.ordinal(56, gender='female')
h.intcomma(5000.65)
h.intword(200)

# Listas
h.natural_list([1, 2, 3])
