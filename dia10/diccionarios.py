"""
DICCIONARIOS    
par -> {clave : valor}
la clave en un mismo dicc debe ser unica-> si existe duplicidad imprime solo el ultimo valor 
OJO con las mayus en las claves
"""
#diccionario vacio
notas = {} 

#creacion de un diccionario
notas = {
    "camila": 7,
    "antonio": 7, 
    "felipe": 6,
    "antonia": 7,
    "antonia": 6,
    }
#acceder a los valores del diccionario
print(notas["camila"]) #7
print(notas["antonio"]) #7
print(notas["felipe"]) #6

print(notas["antonia"]) #7 #6
#print(notas["mijahil"]) #keyerrro: "mijahil"
#print(notas["feLiPe"]) #7keyerrro: "feLiPe"

#agregar par de clave:valor al diccionario
#diccionario[clave] = valor
notas["mijahil"] = 7
print(notas)

#cambiar el valor a una clave
notas["mijahil"] = 9
print(notas)

#eliminar clave:valor de un diccionario con del
del notas["antonia"] # tambien se puede usar pop
print(notas)

#pop -> al eliminar permite capturar el elemEnto en una variable
#imprime solo el valor del key eliminado
print(notas) #{'camila': 7, 'felipe': 6, 'mijahil': 9}

# union de diccionarios diccionario.update()
notas2 = {
    "alexis": 6,
    "yasna": 6,
    "camila": 3,
}
#notas.update(notas2) #{'camila': 3, 'felipe': 6, 'mijahil': 9, 'alexis': 6, 'yasna': 6}
print(notas)

#cuidado colision de igualdad de llaves "camila"
# {'camila': 3, 'felipe': 6, 'mijahil': 9, 'alexis': 6, 'yasna': 6}

print("*****")
notas2.update(notas)
print(notas2)#{'alexis': 6, 'yasna': 6, 'camila': 7, 'antonio': 7, 'felipe': 6, 'mijahil': 9}

