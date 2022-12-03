import uuid
from flask import Flask, request
from db.db import stores, items

app = Flask(__name__)

# app decorator registers the endpoint with the HTTP verb at the specific endpoint
@app.get("/store")
def get_stores():
    return {'stores': list(stores.values())}

@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uuidv4().hex
    store = {**store_data, "id": store_id}
    stores[store_id] = store
    return store


@app.get("/store/<string:id>")
def get_store(id):
    try:
        return stores[id]
    except KeyError as e:
        return {"message": "store not found"}
    

@app.post("/store")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item

@app.get('/items')
def get_items():
    return {"items": list(items.values())}


@app.get("/item/<string:item_id>")
def get_item(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "Item not found"}, 404
    
@app.post("/item")
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        return {"message": "Store not found"}, 404

    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item
    
    
