class Variable(object):
    type_ = None

    def __init__(self, name, size, lims=None, spc=1, info=''):
        self.name = name
        self.size = size
        self.lims = lims
        self.info = info
        self.spc = spc

    def __str__(self):
        return str(self.name)


class CharacterVar(Variable):
    type_ = str

    def __init__(self, name, size, lims=None, spc=1, info=''):
        super().__init__(name, size, lims, spc, info)


class FloatVar(Variable):
    type_ = float

    def __init__(self, name, size, dec, lims=None, spc=1, info=''):
        super().__init__(name, size, lims, spc, info)
        self.dec = dec


class IntegerVar(Variable):
    type_ = int

    def __init__(self, name, size, lims=None, spc=1, info=''):
        super().__init__(name, size, lims, spc, info)


class VariableSet(object):
    def __init__(self, l_vars):
        self._vars = {str(vr): vr for vr in l_vars}

    def __getitem__(self, item):
        return self._vars[item]
