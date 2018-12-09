import json
import os
from copy import deepcopy
from json import JSONDecodeError
from tempfile import NamedTemporaryFile
from warnings import warn

import numpy as np
import numpy.testing as npt


def find_files(inp_class, folder):
    l_files = []
    for root, dirs, files in os.walk(folder):
        for f in files:
            if inp_class.matches_file(f):
                l_files.append(os.path.join(root, f))

    return l_files


def get_ref(file, default):
    path, file = os.path.split(file)
    file_name = os.path.splitext(file)[0]
    ref_file = os.path.join(path, '_ref_{}.json'.format(file))
    try:
        return read_json(ref_file)
    except (FileNotFoundError, JSONDecodeError):
        write_json(default, ref_file)
        warn('Reference generated for tmpl "{}". Check that its contents are correct.'.format(file_name))
        return default


def test_read(inp_class, folder, testcase):
    files = find_files(inp_class, folder)

    for f in files:
        with testcase.subTest(os.path.split(f)[1]):
            dict_vars = inp_class(f).to_dict()

            ref = get_ref(f, dict_vars)
            _test_dicts_equal(tc=testcase, act=dict_vars, ref=ref, f=f)


def test_write(inp_class, folder, testcase):
    ext = inp_class.ext
    files = find_files(inp_class, folder)

    for f in files:
        with testcase.subTest(os.path.split(f)[1]):
            if isinstance(ext, list):
                ext = ext[0]

            name = os.path.split(f)[1]

            temp_file = NamedTemporaryFile(prefix=name, suffix=ext).name
            inp_file_obj = inp_class(f)
            inp_file_obj.write(temp_file)

            new_file_obj = inp_class(temp_file)

            _test_dicts_equal(testcase, act=new_file_obj.to_dict(), ref=inp_file_obj.to_dict(), f=f)


def _test_dicts_equal(tc, act, ref, f, keys=None):
    if keys is None:
        keys = []
    if isinstance(act, dict):
        tc.assertListEqual(list(act), list(ref), msg='Dictionary keys are not equal in {}'.format(_f_loc(f, keys)))
        for k, v in act.items():
            keys.append(k)
            _test_dicts_equal(tc=tc, act=v, ref=ref[k], f=f, keys=keys)
            keys[:] = keys[:-1]
    elif isinstance(act, list):
        tc.assertEqual(len(act), len(ref), msg='List lengths not equal in {}'.format(_f_loc(f, keys)))
        for i, (a, r) in enumerate(zip(act, ref)):
            keys.append(i)
            _test_dicts_equal(tc=tc, act=a, ref=r, f=f, keys=keys)
            keys[:] = keys[:-1]
    elif isinstance(act, np.ndarray):
        if not len(act) == len(ref) == 0:  # skip empty arrays (which may have inferred different types)
            npt.assert_equal(actual=act, desired=ref, err_msg=_f_loc(f, keys))


def _f_loc(f, keys):
    return '{}\n\t{}'.format(f, ': '.join(str(k) for k in keys))


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