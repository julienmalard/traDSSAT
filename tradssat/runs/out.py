from tradssat import SummaryOut, PlantGrowOut


class DSSATResults(object):

    def __init__(self, folder):
        self.folder = folder

        outfiles = [PlantGrowOut]
        self._outfiles = {f: None for f in outfiles}

        self._sumoutclass = SummaryOut
        self._sumoutfile = None

    def reload(self):
        for out_class in self._outfiles:
            self._outfiles[out_class] = None
        self._sumoutfile = None

    def get_value(self, var, trt, t=None, at='YEAR DOY'):

        if t is not None:
            if at in ['DAS', 'DAP']:
                cond = {at: t}
            elif at in ['DOY', 'YEAR DOY']:
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
                return f.get_value(var, sect={'TREATMENT': trt}, cond=cond)

        raise ValueError('Output variable "{}" could not be found in any output file.'.format(var))

    def get_final_value(self, var, trt):
        if self._sumoutfile is None:
            self._sumoutfile = self._sumoutclass(self.folder)
        if var in self._sumoutfile.variables():
            return self._sumoutfile.get_value(var, cond={'TRNO': trt})[0]
        vals = self.get_value(var=var, trt=trt)
        return vals[-1]
