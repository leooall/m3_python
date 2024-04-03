import requests
import json

def request_get(url):
    return json.loads(requests.get(url).text)


if __name__ == "__main__":
    url = "https://aves.ninjas.cl/api/birds"

    response = request_get(url)

    print(response)#<Response [200]>

    if response.status_code == 200:
        print("obtencion correcta")#"obtencion correcta"
        #print(response.json())
        print("")
        post = response.json()
        print(post[0])
    else:
        print("error en la solicitud")