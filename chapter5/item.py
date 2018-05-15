from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3

items = []


class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return {"name": self.name, "price": self.price}


class ItemResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(name='price', required=True, type=float)

    @classmethod
    def get_item_by_name(cls, name):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        res = cursor.execute(query, (name, ))

        items = []
        for row in res:
            items.append(Item(row[1], row[2]))
        conn.close()
        return items

    @jwt_required()
    def get(self, name):
        items = self.get_item_by_name(name)
        if not items:
            return {'items': None}, 404
        return [i.to_dict() for i in items]

    @classmethod
    def add_item_to_db(cls, item):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "INSERT INTO items VALUES (null, ?, ?)"
        cursor.execute(query, (item.name, item.price))
        conn.commit()
        conn.close()

    @classmethod
    def update_item_in_db(cls, item):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (item.price, item.name))
        conn.commit()
        conn.close()

    def post(self, name):
        data = self.parser.parse_args()
        items = self.get_item_by_name(name)
        if items:
            return "Item with that name already exists", 400
        item = Item(name, data['price'])
        self.add_item_to_db(item)
        return item.to_dict(), 201

    def put(self, name):
        data = self.parser.parse_args()
        item = Item(name, data['price'])
        items = self.get_item_by_name(name)
        if not items:
            self.add_item_to_db(item)
            return item.to_dict(), 201
        self.update_item_in_db(item)
        return item.to_dict()

    @classmethod
    def delete_item_from_db(cls, name):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (name, ))
        conn.commit()
        conn.close()

    def delete(self, name):
        items = self.get_item_by_name(name)
        if not items:
            return "Item not found", 404
        self.delete_item_from_db(name)
        return "Item deleted"


class ItemList(Resource):
    def get(self):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "SELECT * FROM items"
        res = cursor.execute(query)

        items = []
        for row in res:
            items.append(Item(row[1], row[2]).to_dict())
        conn.close()
        return items
