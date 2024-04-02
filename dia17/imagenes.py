import requests
from string import Template

url = "https://aves.ninjas.cl/api/birds"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

html_template = """
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Aves de Chile</title>
</head>
<body>
    <h1>Aves de Chile</h1>
    <ul>
        ${bird_list}
    </ul>
</body>
</html>
"""

bird_template = """
<li>
    <h2>${name_es}</h2>
    <p><em>${name_en}</em></p>
    <img src="${url}" alt="${name_es}">
</li>
"""

bird_list = ""
for bird in response.json():
    bird_list += Template(bird_template).substitute(bird)
    
html_content = Template(html_template).substitute(bird_list=bird_list)

# contenido HTML en un archivo
with open("aves_de_chile.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("El sitio web se ha exportado correctamente como 'aves_de_chile.html'")

