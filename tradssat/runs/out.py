from tradssat.out import PlantGrowOut


class DSSATResults(object):

    def __init__(self, folder):
        self.folder = folder

        outfiles = [PlantGrowOut]
        self._outfiles = {f: None for f in outfiles}

    def reload(self):
        for out_class in self._outfiles:
            self._outfiles[out_class] = out_class(self.folder)

    def get_value(self, var, trt, t=None, at='YEAR DOY'):

        if t is not None:
            if at in ['DAS', 'DAP']:
                cond = {at: t}
            elif at == 'YEAR DOY':
                year, doy = t.split()
                cond = {'YEAR': int(year), 'DOY': int(doy)}
            else:
                raise ValueError(at)
        else:
            cond = None

        for c, f in self._outfiles.items():

            if f is None:
                try:
                    f = self._outfiles[c] = c(self.folder)
                except FileNotFoundError:
                    pass

            if var in f.variables():
                if t is None:
                    return f.get_value(var)
                else:
                    return f.get_value(var, sect={'TREATMENT': trt}, cond=cond)

        raise ValueError('Output variable "{}" could not be found in any output file.'.format(var))

    def get_final_val(self, var, trt=None):
        pass
