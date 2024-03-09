#la separacion de los float es un punto (.)
#la division entre integers el resultado es siempre un float

print(4/2)
print(5/2)
print(5/3.5)
print(2.4*4)

nombre = "leo"
año = "2024"
print(3*nombre) #si se puede multiplicar string
print(año*2)
#print(nombre/2)#No se puede dividir un string

#interpolacion de cadenas (otra forma de imprimir) (f)
mes = 3
dia = 7
año = 2024
print(f"hola {nombre} el año es {año} del mes {mes} y el dia {dia}")

#string.format
print("".format())
print("hola {} el año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#interpolacion con % (%s para string y %d para numeros)
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre, año, mes,dia))

#metodo count--> cuenta cuantas veces se encuentra un caracter en un string  
print("saitama".count("a"))
print(nombre.count("i"))
#metodo upper(todo a mayuscula) y lower(todo a minuscula)
print(nombre.upper())
print("sAitAma".lower())
#metodo title ->solo la primera letra mayuscula
print("sAitAma".title())

#len ->cuenta caracteres de una string
print(len("  israel palma 2024"))

print(",  ".join(["leonardo","llaupe","paillama"]))

#salto de linea(\n)
print("cualquier\ncosa")

#las variables** 
#comienzan con una minuscula
#no pueden tener espacio 
#separaciones con _
#no pueden comenzar con un numero

peso = 85.5
verdadero = True
#tipo de dato type(nombre_variable) 
print(type(nombre))
print(type(año))
print(type(peso))
print(type(verdadero))

#manipulacion de variable
numero = 2
numero = numero + 3 #numero = 2 + 3
print(numero)

nombre = nombre + "llaupe"  #concatenacion de str
print(nombre)

#precision de datos
print(5/9)
print(f"resultado de la division {5/9:.2f}")
print("resultado de la division", round(5/9,2))

nombre = input ("ingrese nombre")
print("tu nombre es", nombre)
print(f"tu nombre es {nombre}")
edad = input("ingrese su edad: ")
print("tu tienes", edad, "años")
print(type(edad))