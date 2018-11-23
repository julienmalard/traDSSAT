import os
import shutil
import tempfile
import unittest

from tradssat import DSSATRun, set_dssat_dir, ExpFile


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

    def test_write(self):
        pass

    def test_write_overwrite(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.temp_dir.cleanup()
