import os

import numpy as np

from .file import File


class InpFile(File):
    ext = None  # type: str

    def write(self, file, force=False, check=True):
        lines = []

        write = force or file != self.file or self.changed()

        if write:
            self._values.write(lines, self._var_info)

            with open(file, 'w', encoding=self.encoding) as f:
                f.writelines(l + "\n" for l in lines)

    def set_val(self, var, val, sect=None, subsect=None, cond=None):
        self._values.set_val(var, val, sect=sect, subsect=subsect, cond=cond)

    def changed(self):
        return self._values.changed()

    def _process_section_header(self, lines):

        section_name = lines[0][1:].strip()
        self._values.add_section(section_name)

        return section_name, lines[1:]

    @classmethod
    def matches_file(cls, file):
        ext = os.path.splitext(file)[1]
        if isinstance(cls.ext, str):
            return ext.lower() == cls.ext.lower()
        else:
            return ext.lower() in [x.lower() for x in cls.ext]

    def _get_var_info(self):
        raise NotImplementedError
