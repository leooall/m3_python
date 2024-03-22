#tuplas: par ordenado inmutable

from os import system
##TUPLAS****similar a las listas pero son inmutables (valor1,valor2,....)


tupla_eje = ("marzo", "2024")
print(tupla_eje)
print(type(tupla_eje)) #<class 'tuple'>

#desempaquetamiento
mes, anio = tupla_eje
print(mes)
print(anio)

tupla2 = 3,5,(1,11),7,9  #tupla anidada
print(type(tupla2)) #<class 'tuple'>
print(tupla2) #(3, 5, (1, 11), 7, 9)

lista_vocales = ["a","e","i","o","u"]
print(lista_vocales)#['a', 'e', 'i', 'o', 'u']

tupla_vocales = tuple(lista_vocales)
print(tupla_vocales)#('a', 'e', 'i', 'o', 'u')

#iterar una tupla
for tv in tupla_vocales:
    print(tv)
    
    
#count() cuenta las veces q se encuentra un elemento en la tupla
print(tupla_vocales.count("a"))

"""
sets 
se escriben con {}, no tienen claves, no acepta datos repetidos
no tiene orden especifico
no se puede ingresar listas ni dicc tampoco contener otro set
"""
muchos_animales = {'Gato', True, 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 2, 1.5,
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)

muchos_animales.add(7) #agrega el elemento en cualquier orden
print(muchos_animales)

muchos_animales.remove("Hamster")
print(muchos_animales)

muchos_animales.discard("raton")# no hace nada porq no exioste ese elemento
print(muchos_animales)

muchos_animales.discard("Hurón") #lo elimina
print(muchos_animales)

muchos_animales.pop() #elimina cualquiera
print(muchos_animales)

muchos_animales.clear() #dejara un set vacio
print(muchos_animales)

#Convertir un diccionario en una lista --> se convierten en tuplas
lista_dicc=list({"k1": 5, "k2": 7}.items()) 
print(lista_dicc) # [('k1', 5), ('k2', 7)]


#la funcion dir() Permite determinar qué métodos están disponibles en cada tipo de dato y/o estructura. 
