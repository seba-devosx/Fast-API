from fastapi import FastAPI
from routes.user import user

#main de la api 
app=FastAPI()
app.include_router(user)

