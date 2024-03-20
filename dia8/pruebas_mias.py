for i in range (1, 10, 3) :
    print(i)

print("")
texto = "hola mundo"
for caracter in texto:
    print(caracter)
    
print("")

diccionario = {" Nombre" : "leo",
                "Apellido" : "llaupe",
                "Ocupación" : "kine"}
for clave, valor in diccionario.items():
    print(f"Mi { clave } es {valor}")
    
print("")

texto = "esternocleidomastoideo"
for po, let in enumerate(texto) :
    print(f"la letra en la posicion {po} es la {let}")