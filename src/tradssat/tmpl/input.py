import os

from .file import File
from .vals import ValueSubSection
from .var import HeaderVariableSet


class InpFile(File):
    """
    Parent class for all input files, as well as for `Summary.OUT`.
    """

    ext = None  # type: str

    def __init__(self, file):
        self._header_vars = HeaderVariableSet(self._get_header_vars())
        super().__init__(file)

    def write(self, file, force=False, check=True):
        lines = []

        write = force or file != self.file or self.changed()

        if write:
            self._values.write(lines)

            with open(file, 'w', encoding=self.encoding) as f:
                f.writelines(l + "\n" for l in lines)

    def set_value(self, var, val, sect=None, subsect=None, cond=None):
        self._values.set_value(var, val, sect=sect, subsect=subsect, cond=cond)

    def changed(self):
        """
        Checks whether the file has been edited and needs to be rewritten.

        Returns
        -------
        bool
            Whether the file has been edited or not.
        """
        return self._values.changed()

    def get_var(self, var, sect=None):
        try:
            return super().get_var(var, sect=sect)
        except ValueError:
            return self._header_vars.get_var(var, sect=sect)

    def _process_section_header(self, lines):

        if lines[0][0] == '@':  # In case a section header is missing
            self._values.add_section('')
            return '', lines

        header_text = lines[0][1:].strip()  # Skip initial "*"

        match = self._header_vars.matches(header_text)
        if match:

            section_name = match.strip()
            self._values.add_section(section_name)
            header_text = header_text[len(match):]

            h_vars = self._header_vars.get_vars(match)

            l_vals = []
            for vr in h_vars:
                size = vr.size + vr.spc
                val = header_text[:size].strip()

                matr = self._gen_empty_mtrx(str(vr), size=1)
                matr[:] = val

                l_vals.append(matr)

                header_text = header_text[size:]

            header_vars_subsect = ValueSubSection(h_vars, l_vals=l_vals)
            self._values[section_name].set_header_vars(header_vars_subsect)

            return match, lines[1:]

        self._values.add_section(header_text)
        return header_text, lines[1:]

    def _get_header_vars(self):
        return {}

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

        ext = os.path.splitext(file)[1]
        if isinstance(cls.ext, str):
            return ext.lower() == cls.ext.lower()
        return ext.lower() in [x.lower() for x in cls.ext]

    def _get_var_info(self):
        raise NotImplementedError
