class Variable(object):
    type_ = None

    def __init__(self, name, size, lims=None, spc=1, info=''):
        self.name = name
        self.size = size
        self.lims = lims
        self.info = info
        self.spc = spc

    def write(self, val=None):
        if val is None:
            return str(self).rjust(self.size + self.spc)
        else:
            return self._write(val)

    def _write(self, val):
        raise NotImplementedError

    def __str__(self):
        return str(self.name)

class CharacterVar(Variable):
    type_ = str

    def __init__(self, name, size, lims=None, spc=1, info=''):
        super().__init__(name, size, lims, spc, info)

    def _write(self, val):
        return val.rjust(self.size + self.spc)


class FloatVar(Variable):
    type_ = float

    def __init__(self, name, size, dec, lims=None, spc=1, info=''):
        super().__init__(name, size, lims, spc, info)
        self.dec = dec

    def _write(self, val):
        return '{:{sz}.{dec}f}'.format(val, sz=self.size, dec=self.dec).rjust(self.spc + self.size)


class IntegerVar(Variable):
    type_ = int

    def __init__(self, name, size, lims=None, spc=1, info=''):
        super().__init__(name, size, lims, spc, info)

    def _write(self, val):
        return '{:{sz}d}'.format(val, sz=self.size).rjust(self.spc + self.size)


class VariableSet(object):
    def __init__(self, l_vars):
        self._vars = {str(vr): vr for vr in l_vars}

    def __getitem__(self, item):
        return self._vars[item]
