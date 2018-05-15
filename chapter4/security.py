from user import User

users = [
    User("Kuba", 1, "aaa")
]

name_to_user = {u.username: u for u in users}
id_to_user = {u.id: u for u in users}


def authenticate(username, password):
    u = name_to_user.get(username, None)
    if u and u.password == password:
        return u


def identity(payload):
    user_id = payload['identity']
    return id_to_user.get(user_id, None)