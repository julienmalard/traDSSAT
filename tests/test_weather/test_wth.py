import os
import unittest
from json import JSONDecodeError
from warnings import warn
import numpy.testing as npt
from tradssat.utils import write_json, read_json
from tradssat.weather import WTHFile


class TestWTH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder = os.path.join(os.path.split(__file__)[0], '../rsrc/mock_DSSAT')
        cls.inp_class = WTHFile

    def _find_files(self):

        ext = self.inp_class.ext

        l_files = []
        for root, dirs, files in os.walk(self.folder):
            for f in files:
                ext_f = os.path.splitext(f)[1]
                if ext_f == ext or ext_f in ext:
                    l_files.append(os.path.join(root, f))

        return l_files

    def _get_ref(self, file, default):
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

                for sect, d_sect in dict_vars.items():
                    for var, val in d_sect.items():
                        npt.assert_equal(ref[sect][var], val, err_msg=sect+var)
    def test_write(self):
        print('test')