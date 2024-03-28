
from os import system

""" 
Funciones

Si una funcion no se invoca, NUNCA se ejecutara el código en su interior
es imperativo utilizar (), en el llamado a la función

def nombre_de_la_funcion(variable):
    #codigo a ejecutar
    
nombre_de_la_funcion(3)

PARAMETRO, variable a utilizar en la funcion
ARGUMENTO, valor que sera pasado en el llamado de la función

cuando hacemos un RETURN de multiples valores, se retorna una TUPLA

"""
print("Inicio")
#imprimir_menu() #no se puede llamar a una funcion que no este definida previamente

#definicion de la funcion
def imprimir_menu():
    print("Opciones: ")
    print("1). De acuerdo")
    print("2). En desacuerdo")
    print("3). No me interesa")

#llamado a la funcion (invocación)
imprimir_menu()
imprimir_menu()
imprimir_menu()
print("Fin")

system("cls")
print("**def suma**")
def suma(valor1,valor2):#valor1=3 ; valor2=5
    suma = valor1 + valor2 # suma= 3 + 5; suma = 8
    return suma #return 8 devuelve el valor a donde fue invocada la funcion, sig linea
suma(3,5)#aqui llega el return

def suma2(valor1,valor2):
    return valor1 + valor2 #return 
    print("qwerty123456")#nunca se ejecutara

print("valor de respuesta",suma2(1,9))#10, se imprime el valor de retorno

resultado = suma2(6,7)#capturando el valor de retorno en una variable
print("valor respuesta capturado",resultado)#13 ,imprime valor de retorno

print("**RETORNO MULTIPLE**")
#RETORNO MULTIPLE
def cuadrado_cubo(base):
    cuadrado = base ** 2
    cubo = base  ** 3
    return cuadrado, cubo

print(cuadrado_cubo(2))#retorno de una tupla (4, 8)

valor_cuadrado,valor_cubo = cuadrado_cubo(3) #guardamos los valores en dos variables
print(valor_cuadrado,valor_cubo)#(9,27)

print("**DICC UMBRAL PRECIOS**")

def filtrar(diccionario, umbral):# diccionario = precios ; Umbral = valor
    filtro = {k:v for k,v in diccionario.items() if v > umbral} #comprehesions
    return filtro

precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}
print(filtrar(precios, 25000))

print("**PARAMETROS OBLIGATORIOS**")
#PARAMETROS OBLIGATORIOS
def extremo_multiplicado(lista,factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo

print(extremo_multiplicado([1,2,3,4], 4))# primero lista segundo el factor

print(extremo_multiplicado(factor = 4, lista = [1,2,3,4]))# otro orden, pero especificando para que parametro

print("**PARAMETROS OPCIONALES O POR DEFAULT**")
#PARAMETROS OPCIONALES O POR DEFAULT
#se agrega false en parametro redondear en caso de que no ingresen un argumento
def elevar(base, exponente, redondear = False):# redondear = false
    if redondear:
        valor = round(base**exponente, 2)
    else:
        valor = base**exponente
    return valor

print(elevar(2, 3))#8

print(elevar(2, 3, redondear = True))#8 se le cambia el valor a redondear  por true

print("****KWARGS**")
# **KWARGS -> cada argumento TIENE que ir con su nombre 
def parametros(**kwargs):
    print(kwargs)#se imprime un diccionario
    print(kwargs["lista1"])# se imprime solo la lista1

parametros(numero1= 23, texto ="Hola", lista1 = [2,3,4,5,6])

print("***ARGS**")
# *ARGS ->  numero indeterminado de argumentos
def argumentos(*args):
    print(args)#se recibe una tupla
    print(args[0])#23
    print(args[2])#[2,3,4,5,6]
    
argumentos(23,"hola",[2,3,4,5,6])


print("***VARIABLES LOCALES Y VARIABLES GLOBALES**")
#VARIABLES LOCALES Y VARIABLES GLOBALES

pais = "Chile" #variable global
#constantes
G = 9.8
PI = 3.14
IVA = 19

def ciudades():
    #scope de la variable "capital" es solo en el metodo ciudades()
    capital = "Santiago" #es una variable local o scope
    print(pais, capital)
    #pais = "Peru" # no se puede/recomiendo modificar el valor de una variable global

    return capital # return "Santiago"
    
print(pais)
ciudades() #Chile Santiago
#print(capital)#variable no definida globalmente
print(pais)