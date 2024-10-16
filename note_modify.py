import os

def delete_data(note_id):
    os.remove(f"notes/note_{note_id}.json")