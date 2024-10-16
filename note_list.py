from datetime import datetime as DT
import os
import json

json_dict = {}

def note_list():
    print('Вывожу список заметок: \n')
    directory = "notes"
    files = os.listdir(directory)
    json_array = []
    for i, v in enumerate(files):
        with open(f"notes/{v}", "r") as f:
            capitals_json = f.read() 
            templates = json.loads(capitals_json)
            json_array.append(templates)

    json_array_sorted = sorted(json_array, key=get_date, reverse=True)
    
    for i, v in enumerate(json_array_sorted):
        n = i+1
        title = v["Title"]
        json_dict[f"{n}"] = v
        print(f"{n} - {title}")

def get_date(x, format="%Y-%m-%d %H:%M:%S.%f"):
    return DT.strptime(x.get("Date"), format)

def get_note(note):
    try:
        return json_dict[note]
    except KeyError as e:
        return "0"
    
def get_note_id(note):
    return note["Id"]