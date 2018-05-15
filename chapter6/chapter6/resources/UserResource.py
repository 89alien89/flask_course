from flask_restful import Resource, reqparse
from models.UserModel import UserModel


class UserResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='username', required=True, type=str)
        parser.add_argument(name='password', required=True, type=str)

        data = parser.parse_args()
        if UserModel.get_user_by_name(data['username']):
            return {'message': "The user with this username already exists"}, 400
        user = UserModel(None, data['username'], data['password'])
        user.insert()

        return {'message': 'User created', 'user': user.json()}, 201