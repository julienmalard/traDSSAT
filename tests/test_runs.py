import unittest
from tradssat import DSSATRun


class TestRuns(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_get_general_val(self):
        run = DSSATRun('rsrc/mock_DSSAT/Exper/Maize/BRPI0202.MZX')

    def test_set_general_val(self):
        pass

    def test_write(self):
        pass

    def test_write_overwrite(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass