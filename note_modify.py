import os
import json

def delete_data(note_id):
    os.remove(f"notes/note_{note_id}.json")


def edite(note):
    id = note ["Id"]
    with open(f"notes/note_{id}.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(note, indent=4, ensure_ascii=False))