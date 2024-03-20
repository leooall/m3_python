
from string import ascii_lowercase

contrasena = input("Ingrese la contraseña: ").lower()# la convertimos a minúsculas.
    
# Inicializamos el conjunto de letras con todas las letras minúsculas del alfabeto.
letras = ascii_lowercase
intentos = 0
    
    # Iteramos sobre cada letra de la contraseña ingresada por el usuario.
for letra in contrasena:
  for intento in letras:# Iteramos sobre cada letra del alfabeto.
    intentos += 1# Incrementamos el contador de intentos en cada iteración.
    if intento == letra:# Si encontramos la letra de la contraseña en el conjunto de letras,
      break# salimos del bucle interno.

    print(f"La contraseña fue forzada en {intentos} intentos.")