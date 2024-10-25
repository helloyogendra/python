import os
import uuid
from flask import Flask, request, abort
from db import items, stores

clear = lambda : os.system("cls")
clear()

app = Flask(__name__)

@app.get("/")
def home():
    return "<h1><p> Flask </p></h1>"

@app.get("/store")
def get_all_stores():
    return {"stores" : list(stores.values())}


@app.get("/item")
def get_all_items():
    return {"items" : list(items.values())}


@app.post("/store")
def create_store():
    data = request.get_json()
    if data['id'] not in stores:
        abort(404, "Store not found")

    id = uuid.uuid4().hex
    store = {**data, "id" : id}

    stores[id] = store
    return store, 201


@app.post("/item")
def create_item(name):
    data = request.get_json()

    if data['id'] not in stores:
        return {"message": "Store not found"}, 404

    id = uuid.uuid4().hex
    item = {**data, "id" : id}
    items[id] = item

    return item, 201


    
@app.get("/data/<string:id>")
def get_store_by_id(id):
    try:
        return stores[id]
    except KeyError as ex:
        return {"error : ", ex}, 404


@app.get("/data/<string:id>")
def get_item_by_id(id):
    try:
        return items[id]
    except KeyError as ex:
        return abort(404, "Store not found")



#
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)