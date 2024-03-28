
from os import system
import suma # Importamos modulo suma
import resta as r #importamos modulo resta
from input import captura_de_datos #Importamos la función de nuestro módulo "input" para obtener los datos 

print("calculadora basica\n")
opcion = int(input("""Esto es una calculadora:
¿Qué operación le gustaría realizar?
1. Sumar
2. Restar
0. Salir
> """))
system("cls")
if opcion == 1 :
    x, y = captura_de_datos()
    suma.sumar(x, y)
elif opcion == 2:
    x, y = captura_de_datos()
    r.restar(x, y)
elif opcion == 0:
    print("hasta luego")
else:
    #exit()-> se pone termino a la ejecucion del programa y lo de abajo NO se ejecuta
    print("opcion invalida")
