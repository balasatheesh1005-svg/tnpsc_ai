import json
import os

FILE_PATH = "user_data.json"


# =========================
# LOAD ALL DATA
# =========================
def load_all_data():

    if not os.path.exists(FILE_PATH):
        return {}

    with open(FILE_PATH, "r") as file:
        return json.load(file)


# =========================
# SAVE ALL DATA
# =========================
def save_all_data(data):

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


# =========================
# SAVE SINGLE USER DATA
# =========================
def save_user_data(user, data):

    all_data = load_all_data()

    all_data[user] = data

    save_all_data(all_data)


# =========================
# LOAD SINGLE USER DATA
# =========================
def load_user_data(user):

    all_data = load_all_data()

    return all_data.get(user, {})
