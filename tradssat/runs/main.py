from tradssat import ExpFile


class DSSATRun(object):
    def __init__(self, file):
        self.file = file
        self.exp = ExpFile(file)
        self.soil = self._get_soil()
        self.weather = self._get_weather()

    def get_val(self, var, treatment=None):
        pass

    def set_val(self, var, treatment=None):
        pass

    def get_out(self, var, treatment=None):
        pass

    def _get_soil(self):
        soil_codes = self.get_val('')

    def _get_weather(self):
        weather_codes = self.get_val('')


class PeriphFileMgr(object):
    pass