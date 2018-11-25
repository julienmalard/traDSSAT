import os
import shutil
import tempfile
import unittest

import numpy as np
import numpy.testing as npt

from tradssat import DSSATRun, set_dssat_dir, ExpFile
from tradssat.exper.exper_vars import TRT_HEAD

_test_vars = {
    'SOL': 'SRGF',
    'WTH': 'SRAD',
    'EXP': 'FACD',
    'CUL': 'P1',
    'ECO': 'TOPT',
}


class TestRuns(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()

        mock_dir = shutil.copytree('rsrc/mock_DSSAT', os.path.join(cls.temp_dir.name, 'DSSAT47'))
        set_dssat_dir(mock_dir)
        cls.file = 'rsrc/mock_DSSAT/Exper/Maize/BRPI0202.MZX'

        cls.dssat_run = DSSATRun(cls.file)
        cls.ref_expfile = ExpFile(cls.file)

    def _get_run(self):
        return DSSATRun(self.file)

    def test_get_general_val(self):
        val = self.dssat_run.get_general_val('PEOPLE')
        ref_val = self.ref_expfile.get_val('PEOPLE')

        self.assertEqual(val, ref_val)

    def test_set_general_val(self):
        run = self._get_run()
        run.set_general_val('PEOPLE', 'me')
        new_val = run.get_general_val('PEOPLE')
        self.assertEqual(new_val, 'me')

    def test_n_factor_levels(self):
        ref_n = self.ref_expfile.get_val('INGENO').size

        n = self.dssat_run.n_factor_levels('CULTIVARS')
        npt.assert_equal(n, np.arange(1, ref_n+1))

    def test_get_trt_num(self):
        ref_names = self.ref_expfile.get_val('TNAME')
        ref_i_s = self.ref_expfile.get_val('N', sect=TRT_HEAD)

        ref_i = 4
        name = ref_names[ref_i_s == ref_i]
        i = self.dssat_run.get_trt_num(name)

        self.assertEqual(ref_i, i)

    def test_get_trt_name(self):
        ref_names = self.ref_expfile.get_val('TNAME')
        ref_i = self.ref_expfile.get_val('N', sect=TRT_HEAD)

        i = 2
        name = self.dssat_run.get_trt_name(i)

        self.assertEqual(ref_names[ref_i == i], name)

    def test_get_trt_val(self):

        for subfile, vr in _test_vars.items():
            with self.subTest(file=subfile):
                self.dssat_run.get_trt_val(vr, trt=1)

    @unittest.skip('not ready')
    def test_set_trt_val(self):
        pass

    @unittest.skip('not ready')
    def test_add_treatment(self):
        pass

    @unittest.skip('not ready')
    def test_remove_treatment(self):
        pass

    @unittest.skip('not ready')
    def test_add_factor_level(self):
        pass

    def test_get_trt_factor_level(self):

        factor = 'CU'
        trt = 5

        factors = self.ref_expfile.get_val(factor)
        trts = self.ref_expfile.get_val('N', sect=TRT_HEAD)

        ref = factors[trts == trt][0]

        val = self.dssat_run.get_treatment_factor_level(trt, 'CU')
        self.assertEqual(val, ref)

    @unittest.skip('not ready')
    def test_set_trt_factor_level(self):
        pass

    def test_get_factor_level_val(self):
        for subfile, vr in _test_vars.items():
            with self.subTest(file=subfile):
                self.dssat_run.get_factor_level_val(vr, level=1)

    @unittest.skip('not ready')
    def test_set_factor_level_val(self):
        pass

    @unittest.skip('not ready')
    def test_clean(self):
        pass

    @unittest.skip('not ready')
    def test_check(self):
        pass

    @unittest.skip('not ready')
    def test_write(self):
        pass

    @unittest.skip('not ready')
    def test_write_overwrite(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
