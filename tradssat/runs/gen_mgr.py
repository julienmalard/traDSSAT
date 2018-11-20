import os

import numpy as np
from tradssat import CULFile, ECOFile, config


class PeriphGenMgr(object):
    def __init__(self, crops, cultivars, treatments):
        self.crops = crops
        self.cultivars = cultivars

        self.files = {trt: GeneticMgr(crp, cult) for trt, crp, cult in zip(treatments, crops, cultivars)}

    def get_val(self, var, trt):
        return self.files[trt].get_val(var)

    def set_val(self, var, val, trt):
        return self.files[trt].set_val(var, val)


class GeneticMgr(object):
    def __init__(self, crop, cult):
        self.crop = crop
        self.cult = cult

        self.eco_file = self.cult_file = None
        for f in os.listdir(config['DSSAT_DIR']):
            name = os.path.split(f)[1]
            if CULFile.matches_file(name) and name.startswith(self.crop):
                self.cult_file = CULFile(f)
            elif ECOFile.matches_file(name) and name.startswith(self.crop):
                self.eco_file = ECOFile(self.crop)

            if self.eco_file is not None and self.cult_file is not None:
                break

        if self.cult_file is None:
            raise ValueError('No cultivar file (.CUL) found for crop "{}".'.format(self.crop))

        eco_codes = self.cult_file.get_val('ECO#')
        cult_codes = self.cult_file.get_val('VAR#')
        eco = eco_codes[cult_codes == self.cult]

        self.eco_n = np.where(self.eco_file.get_val('ECO#') == eco)
        self.cult_n = np.where(cult_codes == cult)

    def get_val(self, var):
        if var in self.cult_file.variables():
            return self.cult_file.get_val(var)
        elif var in self.eco_file.variables():
            return self.eco_file.get_val(var)
        else:
            raise ValueError('No genetic variable named "{}" was found.'.format(var))

    def set_val(self, var, val):
        if var in self.cult_file.variables():
            return self.cult_file.set_val(var, val)
        elif var in self.eco_file.variables():
            return self.eco_file.set_val(var, val)
        else:
            raise ValueError('No genetic variable named "{}" was found.'.format(var))
