import json


def get_topics(subject):
    file_path = f"data/structure/{subject}_structure.json"

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["topics"]


def get_topic_key(subject, topic):
    topic = topic.lower().replace(" ", "_")
    return f"{subject}-{topic}"
