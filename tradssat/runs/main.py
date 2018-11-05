from tradssat import ExpFile


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFile(file)
        self.soil = self._get_soil()
        self.weather = self._get_weather()

    def get_val(self, var, treatment):
        trt, n_trt = self._valid_trt(treatment)

    def set_val(self, var, treatment):
        trt, n_trt = self._valid_trt(treatment)

    def get_out(self, var, treatment):
        trt, n_trt = self._valid_trt(treatment)

    def treatments(self):
        nums = self.exp.get_val('N')
        names = self.exp.get_val('TNAME')
        return {name: num for name, num in zip(names, nums)}

    def _valid_trt(self, trt):
        if isinstance(trt, str):
            return next((t, n) for t, n in self.treatments().items() if n == trt)
        else:
            return trt, self.treatments()[trt]

    def _get_soil(self):
        soil_codes = self.get_val('')

    def _get_weather(self):
        weather_codes = self.get_val('')


class PeriphFileMgr(object):
    pass
