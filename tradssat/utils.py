import os

from chardet import UniversalDetector


def read_txt(f):
    with open(f, 'r', encoding='UTF-8') as d:
        return d.read()


def detect_encod(file):
    detector = UniversalDetector()
    with open(file, 'rb') as d:
        for line in d.readlines():

            detector.feed(line)

            if detector.done:
                break

    detector.close()

    return detector.result['encoding']


DSSAT_DIR = 'DSSAT_DIR'
config = {DSSAT_DIR: None}


def set_dssat_dir(dssat_dir):
    if os.path.isdir(dssat_dir):
        config[DSSAT_DIR] = dssat_dir
    else:
        raise FileNotFoundError(dssat_dir)


def get_dssat_dir():
    return config[DSSAT_DIR]
