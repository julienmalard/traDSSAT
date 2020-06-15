import os
import re

import numpy as np

from tradssat.utils import detect_encod
from .vals import FileValueSet, ValueSubSection
from .var import VariableSet, CODE_MISS


class File(object):
    """
    Parent class for all file objects.
    """

    def __init__(self, file):
        """

        Parameters
        ----------
        file: str

        """
        self.file = file
        self._var_info = VariableSet(self._get_var_info())

        self._values = FileValueSet()
        self.encoding = detect_encod(self.file)
        self._read()

    def _read(self):

        with open(self.file, encoding=self.encoding) as f:
            section = []  # To store lines that go in the same section
            for l in f.readlines():

                if l[0] == '!':  # skip comments
                    continue

                if l[0] == '*':  # start of section

                    # Process any previously stored block
                    if section:
                        self._read_section(section)

                    # Clear the current block
                    section.clear()

                if l.strip():
                    section.append(l)  # Append current line to block

            # Read the last block too
            self._read_section(section)

    def get_var_type(self, var, sect=None):
        return self.get_var(var, sect).type_

    def get_var_lims(self, var, sect=None):
        return self.get_var(var, sect).lims

    def get_var_spc(self, var, sect=None, **kwargs):
        return self.get_var(var, sect).spc

    def get_var_size(self, var, sect=None):
        """
        Returns the size of a variable.

        Parameters
        ----------
        var: str
            The name of the variable.
        sect: str
            The name of the section in which this variable appears (optional; for ambiguous cases where a file
            has several variables with the same code).

        Returns
        -------
        int
            The size of the variable.

        """
        return self.get_var(var, sect).size

    def get_var_code_miss(self, var, sect=None):
        return self.get_var(var, sect).miss

    def get_var(self, var, sect=None):
        return self._var_info.get_var(var, sect)

    def get_value(self, var, sect=None, subsect=None, cond=None):
        """

        Parameters
        ----------
        var
        sect
        subsect
        cond

        Returns
        -------
        np.ndarray
        """
        return self._values.get_value(var, sect=sect, subsect=subsect, cond=cond)

    def get_dims_val(self, var):
        return self.get_value(var).shape

    def add_row(self, sect, subsect=None, vals=None):
        self._values.add_row(sect, subsect, vals)

    def remove_row(self, sect, subsect=None, cond=None):
        self._values.remove_row(sect, subsect, cond)

    def find_var_sect(self, var):
        return self._values.find_var_sect(var)

    def variables(self):
        return list(str(vr) for vr in self._var_info.variables())

    def to_dict(self):
        return self._values.to_dict()

    def _read_subsection(self, section_name, subblock):

        var_names = self._get_var_names(subblock[0])

        n_lines = len(subblock) - 1  # -1 for the header line (with "@" )
        lengths = [self.get_var_size(vr) for vr in var_names]

        spaces = [self.get_var_spc(var = vr,
                                   header = subblock[0]) for vr in var_names]

        cum_lens = np.insert(np.cumsum(lengths) + np.cumsum(spaces), 0, 0)
        cutoffs = [(cum_lens[i], cum_lens[i + 1]) for i in range(len(var_names))]

        d_vals = {vr: self._gen_empty_mtrx(vr, n_lines) for vr in var_names}

        for i, l in enumerate(subblock[1:]):
            # Odd workaround necessary because several cultivar names in DSSAT are larger than the allowed space
            # and so run into the next column, which apparently isn't supposed to matter if the next column's value
            # is small enough to allow both to fit. (Really?!)
            vals = [
                (l[0 if c[0] == 0 else max(c[0], l.find(' ', c[0], c[1] - 1)):
                   None if l.find(' ', c[1] - 1) < 0 else l.find(' ', c[1] - 1)]).strip()
                for c in cutoffs]
            for vr, vl in zip(var_names, vals):
                if not vl:
                    vl = self.get_var_code_miss(vr)
                d_vals[vr][i] = vl

        l_vars = [self._var_info.get_var(vr, sect=section_name) for vr in var_names]
        l_vals = [d_vals[vr] for vr in var_names]
        subsect = ValueSubSection(l_vars, l_vals)

        self._values[section_name].add_subsection(subsect)

    def _read_section(self, section):
        section_name, section_lines = self._process_section_header(section)

        subblock = []
        for l in section_lines:  # skip first line (with "*")
            if l[0] == '@':

                if subblock:
                    self._read_subsection(section_name, subblock)
                subblock.clear()

            # Append current line to section
            if l.strip().strip('\x1a'):  # '\x1a' needed for obscure character DSSAT likes to append to .SNX/SQX
                subblock.append(l)

        if subblock:
            self._read_subsection(section_name, subblock)

    def _gen_empty_mtrx(self, var, size):
        tp = self.get_var_type(var)
        if tp == 'float':
            dtype = float
        elif tp == 'int':
            dtype = int
        elif tp == 'str' or tp == str:
            str_size = self.get_var_size(var)
            dtype = 'U{}'.format(str_size + 5)  # +5 just to be safe (with DSSAT input files you never know)
        else:
            dtype = tp

        return np.full(size, CODE_MISS, dtype=dtype)

    def _get_var_names(self, line):
        var_names = [str(vr) for vr in self._var_info]
        var_names.sort(key=len, reverse=True)

        def _strip(txt):
            return re.sub('^[|.\W]+', '', txt)

        final_names = []
        line = _strip(line[1:])  # skip initial "@"

        while line:
            try:
                name = next(vr for vr in var_names if line.startswith(vr))
            except StopIteration:
                raise ValueError(
                    'No variable matching "{line}" for file {nm}.'.format(
                        line=line[:20], nm=os.path.split(self.file)[1]
                    )
                )
            final_names.append(name)
            line = _strip(line[len(name):])

        return final_names

    def __contains__(self, item):
        return item in self._values

    def _get_var_info(self):
        """
        Return a set of variables.

        Returns
        -------
        set[Variable]
        """

        raise NotImplementedError

    @classmethod
    def matches_file(cls, file):
        """
        Checks whether a given file can be read by this class. Must be implemented in subclasses.

        Parameters
        ----------
        file: str
            The file to be read.

        Returns
        -------
        bool
            ``True`` if the file matches; ``False`` otherwise.
        """

        raise NotImplementedError

    def _process_section_header(self, lines):
        """

        Parameters
        ----------
        lines

        Returns
        -------
        tuple[str, list]
        """

        raise NotImplementedError
