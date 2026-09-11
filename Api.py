from fastapi import FastAPI
from Case import UserManger

app = FastAPI()

manager = UserManger()

@app.get("/users")
def get_users():
    return manager.show_all_users()

@app.get("/users/search_userID")
def search_UserName(id:int):
    return manager.search_userID(id) 

@app.get("/users/search_UserName")
def search_userID(name:str):
    return manager.search_UserName(name) 

@app.post("/users")
def add_users(name:str,age:int):
    return manager.add_user(name,age)

@app.delete("/delete_user")
def add_users(name:str,age:int):
    return manager.delete_user(name,age)

@app.put("/update_user")
def update_user(
    name: str,
    age: int,
    new_name: str,
    new_age: int
):
    return manager.update_user(name, age, new_name, new_age)






