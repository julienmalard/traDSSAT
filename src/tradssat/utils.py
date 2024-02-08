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
DSSAT_EXE = 'DSSAT_EXE'
config = {DSSAT_DIR: None, DSSAT_EXE: None}


def set_dssat_dir(dssat_dir):
    if os.path.isdir(dssat_dir):
        config[DSSAT_DIR] = dssat_dir
    else:
        raise FileNotFoundError(dssat_dir)


def get_dssat_dir():
    return config[DSSAT_DIR]


def get_dssat_exe():
    exe = config[DSSAT_EXE]
    dssat_root = get_dssat_dir()
    if not dssat_root:
        raise FileNotFoundError("DSSAT root folder is not defined. Define it with `set_dssat_dir()`.")

    # If path was relative, make absolute
    if exe and not os.path.isabs(exe):
        exe = os.path.join(dssat_root, exe)

    # If executable not specified, try to find default file
    if not exe:
        try:
            # Check for default EXE file name
            dssat_version = int(dssat_root[-2:])
            default_exe_path = os.path.join(dssat_root, f"DSCSM0{dssat_version}.EXE")
            if os.path.isfile(default_exe_path):
                exe = default_exe_path
        except ValueError:
            # If that doesn't work, check for any .exe file
            files_in_dssat = [os.path.join(dssat_root, f) for f in os.listdir(dssat_root) if
                              os.path.isfile(os.path.join(dssat_root, f))]
            try:
                exe = next(f for f in files_in_dssat if os.path.splitext(f)[1].upper() == '.EXE')
            except StopIteration:
                pass

    # If we've found something, make sure it exists
    if exe and not os.path.isfile(exe):
        raise FileNotFoundError(exe)

    return exe
