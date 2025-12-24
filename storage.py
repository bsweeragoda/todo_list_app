import json
import os

BASE_PATH = "data/users"

def load_tasks(username):
    path = f"{BASE_PATH}/{username}_tasks.json"
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        return json.load(f)

def save_tasks(username, tasks):
    os.makedirs(BASE_PATH, exist_ok=True)
    path = f"{BASE_PATH}/{username}_tasks.json"
    with open(path, "w") as f:
        json.dump(tasks, f, indent=4)
