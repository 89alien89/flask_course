from chapter6.resources.ItemListResource import ItemListResource
from chapter6.resources.UserResource import UserResource
from chapter6.resources.ItemResource import ItemResource
from chapter6.resources.StoreResource import StoreResource
from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from chapter6.security import authenticate, identity
from chapter6.db import db


app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'


@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api = Api(app)
api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(ItemListResource, '/items')
api.add_resource(UserResource, '/register')
api.add_resource(StoreResource, '/store/<string:name>')

db.init_app(app)

app.run(port=5000, debug=True)
