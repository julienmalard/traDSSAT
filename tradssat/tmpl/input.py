import numpy as np
import numpy.testing as npt
from tradssat.tmpl.var import Variable, VariableSet


class InpFile(object):
    ext = None

    def __init__(self, file):
        self.file = file
        self.var_info = VariableSet(self._get_var_info())

        self._values = FileValueSet()
        self._read()

    def _read(self):

        with open(self.file, encoding='utf8') as f:
            section = []  # To store lines that go in the same section
            for l in f.readlines():

                if l[0] == '!':  # skip comments
                    continue

                if l[0] == '*':  # start of section

                    # Process any previously stored block
                    if len(section):
                        self._read_section(section)

                    # Clear the current block
                    section.clear()

                if len(l.strip()):
                    section.append(l)  # Append current line to block

            # Read the last block too
            self._read_section(section)

    def write(self, file, check=True):
        lines = []

        self._values.write(lines, self.var_info)

        with open(file, 'w', encoding='utf8') as f:
            f.writelines(l + "\n" for l in lines)

    def to_dict(self):
        return self._values.to_dict()

    def get_val(self, var):
        return self._values[var]['val']

    def get_dims_val(self, var):
        return self.get_val(var).shape

    def set_var(self, var, val):
        if isinstance(val, np.ndarray) and val.shape != self.get_dims_val(var):
            self._values[var] = val
        else:
            self._values[var][:] = val

    def get_var_section(self, var):
        return self.var_info[var].sect

    def get_var_type(self, var):
        return self.var_info[var].type_

    def get_var_spc(self, var):
        return self.var_info[var].spc

    def get_var_size(self, var):
        return self.var_info[var].size

    def get_var_lims(self, var):
        return self.var_info[var].lims

    def _read_section(self, section):
        section_name = self._get_sect_name(section[0])
        self._values.add_section(section_name)

        subblock = []
        for l in section[1:]:  # skip first line (with "*")
            if l[0] == '@':

                if len(subblock):
                    self._read_subsection(section_name, subblock)
                subblock.clear()

            # Append current line to section
            if len(l.strip()):
                subblock.append(l)

        if len(subblock):
            self._read_subsection(section_name, subblock)

    def _read_subsection(self, section_name, subblock):
        var_names = self._get_var_names(subblock[0])
        n_lines = len(subblock) - 1  # -1 for the header line (with "@" )
        lengths = [self.get_var_size(vr) for vr in var_names]
        spaces = [self.get_var_spc(vr) for vr in var_names]
        cum_lens = np.insert(np.cumsum(lengths) + np.cumsum(spaces), 0, 0)
        cutoffs = [(cum_lens[i], cum_lens[i + 1] + 1) for i in range(len(var_names))]

        d_vals = {vr: self._gen_empty_mtrx(vr, n_lines) for vr in var_names}

        for i, l in enumerate(subblock[1:]):
            vals = [l[c[0]:c[1]].strip() for c in cutoffs]
            for vr, vl in zip(var_names, vals):
                if not len(vl):
                    vl = -99
                d_vals[vr][i] = vl

        subsect = ValueSubSection()
        for vr in var_names:
            subsect.set_value(vr, d_vals[vr])

        self._values[section_name].add_subsection(subsect)

    def _gen_empty_mtrx(self, var, size):
        tp = self.get_var_type(var)
        if tp == 'float':
            dtype = float
        elif tp == 'int':
            dtype = int
        elif tp == 'str' or tp == str:
            str_size = self.get_var_size(var)
            dtype = f'U{str_size}'
        else:
            dtype = tp

        return np.full(size, -99, dtype=dtype)

    @staticmethod
    def _get_sect_name(line):
        return line[1:].strip()

    def _get_var_names(self, line):
        names = [x.strip('.') for x in line[1:].split()]  # skip initial "@"
        final_names = []
        to_skip = []
        for i, vr in enumerate(names):
            if vr in to_skip:
                continue
            if vr in self.var_info:
                final_names.append(vr)
            elif i != len(names) - 1 and '{} {}'.format(vr, names[i+1]) in self.var_info:
                final_names.append('{} {}'.format(vr, names[i+1]))
                to_skip.append(names[i+1])
            else:
                raise ValueError('Variable "{}" does not exist.'.format(vr))
        return final_names

    def equals(self, other):
        self._values.equals(other._values)

    def __eq__(self, other):
        return self._values == other._values

    def _get_var_info(self):
        """
        Return a dictionary of variable information.

        Returns
        -------
        set[Variable]
        """

        raise NotImplementedError


class FileValueSet(object):
    def __init__(self):
        self._sections = {}

    def add_section(self, name):
        self._sections[name] = ValueSection(name)

    def write(self, lines, var_info):

        for s in self:
            s.write(lines, var_info)

        lines.append('')

        return lines

    def __iter__(self):
        for s in self._sections.values():
            yield s

    def __getitem__(self, item):
        return self._sections[item]

    def __eq__(self, other):
        return all(s1 == s2 for s1, s2 in zip(self, other))

    def equals(self, other):
        for s1, s2 in zip(self, other):
            s1.equals(s2)

    def to_dict(self):
        return {name: sect.to_dict() for name, sect in self._sections.items()}


class ValueSection(object):
    def __init__(self, name):
        self.name = name
        self._subsections = []

    def add_subsection(self, subsect):
        self._subsections.append(subsect)

    def write(self, lines, var_info):
        lines.append('*' + self.name)
        for s in self:
            s.write(lines, var_info)

        lines.append('')

        return lines

    def __iter__(self):
        for s in self._subsections:
            yield s

    def __setitem__(self, key, value):
        for subsect in self:
            if key in subsect:
                subsect[key] = value

    def __eq__(self, other):
        return all(s1 == s2 for s1, s2 in zip(self, other))

    def equals(self, other):
        for s1, s2 in zip(self, other):
            s1.equals(s2)

    def to_dict(self):
        return [subsect.to_dict() for subsect in self]


class ValueSubSection(object):
    def __init__(self):
        self._values = {}

    def set_value(self, var, val):
        if isinstance(val, np.ndarray) and (var not in self or val.shape != self[var].shape):
            self._values[var] = val
        else:
            self[var][:] = val

    def check_dims(self):
        return len(np.unique([v.shape for v in self._values.values()])) == 1

    def check_vals(self, var_info):
        for vr in self:
            var_info[vr].check_val(self[vr])

    def n_data(self):
        self.check_dims()
        return self[list(self._values)[0]].size

    def write(self, lines, var_info):
        self.check_dims()
        self.check_vals(var_info)

        lines.append('@' + ''.join([var_info[vr].write() for vr in self]))
        for i in range(self.n_data()):
            lines.append(''.join([var_info[vr].write(self[vr][i]) for vr in self]))

        return lines

    def to_dict(self):
        return self._values

    def __iter__(self):
        for vr in self._values:
            yield vr

    def __contains__(self, item):
        return item in self._values

    def __getitem__(self, item):
        return self._values[item]

    def __setitem__(self, key, value):
        self.set_value(key, value)

    def __eq__(self, other):
        return set(self) == set(other) and all(np.array_equal(self[vr], other[vr]) for vr in self)

    def equals(self, other):
        missing = set(self) - set(other)
        if len(missing):
            raise ValueError('Missing variables:' + ', '.format(missing))
        for vr in self:
            npt.assert_equal(self[vr], other[vr], err_msg=vr)
