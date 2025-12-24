import json
import os

USER_FILE = "data/users/users.json"

def load_users():
    os.makedirs("data/users", exist_ok=True)

    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w") as f:
            json.dump({}, f)

    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password):
    users = load_users()

    if username in users:
        return False  # user already exists

    users[username] = {"password": password}
    save_users(users)
    return True

def authenticate_user(username, password):
    users = load_users()
    return username in users and users[username]["password"] == password

def reset_password(username, new_password):
    users = load_users()

    if username not in users:
        return False

    users[username]["password"] = new_password
    save_users(users)
    return True
