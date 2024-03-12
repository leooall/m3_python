from math import sqrt #se importa un metodo de la libreria en especifico
r = float(input("Ingrese el radio en kilómetros: \n")) 
g = float(input("Ingrese la constante gravitacional: \n"))

#pasamos los kilometros a metros
r = r * 1000 

#aplicamos la formula para obtener la velocidad de escape
velocidad_escape = sqrt(2 * (g * r)) 

print("La velocidad de Escape es:", round(velocidad_escape,1), "[m/s]")



