
""" 
peso_kilogramos=float(input("ingrea tu peso en kilogramos"))
estatura = float(input("ingresa tu estatura en cm"))/100
estatura = estatura /100 #convirtiendo centimetros a metros
"""
import sys
# se ejecuta en la terminal: python3 desafio2/imc.py 81 178
print(sys.argv)     #['desafio2/imc.py', '81', '178']
print(sys.argv[1])  #81
print(sys.argv[2])  #178

peso_kilogramos= float(sys.argv[1])
estatura = float(sys.argv[2])/100

print(type(peso_kilogramos))
print(type(estatura))

#calculo del imc
#imc = peso_kilogramos/ (estatura * estatura)
imc = peso_kilogramos/ (estatura ** 2 )
print(f"Tu IMC es de {round(imc,2)}")
#print(f"Tu IMC es de {imc:.2}")

if imc < 18.5:
    clasificacion = "Bajo Peso"
elif imc >=18.5 and imc < 25:
    clasificacion = "Adecuado"
elif imc < 30:
    clasificacion = "Sobrepeso"
elif imc < 35:
    clasificacion = "Obesidad grado I"
elif imc < 40:
    clasificacion = "Obesidad grado II"
elif imc >=40:
    clasificacion = "Obesidad grado III"

print(f"Tu clasificación según la OMS es: {clasificacion}")