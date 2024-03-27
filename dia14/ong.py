#calculo del factorial de un numero
def factorial(numero): #5! = 5*4*3*2*1
    """calculo del factorial de un numero

    Args:
        numero (int): numero del cual se calculara el factorial

    Returns:
        int: resultado del factorial de un numero
    """
    valor = 1 #variable acumuladora
    for n in  range(1, numero + 1): #1,2,3,4,5
        valor = valor * n
    return valor

#print("el factorial es" ,factorial(6))#llamada a la función con el número 5</

#paso 2: una funcion que calcule la productoria

def productoria(lista):
    """funcion que calcule la productoria

    Args:
        lista (int): lista para calcular productoria

    Returns:
        lista: resultado productoria
    """
    valor = 1
    for elemento in lista:
        valor *= elemento
    return valor
#print(productoria([4,6,7,4,3]))

#paso 3: 

def calcular(**parametros): # * tupla; ** diccionario
    for clave,valor in parametros.items():#.items() nos devuelve una tupla 
        if "fact" in clave :
            print(f"el factorial de {valor} es {factorial(valor)}")
        else:
            print (f"el productoria de {valor} es {productoria(valor)}")

#paso4: invocacion al metodo
calcular(fact_1 = 5, prod_1 = [3,6,4,2,8], fact_2 = 6)

