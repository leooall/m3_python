import math
r = float(input("Ingrese el radio en kilómetros: \n")) 
g = float(input("Ingrese la constante gravitacional: \n"))
r = r * 1000 
velocidad_escape = math.sqrt(2 * (g * r)) 

print("La velocidad de Escape es:", round(velocidad_escape,1), "[m/s]")



