users = [
    {"username": "standard_user", "password": "secret_sauce"},
    {"username": "locked_out_user", "password": "secret_sauce"},
]


def get_user(name):
    try:
        return next(user for user in users if user["username"] == name)
    except:
        print("User %s is not valid" % name)


