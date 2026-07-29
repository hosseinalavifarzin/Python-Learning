import json
def load_users():
    try:
        with open("data/users.json", "r") as file:
            users = json.load(file)
            return users
    except FileNotFoundError:
        return []

def save_users(users):
    with open("data/users.json", "w") as file:
        json.dump(users, file, indent=4)