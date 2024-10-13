from collect_data import title_data, body_data
import datetime as DT
import uuid
import json
import os

def create_note():
    title = title_data()
    body = body_data()
    date = str(DT.datetime.now())
    id = str(uuid.uuid1())
    data = {
        "Id": id,
        "Title": title,
        "Body": body,
        "Date": date
    }
    folder_path = 'notes'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(f"notes/note_{id}.json", "w", encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
 