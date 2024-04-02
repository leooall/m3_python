import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response)#<Response [200]>

if response.status_code == 200:
    print("obtencion correcta")
    print(response.json())
    print("")
    print(response.json()["title"])
else:
    print("error en la solicitud")