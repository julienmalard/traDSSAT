import re

import numpy as np


class FileValueSet(object):

    def __init__(self):
        self._sections = {}

    def add_section(self, name):
        self._sections[name] = ValueSection(name)

    def write(self, lines):

        for s in self:
            s.write(lines)

        lines.append('')

        return lines

    def to_dict(self):
        return {name: sect.to_dict() for name, sect in self._sections.items()}

    def get_val(self, var, sect=None, subsect=None):
        if sect is not None:
            return self[sect].get_val(var, subsect)
        else:
            return next(s.get_val(var, subsect) for s in self if var in s)

    def set_val(self, var, val, sect=None, subsect=None, cond=None):
        if sect is not None:
            self[sect].set_val(var, val, subsect, cond=cond)
        else:
            for s in self:
                if var in s:
                    s.set_val(var, val, subsect, cond=cond)

    def find_var_sect(self, var):
        return next(s for s in self if var in s)

    def changed(self):
        return any(s.changed() for s in self)

    def __iter__(self):
        for s in self._sections.values():
            yield s

    def __getitem__(self, item):
        if isinstance(item, re.Pattern):
            return next(s for s in self._sections.values() if re.match(item, s.name))
        else:
            return self._sections[item]


class ValueSection(object):
    def __init__(self, name):
        self.name = name
        self._subsections = []
        self._header_vars = HeaderValues()

    def add_subsection(self, subsect):
        self._subsections.append(subsect)

    def set_header_vars(self, h_vars):
        self._header_vars.set_vars(h_vars)

    def write(self, lines):
        lines.append(self._write_header())
        for s in self:
            s.write(lines)

        lines.append('')

        return lines

    def to_dict(self):
        return {
            'header vars': self._header_vars.to_dict(),
            'main vars': [subsect.to_dict() for subsect in self]
        }

    def get_val(self, var, subsect=None):
        val = []

        if subsect is None:
            subsect = range(len(self._subsections))
        elif isinstance(subsect, int):
            subsect = [subsect]

        for s in subsect:
            sub = self[s]
            if var in sub:
                val.append(sub[var])

        return np.array(val).flatten()

    def set_val(self, var, val, subsect=None, cond=None):

        if subsect is None:
            subsect = range(len(self._subsections))
        elif isinstance(subsect, int):
            subsect = [subsect]

        success = False
        for s in subsect:
            sub = self[s]
            if var in sub:
                success = True
                if cond is None:
                    sub[var] = val
                else:
                    raise NotImplementedError

        if not success:
            raise ValueError('Variable "{}" not found.'.format(var))

    def changed(self):
        return any(s.changed() for s in self)

    def _write_header(self):
        return '*' + self.name + self._header_vars.write()

    def __iter__(self):
        for s in self._subsections:
            yield s

    def __contains__(self, item):
        return any(item in s for s in self._subsections)

    def __getitem__(self, item):
        return self._subsections[item]

    def __setitem__(self, key, value):
        for subsect in self:
            if key in subsect:
                subsect[key] = value


class ValueSubSection(object):
    def __init__(self, l_vars, l_vals):

        self._vars = {str(vr): VariableValue(vr, vl) for vr, vl in zip(l_vars, l_vals)}

    def set_value(self, var, val):
        self._vars[str(var)].set_value(val)

    def check_dims(self):
        return len(np.unique([v.size() for v in self._vars.values()])) == 1

    def check_vals(self):
        for vr in self:
            vr.check_val()

    def n_data(self):
        self.check_dims()
        return self[list(self._vars)[0]].size()

    def write(self, lines):
        self.check_dims()
        self.check_vals()

        lines.append('@' + ''.join([vr.write() for vr in self]))
        for i in range(self.n_data()):
            line = ''.join([vr.write(i) for vr in self])
            lines.append(line)

        return lines

    def to_dict(self):
        return {nm: vr.val for nm, vr in self._vars.items()}

    def changed(self):
        return any(v.changed for v in self)

    def __iter__(self):
        for vr in self._vars.values():
            yield vr

    def __contains__(self, item):
        return str(item) in self._vars

    def __getitem__(self, item):
        return self._vars[str(item)]

    def __setitem__(self, key, value):
        self.set_value(key, value)


class VariableValue(object):
    def __init__(self, var, val):

        self.changed = False

        self.name = str(var)

        self.var = var
        self.val = val

    def set_value(self, val):

        if isinstance(val, np.ndarray) and (val.shape != self.val.shape):
            self.val = np.array(val)
            self.changed = True
        else:
            if np.any(val != self.val):
                self.val[:] = val
                self.changed = True

    def size(self):
        return self.val.size

    def check_val(self):
        self.var.check_val(self.val)

    def write(self, i=None):
        if i is None:
            return self.var.write()
        else:
            self.changed = False
            return self.var.write(self.val[i])


class HeaderValues(object):
    def __init__(self):
        self._subsect = None

    def set_vars(self, subsect):
        self._subsect = subsect

    def to_dict(self):
        if self._subsect is None:
            return []
        else:
            return self._subsect.to_dict()

    def write(self):
        if self._subsect is None:
            return ''
        else:
            return ''.join([vr.write(0) for vr in self._subsect])
