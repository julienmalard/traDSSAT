import os
import unittest

from tests.utils import test_read, test_write
from tradssat import SoilFile, WTHFile, ExpFile, PlantGrowOut, CULFile, ECOFile

rsrcs = os.path.join(os.path.split(__file__)[0], 'rsrc/mock_DSSAT')
input_classes = [SoilFile, WTHFile, CULFile, ECOFile, ExpFile]

rsrcs_out = os.path.join(os.path.split(__file__)[0], 'rsrc/mock_DSSAT/Out')
output_classes = [PlantGrowOut]


# Inputs must be read and written
class TestInputs(unittest.TestCase):
    def test_read(self):
        for inp_class in input_classes:
            with self.subTest(inp_class.__name__):
                test_read(inp_class, folder=rsrcs, testcase=self)

    def test_write(self):
        for inp_class in input_classes:
            with self.subTest(inp_class.__name__):
                test_write(inp_class, rsrcs, testcase=self)


# Outputs are only read, not written
class TestOutputs(unittest.TestCase):
    def test_read(self):
        for out_class in output_classes:
            with self.subTest(out_class.__name__):
                test_read(out_class, folder=rsrcs_out, testcase=self)
