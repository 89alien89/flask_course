from user import User, get_user_by_name, get_user_by_id


def authenticate(username, password):
    u = get_user_by_name(username)
    if u and u.password == password:
        return u


def identity(payload):
    user_id = payload['identity']
    return get_user_by_id(user_id)