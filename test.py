
import re
from unicodedata import name
from wsgiref.util import request_uri
from fastapi import FastAPI,Query
from typing import Union, Optional
from faker import Faker
from pydantic import BaseModel
from fastapi import Body
import uuid
myuuid= uuid.uuid4()
app = FastAPI()
faker =Faker()
#comando para poder iniciar la api uvicorn main:app --reload
#link para poder ingresar a la documetacion http://127.0.0.1:8000/docs
#link para poder ingresar a la documentacion http://127.0.0.1:8000/redoc
# se importa pydantyc
# creacion de modelo en caso de que se quiren pasar parametro via post 
#se importa body para indicar que en l;a funcion se devolvera un modelo

#base model modelo para poder hace uso de body como parametro, los datos opcionales
#se puede o no agregar informaciojn, no dara error al respecto
class Persona(BaseModel):
    id:str
    nombre:str
    apellido:str
    Edad:int
    estado_civil:Optional[bool]=None
#ejemplo de path operation, la se mostrara al iniciar la api
#el arroba es un decorador
@app.get("/")
def read_root():
    return {"Hello": "World"}

#se espera un json como parametro el cual si no se envia se generara error
# ... significa que un atributo es obligatorio
@app.post("/Persona/new")
def personas(persona:Persona=Body(...)):
    return persona

@app.get("/users_info")
def read_root():
    names=[]
    for _ in range(10):
        names.append(
            {"name": faker.name(),
            "address":faker.address(),
            "comment": faker.text()
            
            })
    return names


# valor obtenido por parametro debe ser int para que este no retorne error 
@app.get("/params_int/{item}")
async def read_item(item:int):
        return{"parametro obtenido":item}

@app.get("/params_ints/{item}")
async def read_item(item:float):
        return{"parametro obtenido":item}

#query parameter parametros opcionales dntro de un endpoint
#parametros opcionales empiezan con el siguiente signo ? y si hay mas de uno se concatenan
#mediante & https://platzi.com/search/?search=Python&filter=material-lecture
@app.put("/user/{user_id}/details?age=20&weight=190")
def user_data(user_id:int):
    return{"parametros":user_id}

# valor pasado por paramaetro no es decriminado dependiendo del tipo de dato 
@app.get("/params_string/{item}")
def read_item(item):
    return {"parametro obtenido":item}

# si se ingresa un skip de 0 y esta definido un limit de 5 solo se mostraran 5 elemento, si se defiene 10 en el limit se definiran 10
@app.get("/items/")
async def read_item(skip: int = 1, limit: int = 2):
    names=[]
    for _ in range(10):
        names.append(
            {"name": faker.name(),
            "address":faker.address(),
            "comment": faker.text()
            
            })
    return names[skip : skip + limit]

#Query parameter, realizacion de validaciones dentro del envio de informacion de api pasada por paramet24ro
@app.get('/user_info/valid')
async def valid_data(
    Nombre: Optional[str] = Query(None,min_length=1,max_length=15),
    Edad: int =Query(...),
    
):
    return{
        "nombre":Nombre,
        "edad":Edad,
        "id": myuuid
    }
