import json
from copy import deepcopy

import numpy as np


def write_json(obj, file):
    obj = deepcopy(obj)
    jsonify(obj)
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def read_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        d = json.load(f)
    numpyfiy(d)
    return d

def jsonify(d):
    for k, v in d.items():
        if isinstance(v, np.ndarray):
            d[k] = v.tolist()
        elif isinstance(v, dict):
            jsonify(v)


def numpyfiy(d):
    for k, v in d.items():
        if isinstance(v, list):
            d[k] = np.array(v)
        elif isinstance(v, dict):
            jsonify(v)
