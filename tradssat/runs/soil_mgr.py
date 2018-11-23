import os

from tradssat import SoilFile
from .mgr import get_dssat_subdir


class PeriphSoilMgr(object):

    def __init__(self, soils, treatments):
        self.files = {trt: SoilMgr(sl) for sl, trt in zip(soils, treatments)}

    def get_val(self, var, trt):
        return self.files[trt].get_val(var)

    def set_val(self, var, val, trt):
        return self.files[trt].set_val(var, val)

    def variables(self):
        return list({v for f in self.files.values() for v in f.variables()})


class SoilMgr(object):
    def __init__(self, code):

        soils_dir = get_dssat_subdir('Soil')

        self.file = None
        for f in os.listdir(soils_dir):
            if SoilFile.matches_file(f):
                file = SoilFile(os.path.join(soils_dir, f))

                if code in file:
                    self.file = file
                    self.code = code
                    break

        if self.file is None:
            raise ValueError('No soil file found for soil "{}".'.format(code))

    def get_val(self, var):
        return self.file.get_val(var, sect=self.code)

    def set_val(self, var, val):
        return self.file.set_val(var, val, sect=self.code)

    def variables(self):
        return self.file.variables()
