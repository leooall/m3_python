#PROFE; PARA PODER REALIZAR ESTA PRUEBA, RECURRI A LA IA DESDE LA LINEA 13 EN ADELANTE. ESTUVO DIFICIL PARA MI

import requests  # Importamos la librería requests para realizar solicitudes HTTP
from string import Template  # Importamos Template de la librería string para generar el HTML

url = "https://aves.ninjas.cl/api/birds"  # URL de la API de aves de Chile

payload = {}  
headers = {}  

response = requests.request("GET", url, headers=headers, data=payload)  # Realizamos una solicitud GET a la API

# Plantilla HTML que contiene un marcador de posición para la lista de aves
html_template = """
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Aves de Chile</title>
</head>
<body>
    <h1>Aves de Chile</h1>
    <ul>
        ${bird_list}  # Aquí se va a sustituir con la lista de aves
    </ul>
</body>
</html>
"""  
# Plantilla para un elemento de ave en la lista, con marcadores de posición para el nombre en español, nombre en inglés y URL de la imagen
bird_template = """
<li>
    <h2>${name_es}</h2>
    <p><em>${name_en}</em></p>
    <img src="${url}" alt="${name_es}">
</li>
"""  

bird_list = ""  # lista de aves vacia

for bird in response.json():  # Iteramos sobre cada ave en la respuesta JSON de la API
    try:
        # Intentamos sustituir los marcadores de posición en la plantilla de ave con los datos reales
        bird_list += Template(bird_template).substitute(name_es=bird['name']['spanish'], 
                                                        name_en=bird['name']['english'],
                                                        url=bird['image']
                                                        )
    except KeyError as e:
        # Si hay un error al acceder a las claves en el diccionario del ave, imprimimos un mensaje de error
        print(f"Error: No se puede acceder a la clave {e} para el ave: {bird}")

# Sustituimos el marcador de posición de la lista de aves en la plantilla HTML con la lista de aves generada
html_content = Template(html_template).substitute(bird_list=bird_list)

# Guardamos el contenido HTML en un archivo llamado "aves_de_chile.html"
with open("aves_de_chile.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("El sitio web se ha exportado correctamente como 'aves_de_chile.html'")  # Imprimimos un mensaje de confirmación

