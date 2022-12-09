import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores, items


blp = Blueprint('stores', __name__, description='Operations on Stores')

class Store(MethodView):
    
    @blp.route('/store/<string:store_id>')
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError as e:
            abort(404, message="Store not found")
    
    @blp.route('/store/<string:store_id>')
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
            

class Item(MethodView):
    @blp.route('/item/<string:item_id>')
    def get(self, item_id):
        try:
            return stores[item_id]
        except KeyError as e:
            abort(404, message="Item not found")
    
    @blp.route('/item/<string:item_id>')
    def delete(self, item_id):
        try:
            del stores[item_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
