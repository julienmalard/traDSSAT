import numpy as np

from tradssat import ExpFile


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFile(file)
        self.soil = self._get_soil()
        self.weather = self._get_weather()
        self.genetics = self._get_genetics()

        self.check()

    def get_val(self, var, trt=None):
        trts = self._valid_trt(trt)
        sect = self._get_sect(var)
        subsect = self._get_subsect(trts, sect)

        self.exp.get_val(var, sect=sect, subsect=subsect)

    def set_val(self, var, val, var_loc='exp', trt=None):
        trts = self._valid_trt(trt)

        var_loc = var_loc.lower()

        if var_loc == 'exp':
            sect = self._get_sect(var)
            subsect = self._get_subsect(trts, sect)
            self.exp.set_val(var, val, sect=sect, subsect=subsect)

        elif var_loc == 'soil':
            soil = self.get_val('', trt)
            self.soil.set_val(var, val, soil=soil)

        elif var_loc == 'weather':
            weather = self.get_val('', trt)
            self.weather.set_val(var, val, weather=weather)

        elif var_loc == 'genetic':
            cultivar = self.get_val('', trt)
            species = self.get_val('', trt)
            self.genetics.set_val(var, val, cult=cultivar, spe=species)

        else:
            raise ValueError(
                '`var_loc` must be one of "exp", "soil", "weather" or "genetic", not "{}".'.format(var_loc)
            )

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

    def _get_soil(self):
        soil_codes = self.get_val('')
        return PeriphFileMgr()

    def _get_weather(self):
        weather_codes = self.get_val('')
        return PeriphFileMgr()


class PeriphFileMgr(object):
    pass
