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

    def get_value(self, var, sect=None, subsect=None, cond=None):

        if isinstance(sect, str):
            return self[sect].get_value(var, subsect, cond=cond)
        else:
            if isinstance(sect, dict):
                sects = [
                    s for s in self if all(vr in s and np.all(s.get_header_var(vr) == vl) for vr, vl in sect.items())
                ]
            else:
                sects = self._sections.values()
            return next(s.get_value(var, subsect, cond=cond) for s in sects if var in s)

    def set_value(self, var, val, sect=None, subsect=None, cond=None):
        if sect is not None:
            self[sect].set_value(var, val, subsect, cond=cond)
        else:
            for s in self:
                if var in s:
                    s.set_value(var, val, subsect, cond=cond)

    def add_row(self, sect, subsect=None, vals=None):
        self[sect].add_row(subsect, vals)

    def remove_row(self, sect, subsect=None, cond=None):
        self[sect].remove_row(subsect, cond)

    def find_var_sect(self, var):
        return next(s.name for s in self if var in s)

    def changed(self):
        return any(s.changed() for s in self)

    def __iter__(self):
        for s in self._sections.values():
            yield s

    def __contains__(self, item):
        return item in self._sections

    def __getitem__(self, item):
        if isinstance(item, str):
            return self._sections[item]
        else:
            return next(s for s in self._sections.values() if re.match(item, s.name))


class ValueSection(object):
    def __init__(self, name):
        self.name = name
        self._subsections = []
        self._header_vars = HeaderValues()

    def add_subsection(self, subsect):
        self._subsections.append(subsect)

    def set_header_vars(self, h_vars):
        self._header_vars.set_vars(h_vars)

    def get_header_var(self, var):
        return self._header_vars.get_value(var)

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

    def get_value(self, var, subsect=None, cond=None):

        subsect = self._valid_subsects(subsect)

        if cond is None:
            cond = {}
        req_vars = {var, *cond}

        val = []
        for s in subsect:
            sub = self[s]
            if all(vr in sub for vr in req_vars):
                filter_ = sub.filter_cond(cond)
                val.append(sub[var].val[filter_])

        return np.array(val).flatten()

    def set_value(self, var, val, subsect=None, cond=None):

        subsect = self._valid_subsects(subsect)

        if cond is None:
            cond = {}
        req_vars = {var, *cond}

        success = False
        for s in subsect:
            sub = self[s]
            if all(vr in sub for vr in req_vars):
                success = True
                sub.set_value(var, val, cond=cond)

        if not success:
            raise ValueError('Variable "{}" not found.'.format(var))

    def add_row(self, subsect=None, vals=None):
        subsect = self._valid_subsects(subsect)
        for s in subsect:
            self[s].add_row(vals)

    def remove_row(self, subsect=None, cond=None):
        subsect = self._valid_subsects(subsect)
        for s in subsect:
            self[s].remove_row(cond)

    def changed(self):
        return any(s.changed() for s in self)

    def _write_header(self):
        return '*' + self.name + self._header_vars.write()

    def _valid_subsects(self, subsects):
        if subsects is None:
            subsects = range(len(self._subsections))
        elif isinstance(subsects, int):
            subsects = [subsects]
        return subsects

    def __iter__(self):
        for s in self._subsections:
            yield s

    def __contains__(self, item):
        return any(item in s for s in self._subsections) or item in self._header_vars

    def __getitem__(self, item):
        return self._subsections[item]

    def __setitem__(self, key, value):
        for subsect in self:
            if key in subsect:
                subsect[key] = value


class ValueSubSection(object):
    def __init__(self, l_vars, l_vals):

        self._vars = {str(vr): VariableValue(vr, vl) for vr, vl in zip(l_vars, l_vals)}

    def set_value(self, var, val, cond=None):
        filter_ = self.filter_cond(cond)
        self._vars[str(var)].set_value(val, i=filter_)

    def add_row(self, vals=None):
        if vals is None:
            vals = {}
        for nm, vr in self._vars.items():
            val = vals[nm] if nm in vals else vr.var.miss
            vr.add_value(val)

    def remove_row(self, cond=None):
        filter_ = self.filter_cond(cond)
        for vr in self._vars.values():
            vr.remove_value(filter_)

    def filter_cond(self, cond):
        if cond is None:
            cond = {}
        return np.all(
            [self[vr] == vl for vr, vl in cond.items()], axis=0
        )

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
            written = [vr.write(i) for vr in self]
            for i, (x, vr) in enumerate(zip(list(written), self)):
                extra = len(x) - (vr.var.size + vr.var.spc)
                if i < len(written) - 1 and extra:
                    written[i + 1] = written[i + 1][extra:]

            line = ''.join(written)
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

    def set_value(self, val, i=None):
        if i is None:
            i = True

        if isinstance(val, np.ndarray) and (val.shape != self.val[i].shape):
            if i is not True:
                raise ValueError('Cannot set value by index when shapes do not match.')
            self.val = np.array(val)
            self.changed = True

        else:
            if np.any(val != self.val[i]):
                self.val[i] = val
                self.changed = True

    def add_value(self, val):
        self.val = np.append(self.val, val).astype(self.val.dtype)
        self.changed = True

    def remove_value(self, i):
        if i.dtype == bool:
            filter_ = i
        else:
            filter_ = np.isin(np.arange(self.size()), i)
        self.val = self.val[~filter_]

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

    def __eq__(self, other):
        return other == self.val


class HeaderValues(object):
    def __init__(self):
        self._subsect = None

    def set_vars(self, subsect):
        self._subsect = subsect

    def get_value(self, var):
        return self._subsect[var].val

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

    def __contains__(self, item):
        if self._subsect is None:
            return False
        else:
            return item in self._subsect
