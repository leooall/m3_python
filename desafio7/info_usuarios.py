print("***********requerimiento 1************")
import requests

import json
url = "https://reqres.in/api/users"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print(response)
#se crea la variable users_data  para almacenar los datos del request
users_data = response.text
print(users_data)

print("***********requerimiento 2************")
#se agrega informacion usando metodo post 
url = "https://reqres.in/api/users"

payload = json.dumps({
    "data": {
    "first_name": "Ignacio",
    "trabajo": "Profesor"
}
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response)
#se crea la variable created_user para almacenar el contenido de response.text
created_user = response.text
print(created_user)

print("**********requerimiento 3*************")

url = "https://reqres.in/api/users/1"
#se remplazan datos del  usuario con id 1 por nueva info
payload = json.dumps({
"data": {
    "id": 1,
    "first_name": "morpheus",
    "residence": "zion"
}
})
headers = {
'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response)

updated_user =  response.text
print(updated_user)

print("**********requerimiento 4*************")

url = "https://reqres.in/api/users/6"

payload = {}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print("Código de respuesta:", response.status_code)