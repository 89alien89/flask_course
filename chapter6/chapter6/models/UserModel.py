import sqlite3


class UserModel(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def json(self):
        return {'username': self.username, 'password': self.password}

    def insert(self):
        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute(query, (self.username, self.password))

        conn.commit()
        conn.close()

    @classmethod
    def get_user_by_name(cls, name):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        res = cursor.execute('select * from users where username = ?', (name,)).fetchone()
        conn.close()
        ret = None
        if res:
            ret = UserModel(*res)
        return ret

    @classmethod
    def get_user_by_id(cls, id):
        conn = sqlite3.Connection('users.db')
        cursor = conn.cursor()
        res = cursor.execute('select * from users where id = ?', (id,)).fetchone()
        conn.close()
        ret = None
        if res:
            ret = UserModel(*res)
        return ret





