import json
import os

FILE = "data/weakness.json"


def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


# ADD WEAKNESS
def add_weakness(user, subject, topic):
    data = load_data()

    if user not in data:
        data[user] = {}

    key = f"{subject}-{topic}"

    data[user][key] = data[user].get(key, 0) + 1

    save_data(data)


# GET ALL WEAKNESS
def get_weakness(user):
    data = load_data()
    return data.get(user, {})


# TOTAL COUNT
def get_total_weakness(user):
    weak = get_weakness(user)
    return sum(weak.values())


# REDUCE
def reduce_weakness(user, topic_key):
    data = load_data()

    if user in data and topic_key in data[user]:
        data[user][topic_key] -= 1

        if data[user][topic_key] <= 0:
            del data[user][topic_key]

    save_data(data)


def get_most_weak_topic(user):

    data = load_data()

    if user not in data or not data[user]:
        return None, 0

    weakest = max(data[user], key=data[user].get)
    count = data[user][weakest]

    return weakest, count


def reduce_weakness(user, subject, topic):
    data = load_data()

    if user in data and subject in data[user]:
        if topic in data[user][subject]:
            data[user][subject][topic] -= 1

            # 🔥 negative ஆக போகக்கூடாது
            if data[user][subject][topic] <= 0:
                del data[user][subject][topic]

    save_data(data)
