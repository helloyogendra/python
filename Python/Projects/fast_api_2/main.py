import os
from enum import Enum
from fastapi import FastAPI


app = FastAPI()


# @app.get(), @app.post(), @app.put(), @app.delete(), 
# @app.options(), @app.head(), @app.patch(), @app.trace()


@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}


# valid url - http://127.0.0.1:8000/items/101
# valid url  http://127.0.0.1:8000/items/book
@app.get('/items/{item_id}')
async def read_item1(item_id):
    print("itme id is = ", item_id)
    return {'item_id' : item_id}


# 'int' type is fixed
# now valid url is only like - http://127.0.0.1:8000/items/101
@app.get('/books/{item_id}')
async def read_item2(item_id: int):
    return {'item_id' : item_id}


#oder is important

# 1
# This should come first
@app.get('/users/me')
async def read_user_me():
    return {'user_id' : os.getlogin()}


# 2
@app.get('/users/{user_id}')
async def read_user_me(user_id: str):
    return {'user_id' : user_id}


# 3
@app.get('/users')
async def read_users():
    return ['Rob', 'Bob', 'Tom']
    


class ModelName(str, Enum):
    one = 'one'
    two = 'two',
    three = 'three'


@app.get('/models/{model_name}')
async def get_model(model_name : ModelName):
    if model_name is ModelName.one:
        return {"model_name" : model_name, 'message' : 'Deep Learning'}
    if model_name is ModelName.two:
        return {'model_name' : model_name, 'messgae' : 'Machine Learning'}
    
    return {'model_name' : model_name, 'messgae' : 'Cyber Learning'}



@app.get('files/{file_path}')
async def read_file(file_path: str):
    return {"file_path": file_path}


fake_items_db = [
    { "item1" : "fuzz", "item2" : "chocks", "item3" : "cream"},
    { "fruit1" : "apple", "fruit2" : "cherry", "fruit3" : "kiwi"},
    { "soup1" : "manchow", "soup2" : "veg", "soup3" : "lemon"},
    ]


@app.get("/items/")
async def read_items(skip: int=0, limit: int=10):
    print(f"query params are - skip = {skip} & limit = {limit}")
    return fake_items_db[skip: skip + limit]