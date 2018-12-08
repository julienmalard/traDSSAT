import os

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
        for l in lines:
            if 'TREATMENT' in l:
                trt_no = l.split(' : ')[0].split()[1].strip()
                subsect = ValueSubSection(['TREATMENT'], l_vals=[np.array([trt_no], dtype=int)])

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
