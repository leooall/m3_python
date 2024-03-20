"""
debe retornar un diccionario con el mes y el valor asociado siempre
y cuando superen el umbral especificado.
"""
import sys

umbral = int(sys.argv[1])
ventas = {
    "Enero": 15000, 
    "Febrero": 22000, 
    "Marzo": 12000, 
    "Abril": 17000, 
    "Mayo": 81000, 
    "Junio": 13000, 
    "Julio": 21000,
    "Agosto": 41200, 
    "Septiembre": 25000, 
    "Octubre": 21500, 
    "Noviembre": 91000, 
    "Diciembre": 21000, 
    }
#creacion diccionario vacio
mayor_umbral = {}

#recorrer diccionario
for clave, valor in ventas.items():
    #print(f"clave {clave} - valor {valor}")
    if valor > umbral :
        #agregar el par de datos (clave, valor) en el nuevo diccionario)
        mayor_umbral[clave] = valor 

#se imprimen las claves con sus valores, si superaron el umbral
print(f"el nuevo diccionario es {mayor_umbral}")
    





