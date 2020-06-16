import os
import re

import numpy as np

from .file import File
from .input import InpFile
from .vals import ValueSubSection


class OutFile(File):
    """
    Parent class for (nearly all) DSSAT output files.
    """

    filename = None  # type: str

    def __init__(self, folder):
        if os.path.isdir(folder):
            file = os.path.join(folder, self.filename)
        else:
            file = folder

        super().__init__(file)

    def _process_section_header(self, lines):

        section_name = lines[0][1:]
        self._values.add_section(section_name)
        i = 0
        run_no = None
        for l in lines:
            if "RUN" in l:

                run_no = l.split(' : ')[0].strip()
                run_no = re.search('\d+$', run_no).group(0)

            if 'TREATMENT' in l:

                trt_no = l.split(' : ')[0].strip()
                trt_no = re.search('\d+$', trt_no).group(0)
                
                if run_no is None:
                    l_vals = np.array([trt_no], dtype=int)
                    l_vars = ['TREATMENT']
                else:
                    l_vals = np.array([run_no, trt_no], dtype=int)
                    l_vars = ['RUN', 'TREATMENT']
                subsect = ValueSubSection(l_vars, l_vals=l_vals)
                self._values[section_name].set_header_vars(subsect)

            elif '@' in l:
                break
            i += 1

        return section_name, lines[i:]

    def _get_var_info(self):
        raise NotImplementedError

    @classmethod
    def matches_file(cls, file):
        """
        Checks whether a given file can be read by this class.

        Parameters
        ----------
        file: str
           The filename or full path to be read.

        Returns
        -------
        bool
           ``True`` if the file matches; ``False`` otherwise.
        """

        fname = os.path.split(file)[1]
        return fname.lower() == cls.filename.lower()

    def get_var_spc(self, var, sect=None, **kwargs):

        header = kwargs.get('header')

        match = re.search(var, header)
        spc = re.search("[ @]+$", header[:(match.start())]).group(0)
        return len(spc)


class FinalOutFile(InpFile):
    filename = None  # type: str

    def __init__(self, folder):
        if os.path.isdir(folder):
            file = os.path.join(folder, self.filename)
        else:
            file = folder

        super().__init__(file)

    @classmethod
    def matches_file(cls, file):
        fname = os.path.split(file)[1]
        return fname.lower() == cls.filename.lower()

    def _get_var_info(self):
        raise NotImplementedError
