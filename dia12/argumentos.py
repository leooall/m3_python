import sys
#sys.argv[0] -->es siempre el nombre del script

nombre = sys.argv[1] #por eso se parte del [1] en adelante
apellido = sys.argv[2]

print(f"Mi nombre es {nombre}") 
print(f"Mi apellido es {apellido}") 
print(f"nombre de este archivo es {sys.argv[0]}")

print(type(sys.argv)) #notaremos que se trata de una LISTA, esa es la razón por la que podemos utilizar índices para acceder a distintas partes de este.