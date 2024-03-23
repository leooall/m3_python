"""
lista: conjunto de datos, ordenados segun su ingreso, separados por coma, 
el primer elemento, esta en la posicion cero, pueden contener distintos tipos de elementos
son mutables
se usan los [] para definir una variable de tipo lista
**indice => la posicion de los elementos

la primera posicion SIEMPRE es CERO
la ultima posicion esta dada por ultimaPosicion= (cantidad_elementos - 1) o lista[-1]
para acceder a los elementos utilizamos las posiciones; lista[posicion]
no existen indices sin elementos en python
los metodos con __nombre__, se les llama magic built-in o dunders
"""

colores = ["verde", "rojo", "verde", "morado"]

print(colores)
print(colores[0])
print(colores[-1])
print(colores[3])

#metodos
#print(colores.__dir__())#muestra todos los elementos que contiene la lista

colores.append("amarillo") # append() agrega un elemento al final de la lista
print (colores)

#insert(i, elemento) -> agregar el elemto en una posicion especifica y si esta utilizada por otro elemto este es desplazado en una posicion mas
colores.insert(0, "blanco")
print(colores)

colores.insert(6, "negro")
print(colores)

colores.insert(8, "cafe")#cuando se agrega en una posicion fuera de rango lo que hace es ubicarlo al final de la lista
print(colores)

colores.insert(-1, "celeste")
print(colores)

#pop([indice])elimina un elemto dentro de la lista
colores.pop(0)
print(colores)

colores.pop(-1)
print(colores)

#remove()
colores.remove("verde")#elimina un elento especifico, pero el primero que encuentra de izq a der
print(colores)

#reverse() = invierte los elementos de la lista, pero de forma permanente
colores.reverse()
print(colores)

#sort() ordena los elementos de manera ascendente/alfabetico por defecto
colores.sort()
print(colores)

#En Python, cuando asignas una lista a otra variable utilizando el operador de asignación (=), estás creando una nueva referencia a la misma lista en la memoria, no una nueva lista. Por lo tanto, ambas variables (lista1 y lista2) apuntan a la misma ubicación de memoria, lo que significa que cualquier cambio realizado en una de las variables también afectará a la otra.
lista1 = [1, 2, 3,]
lista2 = lista1#esto no es un respaldo de la lista
lista3 = lista1.copy()#si es un respaldo de los datos
lista4 = lista1[:] #si es un respaldo de los datos(slice)
lista = list(lista1) #si es un respaldo de los datos

print(lista2)
lista2.append(5)

lista7 = lista1 + [] # se concatena una lista vacia.. puede ser un metodo de respaldo de lista
lista8 = lista1 * 1
#sorted(lista, reverse=True) ordena la lista asc o desc, no es permanente
print(sorted(colores,reverse=True))#['verde', 'rojo', 'negro', 'morado', 'celeste', 'amarillo']
print(colores)#['amarillo', 'celeste', 'morado', 'negro', 'rojo', 'verde']

#index() retorna el indice del elemento
print(colores.index("celeste")) #1

print(colores.index("negro")) #3
#print(colores.index("azul")) #ValueError: 'azul' is not in list

colores.clear()#limpia la lista y la deja vacia
print(colores) 

#operaciones
lista6 = [20,30,40,50]
lista_concatenada = lista1 + lista6
print(lista1)
print(lista6)
print(lista_concatenada)
lista6.append(60)
print(lista_concatenada)
print(lista7)
print(lista8)


