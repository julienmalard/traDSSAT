import numpy as np
from tradssat import ExpFile
from tradssat.exper.exper_vars import TRT_HEAD, GENERAL

from .gen_mgr import PeriphGenMgr
from .soil_mgr import PeriphSoilMgr
from .wth_mgr import PeriphWeatherMgr

_factor_codes = {
    'CU': 'CULTIVARS',
    'FL': 'FIELDS',
    'SA': 'SOIL ANALYSIS',
    'IC': '',
    'MP': '',
    'MI': '',
    'MF': '',
    'MR': '',
    'MC': '',
    'MT': '',
    'ME': '',
    'MH': '',
    'SM': ''
}

_factor_to_code = {fct: cd for cd, fct in _factor_codes}


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFile(file)

        trts = self.exp.get_val('N', sect=TRT_HEAD)

        self.soil = PeriphSoilMgr(self.get_val('ID_SOIL'), trts)
        self.weather = PeriphWeatherMgr(self.get_val('WSTA'), treatments=trts)
        self.genetics = PeriphGenMgr(self.get_val('CR'), self.get_val('INGENO'), trts)

        self.check()

    def get_general_val(self, var):
        self.exp.get_val(var, sect=GENERAL)

    def set_general_val(self, var, val):
        self.exp.set_val(var, val, sect=GENERAL)

    def add_treatment(self, name, vals=None):
        if vals is None:
            vals = {}
        n = self.n_trts() + 1
        d_vals = {
            'N': n,
            'TNAME': name,
            **{cd: 0 for cd in _factor_codes}
        }
        d_vals.update(vals)
        self.exp.add_row(sect=TRT_HEAD, subsect=0, vals=vals)

    def remove_treatment(self, trt):
        if isinstance(trt, str):
            trt = self.get_trt_num(trt)
        self.exp.remove_row(sect=TRT_HEAD, subsect=0, cond={'N': trt})

    def add_factor_level(self, factor):
        pass

    def get_treatment_factor_level(self, trt, factor):
        factor_code = _factor_to_code[factor]
        if isinstance(trt, str):
            trt = self.get_trt_num(trt)
        trt_nums = self.exp.get_val('N', sect=TRT_HEAD)
        factors = self.exp.get_val(factor_code, sect=TRT_HEAD)
        return factors[trt_nums == trt]

    def set_treatment_factor_level(self, trt, factor, level):
        factor_code = _factor_to_code[factor]
        if isinstance(trt, str):
            trt = self.get_trt_num(trt)
        trt_nums = self.exp.get_val('N', sect=TRT_HEAD)
        i = np.where(trt_nums == trt)

        self.exp.set_val(factor_code, level, sect=TRT_HEAD, subsect=0, i=i)

    def get_treatment_val(self, var, trt):
        pass

    def get_val(self, var, trt):

        var_loc = self._locate_var(var)
        var_loc.get_val(var, trt)

    def set_val(self, var, val, trt):

        var_loc = self._locate_var(var)

        var_loc.set_val(var, val, trt)

    def get_trt_factor_level(self, trt, sect):

        factor_name = _factor_codes[sect]
        levels = self.exp.get_val(factor_name)
        trts = self.treatments()

        return levels[trts == trt]

    def _locate_var(self, var):

        for f in [self.exp, self.soil, self.genetics, self.weather]:
            if var in f.variables():
                return f
        raise ValueError('Could not find variable "{}".'.format(var))

    def treatments(self, name=False):
        if name:
            return self.exp.get_val('TNAME')
        else:
            return self.exp.get_val('N', sect=TRT_HEAD)

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

    def write(self, file=None, force=False, override=False):
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
