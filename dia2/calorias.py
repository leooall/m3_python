import math

grado_alcoholico = float(input("Ingrese los grados alcoholicos: \n"))


# calorias = 7 * grado_alcoholico (1 grado alcoholico aporta a 7 calorias)
calorias = 7 * grado_alcoholico

print(f'Las calorías totales del producto son: {math.ceil(calorias)}')