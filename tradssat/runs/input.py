import os

import numpy as np
from tradssat import ExpFile, config, WTHFile
from .gen_mgr import PeriphGenMgr


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFile(file)

        self.soil = PeriphSoilMgr(self.get_val('ID_SOIL'))
        self.weather = PeriphWeatherMgr(self.get_val('WSTA'))
        self.genetics = PeriphGenMgr(self.get_val('CR'), self.get_val('INGENO'))

        self.check()

    def get_val(self, var, trt=None):
        trts = self._valid_trt(trt)

        var_loc = self._locate_var(var)

        sect = self._get_sect(var)
        subsect = self._get_subsect(trts, sect)

        self.exp.get_val(var, sect=sect, subsect=subsect)

    def set_val(self, var, val, trt=None, overwrite=False):
        trts = self._valid_trt(trt)

        var_loc = self._locate_var(var)

        var_loc.set_val(var, val)

    def _locate_var(self, var):

        for f in [self.exp, self.soil, self.genetics, self.weather]:
            if var in f.variables():
                return f
        raise ValueError('Could not find variable "{}".'.format(var))

    def treatments(self):
        return self.exp.get_val('TNAME')

    def get_trt_name(self, n):
        nums = self.exp.get_val('N')
        names = self.exp.get_val('TNAME')

        return names[np.where(nums == n)]

    def get_trt_num(self, trt):
        nums = self.exp.get_val('N')
        names = self.exp.get_val('TNAME')

        return nums[np.where(names == trt)]

    def check(self):
        # check consistent treatment numbering (numeric order; all subsections have only 1 treatment no.)
        # Check all treatments exist
        # check no ununsed treatments (warn)
        # check all external soil, weather, genetic files exist
        pass

    def clean(self):
        # remove unused treatments and associated subsections
        pass

    def write(self, file=None):
        pass

    def _valid_trt(self, trt):
        if trt is None:
            trt = self.treatments()
        if isinstance(trt, int):
            trt = [self.get_trt_name(trt)]
        elif isinstance(trt, str):
            trt = [trt]

        for i, t in enumerate(trt):
            if isinstance(t, int):
                trt[i] = self.get_trt_name(t)

            elif t not in self.treatments():
                raise ValueError(t)

        return trt


class PeriphFileMgr(object):
    def __init__(self, files):
        self._files = files
        self.dssat_dir = config['DSSAT_DIR']

    def get_val(self, var, code):
        return self._files[code].get_val(var)

    def set_val(self, var, val, code):
        return self._files[code].set_val(var, val)

