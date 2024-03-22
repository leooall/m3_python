#REPAZO DICCIONARIO
notas = {
    "camila": 7,
    "antonio": 7, 
    "felipe": 6,
    "antonia": 7,
    "antonia": 6,
    }
print(notas)
print(len(notas)) #4 porq ignora a la primera antonia y se queda con el ultimo valor

print(notas.get("camila")) #7 obtiene el valor de la key camila
print(notas.get("Mijail",10))# 10 imprime 
print(notas.get("Mijail",))# None 

prueba = notas.get("julio") #guardamos en una variable clave:valor que NO esta en el dicc 
print(prueba)# None  imprimimos y no escuentra esa clave:valor en el dicc
print(type(prueba))#<class 'NoneType'>

#para agregar una nueva clave valor
notas["leo"] = "fullstack"
print(notas) #{'camila': 7, 'antonio': 7, 'felipe': 6, 'antonia': 6, 'leo': 'fullstack'}

notas["leo"] = "100"
print(notas) #{'camila': 7, 'antonio': 7, 'felipe': 6, 'antonia': 6, 'leo': '100'}

notas.setdefault("juan",10) #otro metodo para agregar key valor
print(notas)#{'camila': 7, 'antonio': 7, 'felipe': 6, 'antonia': 6, 'leo': '100', 'juan': 10}

notas.setdefault("juan",2) #
print(notas.setdefault("juan",2)) # cuando la clave ya existe devuelve su valor existente, NO LO REMPLAZA
print(notas)

notas.setdefault("valeria",) # agregamos una key sin valor
print(notas) #{'camila': 7, 'antonio': 7, 'felipe': 6, 'antonia': 6, 'leo': '100', 'juan': 10, 'valeria': None}

print("******")
eliminado = {}
eliminado["camila"]=notas.pop("camila")
print(notas)
print(eliminado)

##TUPLAS****similar a las listas pero son inmutables (valor1,valor2,....)
print("********")
tupla1=notas.popitem()#elimina y devuelve la tupla(clave:valor)
print(tupla1)
print(notas)#
###Tuplas => similar a las litas pero son inmutables (valor1,valor2...valorn)
print(tupla1[0])
print(tupla1[1])
#tupla1[1]= "Mishi" -->TypeError: 'tuple' object does not support item assignment

notas.clear()#elimina los elemtos dejando un dicc vacio

###Comparar diccionarios
dic1 = {1:"uno",2:"dos"}
dic2 = {2:"dos",1:"uno"}
dic3 = {2:"dos",3:"tres"}
dic4 = {2:"dos",3:"cuatro"}
print(dic1==dic2) #True
print(dic1==dic3) #False
print(dic4==dic3) #False

print("********")

##DICCIONARIOS ANIDADOS
pares_impares ={
    "pares":{
        2:"dos",
        4:"cuatro",
        6:"seis",
        8:"ocho",
        10:"diez"
        },
    "impar":{"uno":1,"tres":3,"cinco":5,"siete":7,"nueve":9},
}

print(pares_impares)

#imprimir el valor "seis"
print(pares_impares["pares"])#{2: 'dos', 4: 'cuatro', 6: 'seis', 8: 'ocho', 10: 'diez'}
print(pares_impares["pares"][6]) #seis

#imprimir el valor 5
print(pares_impares["impar"])#{'uno': 1, 'tres': 3, 'cinco': 5, 'siete': 7, 'nueve': 9}
print(pares_impares["impar"]["cinco"]) #5
#si se tiene mas diccionarios se agregan mas corchetes..



