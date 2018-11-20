import os

from tradssat import SoilFile, config


class PeriphSoilMgr(object):

    def __init__(self, soils, treatments):
        self.files = {trt: SoilMgr(sl) for sl, trt in zip(soils, treatments)}

    def get_val(self, var, trt):
        return self.files[trt].get_val(var)

    def set_val(self, var, val, trt):
        return self.files[trt].set_val(var, val)


class SoilMgr(object):
    def __init__(self, code):

        soils_dir = os.path.join(config['DSSAT_DIR'], 'Soil')

        for f in os.listdir(soils_dir):
            if SoilFile.matches_file(f):
                file = SoilFile(f)

                if code in file:
                    self.file = file
                    self.code = code
                    break

    def get_val(self, var):
        return self.file.get_val(var, sect=self.code)

    def set_val(self, var, val):
        return self.file.set_val(var, val, sect=self.code)
