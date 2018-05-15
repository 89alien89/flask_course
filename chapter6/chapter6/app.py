from chapter6.resources.ItemListResource import ItemListResource
from chapter6.resources.UserResource import UserResource
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api
from security import authenticate, identity

from chapter6.resources.ItemResource import ItemResource

app = Flask(__name__)
app.secret_key = "my_secret_key"
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemListResource, '/items')
api.add_resource(UserResource, '/register')
app.run(port=5000, debug=True)
