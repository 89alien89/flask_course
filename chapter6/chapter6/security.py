from chapter6.models.UserModel import UserModel


def authenticate(username, password):
    u = UserModel.get_user_by_name(username)
    print(u.json())
    if u and u.password == password:
        return u


def identity(payload):
    user_id = payload['identity']
    return UserModel.get_user_by_id(user_id)