import os
import unittest

import numpy.testing as npt
from tradssat import SoilFile, WTHFile, MTHFile, ExpFile, CULFile, ECOFile, DSSATResults
from tradssat.out import SoilTempOut, SoilNiOut, SummaryOut, PlantGroOut, ETOut, SoilWatOut, MulchOut

from tests.utils import _test_read, _test_write, rsrcs, read_json, get_ref_var

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


class TestOutHeader(unittest.TestCase):

    def setUp(self):
        self.path = f'{rsrcs_out}/Cassava/headerTest'
        self.ref = read_json(f'{self.path}/_ref_PlantGro.OUT.json')
        self.instance = DSSATResults(self.path)

    def test_entire_array(self):
        actual = self.instance.get_value("HWAD", trt=1, run=2)
        expected = get_ref_var(self.ref, "HWAD", trt=1, run=2)
        npt.assert_equal(actual, expected)

    def test_time_specific(self):
        actual = self.instance.get_value("TWAD", trt=2, run=4, t=194, at='DAP')
        expected = 9394
        npt.assert_equal(actual, expected)

    def test_wrong_values(self):
        """
        Header var 'run' is unique for each simulation.
        For the current ref file the correct input is: 'trt = 2' and 'run = 4'
        """
        with npt.assert_raises(StopIteration):
            self.instance.get_value("LAID", trt=2, run=2)
