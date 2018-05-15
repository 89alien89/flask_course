from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)


class Product(Resource):
    def json(self):
        return {'name': self.name, 'price': self.price}

    def get(self, name):
        prod = products.get(name, None)
        if not prod:
            return "Product not found", 404
        return prod

products = {"piano": ['piano', '20']}
api = Api(app)
api.add_resource(Product, '/product/<string:name>')

app.run(port=8000, debug=True)