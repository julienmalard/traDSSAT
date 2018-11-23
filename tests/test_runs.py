import os
import shutil
import tempfile
import unittest

from tradssat import DSSATRun, set_dssat_dir, ExpFile


_test_vars = {
    'SOL': 'SRGF',
    'WTH': 'SRAD',
    'EXP': 'FACD',
    'CUL': 'P1',
    'ECO': 'TOPT',
}


class TestRuns(unittest.TestCase):

    def _get_run(self):
        return DSSATRun(self.file)

    @classmethod
    def setUpClass(cls):
        cls.temp_dir = tempfile.TemporaryDirectory()

        mock_dir = shutil.copytree('rsrc/mock_DSSAT', os.path.join(cls.temp_dir.name, 'DSSAT47'))
        set_dssat_dir(mock_dir)
        cls.file = 'rsrc/mock_DSSAT/Exper/Maize/BRPI0202.MZX'

    def test_get_general_val(self):
        run = self._get_run()
        val = run.get_general_val('PEOPLE')
        ref_val = ExpFile(self.file).get_val('PEOPLE')

        self.assertEqual(val, ref_val)

    def test_set_general_val(self):
        run = self._get_run()
        run.set_general_val('PEOPLE', 'me')
        new_val = run.get_general_val('PEOPLE')
        self.assertEqual(new_val, 'me')

    @unittest.skip('not ready')
    def test_get_n_factor_levels(self):
        pass

    @unittest.skip('not ready')
    def test_get_trt_num(self):
        pass

    @unittest.skip('not ready')
    def test_get_trt_name(self):
        pass

    @unittest.skip('not ready')
    def test_get_trt_val(self):
        run = self._get_run()

        for subfile, vr in _test_vars.items():
            with self.subTest(file=subfile):
                run.get_trt_val(vr, trt=1)

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

    @unittest.skip('not ready')
    def test_get_trt_factor_level(self):
        pass

    @unittest.skip('not ready')
    def test_set_trt_factor_level(self):
        pass

    @unittest.skip('not ready')
    def test_get_factor_level_val(self):
        pass

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
