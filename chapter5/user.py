import sqlite3
from flask_restful import Resource, reqparse


def get_user_by_name(name):
    conn = sqlite3.Connection('users.db')
    cursor = conn.cursor()
    res = cursor.execute('select * from users where username = ?', (name,)).fetchone()
    conn.close()
    ret = None
    if res:
        ret = User(res[0], res[1], res[2])
    return ret


def get_user_by_id(id):
    conn = sqlite3.Connection('users.db')
    cursor = conn.cursor()
    res = cursor.execute('select * from users where id = ?', (id,)).fetchone()
    conn.close()
    ret = None
    if res:
        ret = User(res[0], res[1], res[2])
    return ret


class User(object):
    def __init__(self, user_id, username, password):
        self.username = username
        self.id = user_id
        self.password = password

    def __str__(self):
        return "({}, {}, {})".format(self.id, self.username, self.password)

    def __repr__(self):
        return self.__str__()


class UserResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name='username', required=True, type=str)
        parser.add_argument(name='password', required=True, type=str)

        data = parser.parse_args()
        if get_user_by_name(data['username']):
            return {'message': "The user with this username already exists"}, 400

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute(query, (data['username'], data['password']))

        conn.commit()
        conn.close()

        return {'message': 'User created'}, 201
