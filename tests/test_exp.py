import os

from tests._inp_test_templ import FileTestTemplate
from tradssat.exper import ExpFile
import unittest


@unittest.skip
class TestEXP(FileTestTemplate):
    @classmethod
    def _get_class(cls):
        return os.path.join(os.path.split(__file__)[0], 'rsrc/mock_DSSAT'), ExpFile
