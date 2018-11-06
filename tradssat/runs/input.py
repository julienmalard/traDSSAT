import numpy as np

from tradssat import ExpFile


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFile(file)
        self.soil = self._get_soil()
        self.weather = self._get_weather()

    def get_val(self, var, trt=None):
        trts = self._valid_trt(trt)

    def set_val(self, var, trt=None):
        trt, n_trt = self._valid_trt(trt)

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
