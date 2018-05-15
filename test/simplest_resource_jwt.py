from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required

app = Flask(__name__)


class Product(Resource):
    def json(self):
        return {'name': self.name, 'price': self.price}

    @jwt_required()
    def get(self, name):
        prod = products.get(name, None)
        if not prod:
            return "Product not found", 404
        return prod

products = {"piano": ['piano', '20']}
api = Api(app)
api.add_resource(Product, '/product/<string:name>')


class User:
    def __init__(self, id):
        self.id = id


def authenticate(name, passwd):
    return User(name)


def identity(payload):
    return "ok"

app.secret_key = "secret_key"
jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)


app.run(port=8000, debug=True)