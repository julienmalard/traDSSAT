import os
import unittest

from tests.utils import _test_read, _test_write, rsrcs
from tradssat.out import SoilTempOut, SoilNiOut, SummaryOut, PlantGroOut, ETOut, SoilWatOut, MulchOut
from tradssat import SoilFile, WTHFile, MTHFile, ExpFile, CULFile, ECOFile

input_classes = [SoilFile, WTHFile, MTHFile, ExpFile, CULFile, ECOFile]

rsrcs_out = os.path.join(rsrcs, 'Out')
output_classes = [PlantGroOut, SoilNiOut, SoilTempOut, SoilWatOut, MulchOut, ETOut]
final_out_classes = [SummaryOut]


# Inputs must be read and written
class TestInputs(unittest.TestCase):
    def test_read(self):
        for inp_class in input_classes:
            with self.subTest(inp_class.__name__):
                _test_read(inp_class, folder=rsrcs, testcase=self)

    def test_write(self):
        for inp_class in input_classes:
            with self.subTest(inp_class.__name__):
                _test_write(inp_class, rsrcs, testcase=self)


# Outputs are only read, not written
class TestOutputs(unittest.TestCase):
    def test_read(self):
        for out_class in output_classes:
            with self.subTest(out_class.__name__):
                _test_read(out_class, folder=rsrcs_out, testcase=self)


class TestFinalOutputs(unittest.TestCase):
    def test_read(self):
        for final_out_class in final_out_classes:
            with self.subTest(final_out_class.__name__):
                _test_read(final_out_class, folder=rsrcs_out, testcase=self)
