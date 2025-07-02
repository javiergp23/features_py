from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Entidad User

class User(BaseModel):
    id: int
    name: str
    age: int


users_list = [User(id=1, name="Javier", age=30), 
         User(id=2, name="Pedro", age=25), 
         User(id=3, name="Carlos", age=35)]

@app.get("/users")
async def usersJson():
    return  [
        {"name": "Javier", "age": 30},
        {"name": "Pedro", "age": 25},
        {"name": "Carlos", "age": 35}
    ]

@app.get("/userclass")
async def userClass():
    return users_list


#path
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
#query
@app.get("/userquery/")
async def userQuery(id: int):
    user = filter(lambda user: user.id == id, users_list)
    try:
        return list(user)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}