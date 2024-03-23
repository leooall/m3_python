# Recordatorios originales recordatorios.py/material descargable
recordatorios = [
    ['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]
]

# 1. Agregar un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”.
recordatorios.append(['2021-02-02', "06:00", "Empezar el Año"])

# 2. Corregir el evento del 15 de Julio al 16 de Julio.
for evento in recordatorios:
    if evento[0] == '2021-07-15':
        evento[0] = '2021-07-16'

# 3. Eliminar el evento del día del trabajo.
for evento in recordatorios:
    if 'trabajar' in evento[2].lower():
        recordatorios.remove(evento)

# 4. Agregar una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
recordatorios.append(['2021-12-24', "22:00", "Cena de Navidad"])
recordatorios.append(['2021-12-31', "22:00", "Cena de Año Nuevo"])

# Ordenar la lista de recordatorios por fecha
recordatorios.sort()

# Imprimir la lista de recordatorios actualizada
for evento in recordatorios:
    print(evento)
