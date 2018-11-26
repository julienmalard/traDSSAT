import json
import os
from copy import deepcopy

import numpy as np
from chardet import UniversalDetector


def write_json(obj, file):
    obj = deepcopy(obj)
    jsonify(obj)
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def read_json(file):
    with open(file, 'r', encoding='utf-8') as f:
        return json.load(f)


def jsonify(d):
    for k, v in d.items():
        if isinstance(v, np.ndarray):
            d[k] = v.tolist()
        elif isinstance(v, dict):
            jsonify(v)
        elif isinstance(v, list):
            for i in v:
                jsonify(i)


def detect_encod(file):
    detector = UniversalDetector()
    with open(file, 'rb') as d:
        for i, line in enumerate(d.readlines()):

            detector.feed(line)

            if detector.done:
                break

    detector.close()

    return detector.result['encoding']


config = {'DSSAT_DIR': None}


def set_dssat_dir(dssat_dir):
    if os.path.isdir(dssat_dir):
        config['DSSAT_DIR'] = dssat_dir
    else:
        raise FileNotFoundError(dssat_dir)


def get_dssat_dir():
    return config['DSSAT_DIR']
