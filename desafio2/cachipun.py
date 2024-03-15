#se importa modulo random
import random 

#entrada de datos
jugada = input("Ingresa piedra, papel o tijera\n")

#generacion de la variable opciones que contendra las opciones de jugadas para el computador
opciones = ["piedra", "papel", "tijera"]

#creacion de la variable jugada_computador que contiene las opciones de jugadas de forma aleatoria gracias al modulo random.choice()
jugada_computador = random.choice(opciones)

#condicionales con sus respectivas salidas de datos
#jugadas con piedra
if jugada == "piedra" and jugada_computador == "piedra" :
    print("Tu jugaste Piedra \nComputador jugó Piedra \nEmpate!!")
    
elif jugada == "piedra" and jugada_computador == "papel" :
    print("Tu jugaste Piedra \nComputador jugó Papel \nPerdiste =(") 

elif jugada == "piedra" and jugada_computador == "tijera" :
    print("Tu jugaste Piedra \nComputador jugó Tijera \nGanaste!!")
    
#jugadas con papel
elif jugada == "papel" and jugada_computador == "papel" :
    print("Tu jugaste Papel \nComputador jugó Papel \nEmpate!!")
    
elif jugada == "papel" and jugada_computador == "tijera" :
    print("Tu jugaste Papel \nComputador jugó Tijera \nPerdiste =(")    
    
elif jugada == "papel" and jugada_computador == "piedra" :
    print("Tu jugaste Papel \nComputador jugó Piedra \nGanaste!!")    
    
#jugadas con tijera
elif jugada == "tijera" and jugada_computador == "tijera" :
    print("Tu jugaste Tijera \nComputador jugó Tijera \nEmpate!!")
    
elif jugada == "tijera" and jugada_computador == "papel" :
    print("Tu jugaste Tijera \nComputador jugó Papel \nGanaste!!")
    
elif jugada == "tijera" and jugada_computador == "piedra" :
    print("Tu jugaste Tijera \nComputador jugó Piedra \nPerdiste =(")

else :
    print("Argumento inválido: Debe ser piedra, papel o tijera.")


