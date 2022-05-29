from typing import Union
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from pymongo import MongoClient
import bcrypt
app = FastAPI()


username = "username"
password = "password"
uri = 'mongodb://%s:%s@127.0.0.1' % (username, password)

client = MongoClient(uri)


class Login(BaseModel):
    email: str
    password: str


class Register(BaseModel):
    email: str
    username: str
    password: str


@app.post("/login", status_code=status.HTTP_200_OK)
def login(login: Login, response: Response):
    collection = client['packet-tracer'].users
    user = collection.find_one(login.__dict__)
    if user:
        return {
            'username': user['username'],
        }
    response.status_code = status.HTTP_401_UNAUTHORIZED


@app.post("/register/", status_code=status.HTTP_201_CREATED)
def register(register: Register):
    collection = client['packet-tracer'].users
    user = collection.insert_one(register.__dict__)
    if not user:
        response.status_code = status.HTTP_400_BAD_REQUEST
