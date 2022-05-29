import typer
import socket
import requests
import json


IP = socket.gethostbyname(socket.gethostname())
API_URL = "http://127.0.0.1:8000"

app = typer.Typer()


class Deployment:
    def __init__(self, name, label, ip):
        self.name = name
        self.label = label
        self.ip = ip


@app.command()
def login():

    email = typer.prompt("E-mail")
    password = typer.prompt("Password", hide_input=True)

    credentials = {
        "email": email,
        "password": password
    }

    response = requests.post(API_URL + '/login', data=json.dumps(credentials))

    if response.status_code != 200:
        typer.secho("Invalid credentials", fg="red")
        return

    user = response.json()

    typer.secho("Login successfull", fg="green")
    typer.secho("Starting Packet tracer please wait ... ", fg="green")

    deployment = Deployment(
        user['username'], user['username'], IP).__dict__
    requests.post(API_URL + '/run-deployment', data=json.dumps(deployment))


@app.command()
def registre():

    email = typer.prompt("E-mail")
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)

    credentials = {
        "email": email,
        "username": username,
        "password": password

    }

    response = requests.post(API_URL + '/register',
                             data=json.dumps(credentials))

    if response.status_code != 201:
        typer.secho("Invalid credentials", fg="red")
        return

    typer.secho("Register successfull", fg="green")


if __name__ == "__main__":
    app()
