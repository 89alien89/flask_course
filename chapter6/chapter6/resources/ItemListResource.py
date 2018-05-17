from chapter6.models.ItemModel import ItemModel
from flask_restful import Resource


class ItemListResource(Resource):
    def get(self):
        return [item.json() for item in ItemModel.get_items()]