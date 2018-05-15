from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.ItemModel import ItemModel


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(name='price', required=True, type=float)

    @jwt_required()
    def get(self, name):
        item = ItemModel.get_item_by_name(name)
        if not item:
            return {'item': None}, 404
        return item.json()

    def post(self, name):
        data = self.parser.parse_args()
        item = ItemModel.get_item_by_name(name)
        if item:
            return "Item with that name already exists", 400
        item = ItemModel(name, data['price'])
        item.insert()
        return item.json(), 201

    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel(name, data['price'])
        existing_item = ItemModel.get_item_by_name(name)
        if not existing_item:
            item.insert()
            return item.json(), 201
        item.update()
        return item.json()

    def delete(self, name):
        item = ItemModel.get_item_by_name(name)
        if not item:
            return "Item not found", 404
        item.delete()
        return "Item deleted"
