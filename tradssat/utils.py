import json


def write_json(obj, file):
    with open(file, encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False)
