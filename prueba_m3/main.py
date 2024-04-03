import templates
from api_get import request_get

url = "https://aves.ninjas.cl/api/birds"
response = request_get(url)

cadena = ""

for dicc in response:
    print(dicc["name"]["spanish"], dicc["name"]["english"], dicc["images"]["full"])
    cadena = cadena + templates.body.substitute(titulo_esp= dicc["name"]["spanish"],
                           titulo_en= dicc["name"]["english"],
                           url_img_full= dicc["images"]["full"])
    
file = open("aves_de_chile.html", "w")
message = templates.template.substitute(contenido= cadena)
file.write(message)