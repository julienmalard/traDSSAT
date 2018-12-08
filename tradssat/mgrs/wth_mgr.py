import os

from tradssat import WTHFile
from .mgr import PeriphFileMgr, get_dssat_subdir


class PeriphWeatherMgr(PeriphFileMgr):

    def __init__(self, codes, levels):
        self.files = {lvl: WeatherFileMgr(cd) for cd, lvl in zip(codes, levels)}

    def get_value(self, var, level):
        self.files[level].get_value(var)

    def set_value(self, var, val, level):
        self.files[level].set_value(var, val)

    def variables(self):
        return {str(vr) for f in self.files.values() for vr in f.variables()}

    def write(self, force=False):
        for f in self.files.values():
            f.write(force)


class WeatherFileMgr(object):

    def __init__(self, code):
        weather_dir = get_dssat_subdir('Weather')
        gen_weather_dir = os.path.join(weather_dir, 'Gen')

        self.file = None
        for d in [weather_dir, gen_weather_dir]:
            for f in os.listdir(d):
                if WTHFile.matches_file(f):
                    name = os.path.split(os.path.splitext(f)[0])[1]
                    if name.startswith(code):
                        self.file = WTHFile(os.path.join(d, f))
                        break
        if self.file is None:
            raise ValueError('No weather file found matching "{}".'.format(code))

    def get_value(self, var):
        return self.file.get_value(var)

    def variables(self):
        return self.file.variables()
