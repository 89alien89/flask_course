import sqlite3


class ItemModel(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name": self.name, "price": self.price}

    def insert(self):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "INSERT INTO items VALUES (null, ?, ?)"
        cursor.execute(query, (self.name, self.price))
        conn.commit()
        conn.close()

    def update(self):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (self.price, self.name))
        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "DELETE FROM items WHERE name = ?"
        cursor.execute(query, (self.name, ))
        conn.commit()
        conn.close()

    @classmethod
    def get_item_by_name(cls, name):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        res = cursor.execute(query, (name, )).fetchone()

        ret = None
        if res:
            ret = ItemModel(res[1], res[2])
        return ret

    @classmethod
    def get_items(cls):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        query = "SELECT * FROM items"
        res = cursor.execute(query)

        items = []
        for row in res:
            items.append(ItemModel(row[1], row[2]))
        conn.close()
        return items