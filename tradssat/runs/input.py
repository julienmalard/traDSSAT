import numpy as np
from tradssat.exper.exper_vars import TRT_HEAD, GENERAL

from .exp_mgr import ExpFileMgr
from .gen_mgr import PeriphGenMgr
from .soil_mgr import PeriphSoilMgr
from .wth_mgr import PeriphWeatherMgr

_factor_codes = {
    'CU': 'CULTIVARS',
    'FL': 'FIELDS',
    'SA': 'SOIL ANALYSIS',
    'IC': 'INITIAL CONDITIONS',
    'MP': 'PLANTING DETAILS',
    'MI': 'IRRIGATION AND WATER MANAGEMENT',
    'MF': 'FERTILIZERS (INORGANIC)',
    'MR': 'RESIDUES AND ORGANIC FERTILIZER',
    'MC': 'CHEMICAL APPLICATIONS',
    'MT': 'TILLAGE AND ROTATIONS',
    'ME': 'ENVIRONMENT MODIFICATIONS',
    'MH': 'HARVEST DETAILS',
    'SM': 'SIMULATION CONTROLS'
}

_level_codes = {
    'CU': 'C',
    'FL': 'L',
    'SA': 'A',
    'IC': 'C',
    'MP': 'P',
    'MI': 'I',
    'MF': 'F',
    'MR': 'R',
    'MC': 'C',
    'MT': 'T',
    'ME': 'E',
    'MH': 'H',
    'SM': 'N'
}

_factor_to_code = {fct: cd for cd, fct in _factor_codes}


def _valid_factor(factor):
    if factor in _factor_codes:
        return factor
    else:
        try:
            return _factor_to_code[factor]
        except KeyError:
            raise ValueError('Factor "{}" not recognised.'.format(factor))


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFileMgr(file)

        trts = self.exp.get_file_val('N', sect=TRT_HEAD)

        self.soil = PeriphSoilMgr(self.exp.get_file_val('ID_SOIL'), trts)
        self.weather = PeriphWeatherMgr(self.exp.get_file_val('WSTA'), treatments=trts)
        self.genetics = PeriphGenMgr(self.exp.get_file_val('CR'), self.exp.get_file_val('INGENO'), trts)

        self.check()

    def get_general_val(self, var):
        self.exp.get_file_val(var, sect=GENERAL)

    def set_general_val(self, var, val):
        self.exp.set_file_val(var, val, sect=GENERAL)

    def add_treatment(self, name, factors=None):
        if factors is None:
            factors = {}
        factors = {_valid_factor(cd): vl for cd, vl in factors.items()}

        n = self.treatments().size + 1
        d_vals = {
            'N': n,
            'TNAME': name,
            **{cd: 0 for cd in _factor_codes}
        }
        d_vals.update(factors)
        self.exp.add_row(sect=TRT_HEAD, subsect=0, vals=factors)

    def remove_treatment(self, trt):
        if isinstance(trt, str):
            trt = self.get_trt_num(trt)
        self.exp.remove_row(sect=TRT_HEAD, subsect=0, cond={'N': trt})

    def add_factor_level(self, factor, vals):
        factor = _valid_factor(factor)
        factor_name = _factor_codes[factor]
        level = self.n_factor_levels(factor) + 1
        lv_code = _level_codes[factor]
        level_vals = {
            lv_code: level,
            **vals
        }
        self.exp.add_row(sect=factor_name, vals=level_vals)

    def get_treatment_factor_level(self, trt, factor):
        factor = _valid_factor(factor)
        trt = self._valid_trt(trt)

        trt_nums = self.treatments()
        levels = self.exp.get_file_val(factor, sect=TRT_HEAD)

        return levels[trt_nums == trt]

    def set_treatment_factor_level(self, trt, factor, level):
        factor = _valid_factor(factor)
        trt = self._valid_trt(trt)

        self.exp.set_file_val(factor, level, sect=TRT_HEAD, subsect=0, cond={'N': trt})

    def get_factor_level_val(self, var, level):
        file = self._locate_var(var)
        return file.get_val(var, level=level)

    def set_factor_level_val(self, var, val, level):
        file = self._locate_var(var)
        file.set_val(var, val, level=level)

    def get_trt_val(self, var, trt):

        var_loc = self._locate_var(var)
        factor = self._get_var_factor(var, var_loc)
        level = self.get_treatment_factor_level(trt, factor)

        return var_loc.get_val(var, level)

    def set_trt_val(self, var, val, trt):

        var_loc = self._locate_var(var)
        factor = self._get_var_factor(var, var_loc)
        level = self.get_treatment_factor_level(trt, factor)

        var_loc.set_val(var, val, level)

    def treatments(self, name=False):
        if name:
            return self.exp.get_trt_names()
        else:
            return self.exp.get_trt_nums()

    def n_factor_levels(self, factor):
        factor = _valid_factor(factor)
        lv_var = _level_codes[factor]

        levels = self.exp.get_file_val(lv_var, sect=factor)

        return np.unique(levels)

    def get_trt_name(self, n):
        nums = self.treatments()
        names = self.treatments(name=True)

        return names[np.where(nums == n)]

    def get_trt_num(self, trt):
        nums = self.treatments()
        names = self.treatments(name=True)

        return nums[np.where(names == trt)]

    def check(self):
        # check consistent treatment numbering (numeric order)
        # Check all treatments exist
        # check no ununsed treatments (warn)
        # check all external soil, weather, genetic files exist
        # Check all treatment factor levels exist in sections
        pass

    def clean(self):
        # remove factor levels not used in any treatment

        # renumber treatments
        trts = np.arange(self.treatments().size)
        self.exp.set_file_val('N', trts, sect=TRT_HEAD)

        # renumber factor levels, and reorder them in subsections
        pass

    def write(self, file=None, force=False, clean=True, override=False):
        if clean:
            self.clean()

        # todo: peripheral files
        self.exp.file.write(file=file, force=force)

    def _valid_trt(self, trt):

        if trt is None:
            return self.treatments()

        elif isinstance(trt, int):
            trt = [self.get_trt_name(trt)]
        elif isinstance(trt, str):
            trt = [trt]

        for i, t in enumerate(trt):
            if isinstance(t, str):
                trt[i] = self.get_trt_num(t)

            elif t not in self.treatments():
                raise ValueError(t)

        return trt

    def _locate_var(self, var):

        for f in [self.exp, self.soil, self.genetics, self.weather]:
            if var in f.variables():
                return f

        raise ValueError('Could not find variable "{}".'.format(var))

    def _get_var_factor(self, var, var_loc):
        if isinstance(var_loc, (PeriphSoilMgr, PeriphWeatherMgr)):
            sect = 'FIELDS'
        elif isinstance(var_loc, PeriphGenMgr):
            sect = 'CULTIVARS'
        else:
            sect = self.exp.find_var_sect(var)

        return _factor_to_code[sect]
