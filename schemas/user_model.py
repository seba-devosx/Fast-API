
from pydantic import BaseModel, Field


##modelo para el envio de informacion para usuarios
class User(BaseModel):
    Usuario_nombre: str = Field(...,min_length=1,max_length=50,example='jack')
    Usuario_apellido:str=Field(...,min_length=1,max_length=50,example='michels')
    Usuario_edad:int = Field(...,gt=0,le=115,example='25')
    Usuario_rut: str=Field(...,min_length=1,max_length=13,example='190987651')


