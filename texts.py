import json as j

with open("texts.json", encoding='utf-8') as json_data:
    texts = j.load(json_data)["kz"]
