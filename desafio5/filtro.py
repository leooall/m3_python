import sys
# Diccionario de productos y precios
precios = {
    "Notebook": 700000,
    "Teclado": 25000,
    "Mouse": 12000,
    "Monitor": 250000,
    "Escritorio": 135000,
    "Tarjeta de Video": 1500000,
}
# Definición de la función de filtrado
def filtrar_productos(precios, umbral, operacion = "mayor"):
    if operacion not in ["mayor", "menor"]:
        return "Lo sentimos, no es una operación válida"

    productos_filtrados = []
    
    for producto, precio in precios.items():
        if (operacion == "mayor" and precio > umbral) or (operacion == "menor" and precio < umbral):
            productos_filtrados.append(producto)

    return productos_filtrados

# Comprobación del número de argumentos de la línea de comandos
if len(sys.argv) == 2:
    # Se proporciona un solo argumento, se asume que es el umbral y la operación es 'mayor' por defecto
    umbral = int(sys.argv[1])
    productos_filtrados = filtrar_productos(precios, umbral)
    print(f"Los productos con precios mayores al umbral son: {', '.join(productos_filtrados)}")
elif len(sys.argv) == 3:
    # Se proporcionan dos argumentos, el primero es el umbral y el segundo es la operación
    umbral = int(sys.argv[1])
    operacion = sys.argv[2].lower()
    productos_filtrados = filtrar_productos(precios, umbral, operacion)
    
    print(f"Los productos {operacion}es al umbral son: {', '.join(productos_filtrados)}")
