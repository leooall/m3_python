import sys
#Se crea un diccionario vacio para guardar los valores
pesos= {}
#se crean las keys y se transforman a float los argumentos ingresados por sys.argv 
pesos["pen"] = float(sys.argv[1])
pesos["ars"] = float(sys.argv[2])
pesos["usd"] = float(sys.argv[3])
pesos["clp"] = int(sys.argv[4])

#se ejecutan los datos para obtener la equivalencia en cada moneda cotizada desde nuestra moneda base
pen = pesos["pen"] * pesos["clp"]
ars = pesos["ars"] * pesos["clp"]
usd = pesos["usd"] * pesos["clp"]
clp = pesos["clp"]


#se imprimen los resultados
print(f"Los {clp} Pesos Chilenos equivalen a:\n {pen} Soles Peruanos\n {ars} Pesos Argentinos\n {usd} Dolares Americanos")


""" ***OTRA FORMA EN LA QUE ABORDE EL  PROBLEMA*** 
#se importa el modulo sys para la entrega de datos a traves de la terminal
import sys
#linea de entrada de datos segun pdf: conversiones.py 0.0046 0.093 0.0013 10000

#se transforman a float y guardan en variables las tasas de conversion de cada moneda 
#ademas de la moneda base a convertir 
tasa_conversion_pen = float(sys.argv[1]) 
tasa_conversion_ars = float(sys.argv[2]) 
tasa_conversion_usd = float(sys.argv[3])
clp_base = int(sys.argv[4])

#se ejecutan los datos para obtener la equivalencia en cada moneda
clp_base_a_pen = clp_base * tasa_conversion_pen
clp_base_a_ars = clp_base * tasa_conversion_ars
clp_base_a_usd = clp_base * tasa_conversion_usd

#se imprimen los resultados
print(f"Los {clp_base,} Clp equivalen a:\n {round(clp_base_a_pen,1)} Soles Peruanos\n {round(clp_base_a_ars,1)} Pesos Argentinos\n {round(clp_base_a_usd,1)} Dólares Americanos")
"""
