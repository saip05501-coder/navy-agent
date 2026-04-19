import json
import os

FILE_PATH = "data/notifications.json"

def load_old_data():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    os.makedirs("data", exist_ok=True)

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def get_changes(old, new):
    old_map = {item["title"]: item for item in old}

    changed_items = []

    for item in new:
        title = item["title"]

        match = None
        for old_title in old_map:
            if title[:50] in old_title or old_title[:50] in title:
                match = old_map[old_title]
                break

        if match:
            if match["title"] != title:
                changed_items.append({
                    "old": match["title"],
                    "new": title,
                    "link": item["link"]
                })
        else:
            changed_items.append({
                "old": "NEW ENTRY",
                "new": title,
                "link": item["link"]
            })

    return changed_items