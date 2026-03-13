import json

FILE_PATH = "data.json"

def load_data():
    try:
        file = open(FILE_PATH, "r", encoding="utf-8")
        data = json.load(file)
        file.close()
        return data
    except:
        return {"orders": []}

def save_data(data):
    try:
        file = open(FILE_PATH, "w", encoding="utf-8")
        json.dump(data, file)
        file.close()
    except:
        print("error")
