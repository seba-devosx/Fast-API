
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

##creacion de tablas desde python
users =Table("Usuario",meta,
    Column("Usuario_id",String(32)),
    Column("Usuario_nombre",String(50)),
    Column("Usuario_edad",Integer()),
    Column("Usuario_apellido",String(50)),
    Column("Usuario_rut",String(13)))

meta.create_all(engine)