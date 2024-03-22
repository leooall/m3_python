#metodo para importar archivo.txt  
with open("lorem_ipsum.txt", "r") as file:
    texto  = file.read() #se guarda el texto en una variable
    
#set()crea un objeto set a partir de una secuencia iterable (como una cadena de texto), eliminando automáticamente los elementos duplicados. 
#La función len() luego devuelve el número de elementos únicos en el set    
caracteres_distintos = len(set(texto)) 

#el método split() divide el texto en palabras usando como separador el espacio en blanco. El resultado es una lista de palabras
palabras_distintas = len(set(texto.split()))


print(f"El numero de caracteres distinto es: {caracteres_distintos}")
print(f"El numero de palabras distintas es: {palabras_distintas}")
