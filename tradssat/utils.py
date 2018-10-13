import numpy as np


class InpFile(object):
    def __init__(self, file):
        self.file = file
        self.var_info = self._get_var_info()
        self.template = self._get_template()

        self.structure = {}
        self.dict_vars = {}
        self._read()

    def _read(self):
        with open(self.file, encoding='utf8') as f:
            block = []  # To store lines that go in the same section
            for l in f.read():

                if l[0] == '!':  # skip comments
                    pass

                if l[0] == '*':  # start of section

                    # Process any previously stored block
                    if len(block):
                        self._read_section(block)

                    # Clear the current block
                    block.clear()

                # Append current line to block
                if len(l.strip()):
                    block.append(l)

            # Read the last block too
            self._read_section(block)

        # Convert to variable-by-variable dictionary
        self._gen_dict_vars()

    def write(self, file, check=True):
        lines = []

        for sect_line, subs in self.template.items():
            lines.append(sect_line)

            for sub_line, sub_templt in subs:
                lines.append(sub_line)
                var_names = self._get_var_names(sub_line)
                dims = [self.get_dims_val(vr) for vr in var_names]
                if not np.unique(dims).size == 1:
                    raise ValueError(
                        'Not all variables in the same subsection have the same dimensions:'
                        '\n\t{}'.format(', '.join([f'{vr}: {dm}' for vr, dm in zip(var_names, dims)]))
                    )
                dims = self.get_dims_val(var_names[0])
                if check:
                    for vr in var_names:
                        rng = self.get_var_range(vr)
                        val = self.get_val(vr)
                        if rng is not None:
                            errs = np.where(np.logical_or(np.greater(val, rng[1]), np.less(val, rng[0])))
                            if len(errs):
                                raise ValueError(
                                    f'Variable {vr} out of bounds at values: {val[errs]}!'
                                )

                for i in range(dims):
                    d_vals = {}
                    for vr in var_names:
                        d_vals[vr] = self.get_val(vr)[i]
                    lines.append(sub_templt.format(**d_vals))

            lines.append('')

        with open(file, encoding='utf8') as f:
            f.writelines(lines)

    def get_val(self, var):
        return self.dict_vars[var]['val']

    def get_dims_val(self, var):
        return self.get_val(var).shape

    def set_var(self, var, val):
        if isinstance(val, np.ndarray) and val.shape != self.get_dims_val(var):
            self.dict_vars[var] = val
            section_name = self.get_section_var(var)
            self.structure[section_name][var] = val
        else:
            self.dict_vars[var]['val'][:] = val

    def get_section_var(self, var):
        return self.var_info[var]['section']

    def get_type_var(self, var):
        return self.var_info[var]['type']

    def get_size_var(self, var):
        return self.var_info[var]['size']

    def get_var_range(self, var):
        if 'range' in self.var_info[var]:
            return self.var_info[var]['range']
        else:
            return None

    def _read_section(self, block):
        section_name = self._get_sect_name(block[0])
        self.structure[section_name] = {}

        subblock = []
        for l in block:
            if l[0] == '@':

                if len(subblock):
                    self._read_subsection(section_name, subblock)
                subblock.clear()

        self._read_subsection(section_name, subblock)

    def _read_subsection(self, section_name, subblock):
        var_names = self._get_var_names(subblock[0])
        n_lines = len(subblock) - 1  # -1 for the header line (with "@")
        d_vars = self.structure[section_name]
        cum_len = np.cumsum([0] + [self.get_size_var(vr) for vr in var_names])
        cutoffs = [(cum_len[i], cum_len[i + 1]) for i in range(len(var_names))]

        for vr in var_names:
            d_vars[vr] = self._gen_empty_mtrx(vr, n_lines)
        for i, l in enumerate(subblock[1:]):
            vals = [l[c[0]:c[1]] for c in cutoffs]
            for vr, vl in zip(var_names, vals):
                d_vars[vr][i] = vl

    def _gen_dict_vars(self):
        self.dict_vars.clear()
        for section, d_sect in self.structure.items():
            for var, val in d_sect.items():
                self.dict_vars[var] = {
                    'val': val, 'section': section
                }

    def _gen_empty_mtrx(self, var, size):
        tp = self.get_type_var(var)
        if tp == 'float':
            dtype = float
        elif tp == 'int':
            dtype = int
        elif tp == 'str':
            size = self.get_size_var(var)
            dtype = f'U{size}'
        else:
            raise TypeError(
                f'Type {tp} for variable "{var}" is not recognised. Must be one of `int`, `float`, or `str`.'
            )

        return np.empty(size, dtype=dtype)

    @staticmethod
    def _get_sect_name(line):
        return line[1:].strip()

    @staticmethod
    def _get_var_names(line):
        return line.split()

    def _get_var_info(self):
        """
        Return a dictionary of variable information.

        Returns
        -------
        dict
            Dictionary with variable names as keys, and values as dictionaries with keys `section`, `type` and `size`.
        """

        raise NotImplementedError

    def _get_template(self):
        raise NotImplementedError
