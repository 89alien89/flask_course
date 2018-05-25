from flask_restful import Resource, reqparse
from chapter6.models.StoreModel import StoreModel


class StoreResource(Resource):

    def get(self, name):
        store = StoreModel.get_store_by_name(name)
        if not store:
            return {'store': None}, 404
        return store.json()

    def post(self, name):
        store = StoreModel.get_store_by_name(name)
        if store:
            return "Store with that name already exists", 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.get_store_by_name(name)
        if not store:
            return "Store not found", 404
        store.delete()
        return "Store deleted"
