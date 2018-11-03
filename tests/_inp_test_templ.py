import os
import unittest
from json import JSONDecodeError
from tempfile import NamedTemporaryFile
from warnings import warn

import numpy.testing as npt
from tradssat.utils import read_json, write_json


class FileTestTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.folder, cls.inp_class = cls._get_class()

    @classmethod
    def _get_class(cls):
        return '', None

    def _find_files(self):

        if self.inp_class is None:
            return []

        ext = self.inp_class.ext

        l_files = []
        for root, dirs, files in os.walk(self.folder):
            for f in files:
                ext_f = os.path.splitext(f)[1]
                if ext_f == ext or ext_f in ext:
                    l_files.append(os.path.join(root, f))

        return l_files

    @staticmethod
    def _get_ref(file, default):
        path, file = os.path.split(file)
        file_name = os.path.splitext(file)[0]
        ref_file = os.path.join(path, f'ref_{file_name}.json')
        try:
            return read_json(ref_file)
        except (FileNotFoundError, JSONDecodeError):
            write_json(default, ref_file)
            warn('Reference generated for tmpl "{}".'.format(file_name))
            return default

    def test_read(self):
        files = self._find_files()
        for f in files:
            with self.subTest(os.path.split(f)[1]):
                dict_vars = self.inp_class(f).to_dict()

                ref = self._get_ref(f, dict_vars)

                for sect, l_sect in ref.items():
                    for i, subsect in enumerate(l_sect):

                        for var, val in subsect.items():
                            npt.assert_equal(dict_vars[sect][i][var], val, err_msg=sect + var)

    def test_write(self):
        files = self._find_files()
        for f in files:
            with self.subTest(os.path.split(f)[1]):

                ext = self.inp_class.ext
                if isinstance(ext, list):
                    ext = ext[0]

                temp_file = NamedTemporaryFile(suffix=ext).name
                inp_file_obj = self.inp_class(f)
                inp_file_obj.write(temp_file)

                new_file_obj = self.inp_class(temp_file)

                inp_file_obj.equals(new_file_obj)
