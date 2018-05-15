from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt import jwt_required, JWT

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "my_secret_key"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    put_post_parser = reqparse.RequestParser()
    put_post_parser.add_argument(name='price', required=True, type=float)

    @jwt_required()
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        data = request.get_json()
        item = {"name": name, "price": data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        data = Item.put_post_parser.parse_args()

        matching_items = list(filter(lambda x: x['name'] == name, items))
        if matching_items:
            for item in matching_items:
                item['price'] = data['price']
        else:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        return item

    def delete(self, name):
        items = filter(lambda x: x['name'] != name, items)
        return {'message': 'item deleted'}


class Items(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
app.run(port=5000, debug=True)
