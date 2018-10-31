class Variable(object):
    type_ = None

    def __init__(self, name, section, size, lims=None, info=''):
        self.name = name
        self.section = section
        self.size = size
        self.lims = lims
        self.info = info

    def __str__(self):
        return str(self.name)


class CharacterVar(Variable):
    type_ = str

    def __init__(self, name, section, size, lims=None, info=''):
        super().__init__(name, section, size, lims, info)


class FloatVar(Variable):
    type_ = float

    def __init__(self, name, section, size, dec, lims=None, info=''):
        super().__init__(name, section, size, lims, info)
        self.dec = dec


class IntegerVar(Variable):
    type_ = int

    def __init__(self, name, section, size, lims=None, info=''):
        super().__init__(name, section, size, lims, info)


class VariableSet(object):
    def __init__(self, l_vars):
        self._vars = {str(vr): vr for vr in l_vars}

    def __getitem__(self, item):
        return self._vars[item]
