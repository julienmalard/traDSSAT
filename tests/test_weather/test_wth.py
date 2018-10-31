import os
import unittest
from warnings import warn

from tradssat.utils import write_json
from tradssat.weather.wth import WTHFile


class TestWTH(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder = '../rsrc/mock_DSSAT'
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
        file_name = os.path.splitext(file)[0]
        ref_file = f'ref_{file_name}.json'
        if not os.path.isfile(ref_file):
            write_json(default, ref_file)
            warn('Reference generated for file "{}".'.format(file_name))

    def test_read(self):

        files = self._find_files()
        for f in files:
            with self.subTest(os.path.split(f)[1]):
                dict_vars = self.inp_class(f).values

                ref = self._get_ref(f, dict_vars)

                self.assertDictEqual(dict_vars, ref)
