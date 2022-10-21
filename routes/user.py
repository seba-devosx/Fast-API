from fastapi import APIRouter
from config.db import conn
from model.users import users
from schemas.user_model import User
from sqlalchemy import insert
import uuid



user= APIRouter()

##aca se definen las rutas

#esta ruta mostrara los usuarios, realiza un fetch all
@user.get("/users")
def home():
    return  conn.execute(users.select()).fetchall()

#esta alamcenara los usuarios en la tabala creada
@user.post("/users_insert")
def insert_user(user:User):
    myuuid= uuid.uuid4()
    new_user={"Usuario_id":str(myuuid),
              "Usuario_nombre":user.Usuario_nombre,
              "Usuario_apellido":user.Usuario_apellido,
              "Usuario_edad":user.Usuario_edad,
              "Usuario_rut":user.Usuario_rut}
    
    conn.execute(users.insert().values(new_user))
    return  conn.execute(users.select()).fetchall()


@user.get("/user_getBy_Id")
def set_user(user:User):
    return{}    