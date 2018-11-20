from tradssat import WTHFile, config
import os

class PeriphWeatherMgr(object):

    def __init__(self, codes, start, end, treatments):
        self.files = {trt: WeatherFileMgr(cd, srt, end) for cd, srt, end, trt in zip(codes, start, end, treatments)}

    def get_val(self, var, trt):
        self.files[trt].get_val(var)

    def set_val(self, var, val, trt):
        self.files[trt].set_val(var, val)


class WeatherFileMgr(object):

    def __init__(self, code, start, end):
        weather_dir = os.path.join(config['DSSAT_DIR'], 'Weather')
        gen_weather_dir = os.path.join(weather_dir, 'Gen')

        self.file = None
        for d in [weather_dir, gen_weather_dir]:
            for f in os.listdir(d):
                if WTHFile.matches_file(f):
                    name = os.path.split(os.path.splitext(f)[0])[1]
                    if name.startswith(code):
                        self.file = WTHFile(f)
                        break
        if self.file is None:
            raise ValueError
