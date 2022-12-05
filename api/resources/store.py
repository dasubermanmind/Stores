import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db.db import stores, items


blp = Blueprint('stores', __name__, description='Operations on Stores')

class Store(MethodView):
    
    @blp.route('/store/<string:store_id>')
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError as e:
            abort(404, message="Store not found")
    
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")
