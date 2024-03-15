#entrada de datos
peso = int(input("Ingresar peso en Kilogramos: \n"))
talla = int(input("Ingresar talla en centimetros: \n"))

#conversion de cm a mts como lo pide la formula
talla = talla / 100

#aplicacion de la formula imc=peso/talla2
imc = round(peso / (talla * talla),2)

#condicionales con sus respectivas salidas de datos
if imc < 18.5 :
    print(f"Su IMC es {imc}\nLa clasificacion OMS es Bajo Peso")
elif imc >= 18.5 and imc < 25 :
    print(f"Su IMC es {imc}\nLa clasificacion OMS es Adecuado")
elif imc >= 25 and imc < 30 :
    print(f"Su IMC es {imc}\nLa clasificacion OMS es Sobrepeso")
elif imc >= 30 and imc < 35 :
    print(f"Su IMC es {imc}\nLa clasificacion OMS es Obesidad Grado I")
elif imc >= 35 and imc < 40 :
    print(f"Su IMC es {imc}\nLa clasificacion OMS es Obesidad Grado II")
elif imc > 40 :
    print(f"Su IMC es {imc}\nLa clasificacion OMS es Obesidad Grado III")



