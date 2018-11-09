import os
from json import JSONDecodeError
from tempfile import NamedTemporaryFile
from warnings import warn

import numpy.testing as npt

from tradssat.utils import read_json, write_json


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
    ref_file = os.path.join(path, f'ref_{file}.json')
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

            for sect, l_sect in ref.items():
                for i, subsect in enumerate(l_sect):

                for var, val in subsect.items():
                    if len(val):
                        npt.assert_equal(dict_vars[sect][i][var], val, err_msg=f'{f}\n\t {sect}; var {var}')
                    elif len(dict_vars[sect][i][var]):
                        raise ValueError


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

            inp_file_obj.equals(new_file_obj)
