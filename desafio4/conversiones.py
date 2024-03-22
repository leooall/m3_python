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

