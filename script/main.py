import typer
import yaml
import socket
import requests
import json


IP = socket.gethostbyname(socket.gethostname())

apiUrl = "http://127.0.0.1:8000"



def main():

    credentials = {
        "email": "hz_haddad@esi.dz",
        "password": "12345678"
    }

    response = requests.post(apiUrl + '/login', data=json.dumps(credentials))
    user = response.json()

    print(user)

   


if __name__ == "__main__":
    main()
