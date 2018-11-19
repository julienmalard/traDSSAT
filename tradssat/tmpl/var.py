import re

import numpy as np


class Variable(object):
    type_ = None

    def __init__(self, name, size, spc, header_fill, float_r, sect, info):
        self.name = name
        self.size = size
        self.spc = spc
        self.info = info
        self.sect = sect
        self.fill = header_fill

        self.float_r = float_r

    def write(self, val=None):
        if val is None:
            txt = str(self)
        else:
            txt = self._write(val)

        if self.float_r:
            return ' ' * self.spc + txt.ljust(self.size, self.fill)
        else:
            return ' ' * self.spc + txt.rjust(self.size, self.fill)

    def check_val(self, val):
        raise NotImplementedError

    def _write(self, val):
        raise NotImplementedError

    def __str__(self):
        return str(self.name)


class CharacterVar(Variable):
    type_ = str

    def __init__(self, name, size, spc=1, sect=None, header_fill=' ', info=''):
        super().__init__(name, size, spc, header_fill, float_r=False, sect=sect, info=info)

    def check_val(self, val):
        if isinstance(val, str):
            if len(val) > self.size:
                raise ValueError(
                    'Value "{val}" is longer than {sz} characters for variable {name}.'.format(
                        val=val, sz=self.size, name=self
                    )
                )

    def _write(self, val):
        return val


class NumericVar(Variable):

    def __init__(self, name, size, lims, spc, header_fill, sect, info):

        super().__init__(name, size, spc, header_fill, sect=sect, float_r=True, info=info)

        if lims is None:
            lims = (-np.inf, np.inf)
        lims = (-np.inf if lims[0] is None else lims[0], np.inf if lims[1] is None else lims[1])

        self.lims = lims

    def check_val(self, val):
        val = np.array(val)
        out = np.where(np.logical_or(np.less(val, self.lims[0]), np.greater(val, self.lims[1])))
        if len(out[0]):
            vals_out = val[out]
            raise ValueError(
                'Value {val} is not in range {rng} for variable {name}.'.format(val=vals_out, name=self, rng=self.lims)
            )

    def _write(self, val):
        raise NotImplementedError


class FloatVar(NumericVar):
    type_ = float

    def __init__(self, name, size, dec, lims=None, spc=1, sect=None, header_fill=' ', info=''):
        super().__init__(name, size, lims, spc, header_fill, sect, info=info)
        self.dec = dec

    def _write(self, val):
        if val == -99:
            return '-99'  # to avoid size overflow on small-sized variables with decimals
        else:
            return '{:{sz}.{dec}f}'.format(val, sz=self.size, dec=self.dec)


class IntegerVar(NumericVar):
    type_ = int

    def __init__(self, name, size, lims=None, spc=1, sect=None, header_fill=' ', info=''):
        super().__init__(name, size, lims, spc, header_fill, sect, info=info)

    def _write(self, val):
        return '{:{sz}d}'.format(val, sz=self.size)


class VariableSet(object):
    def __init__(self, l_vars):
        self._vars = l_vars

    def get_var(self, var, sect=None):

        def match(vr_sect, target_sect):
            if None in [vr_sect, target_sect]:
                return True
            elif isinstance(vr_sect, re.Pattern):
                return re.fullmatch(vr_sect, target_sect)
            else:
                return target_sect == vr_sect

        try:
            return next(
                vr for vr in self._vars if str(vr) == var and match(vr.sect, sect)
            )
        except StopIteration:
            if sect is None:
                msg = 'Variable {var} does not exist.'.format(var=var)
            else:
                msg = 'Variable {var} does not exist in section {sect}.'.format(var=var, sect=sect)
            raise ValueError(msg)

    def __contains__(self, item):
        return any(str(vr) == str(item) for vr in self._vars)
