import os
import re

import numpy as np

from .file import File


class InpFile(File):
    ext = None  # type: str

    def __init__(self, file):
        self._header_vars = self._get_header_vars()
        super().__init__(file)

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

        header_text = lines[0][1:].strip()

        for txt, h_vars in self._header_vars.items():
            match = _header_matches(txt, header_text)
            if match is not False:
                section_name = match.strip()
                self._values.add_section(section_name)
                header_text = header_text[len(match):]

                for vr in h_vars:
                    val = header_text[:vr.size].strip()
                    header_text = header_text[vr.size:]
                    self._values[section_name].add_header_var(vr, val)
                return match, lines[1:]

        self._values.add_section(header_text)
        return header_text, lines[1:]

    def _write_section_header(self):
        pass

    def _get_header_vars(self):
        return {}

    @classmethod
    def matches_file(cls, file):
        ext = os.path.splitext(file)[1]
        if isinstance(cls.ext, str):
            return ext.lower() == cls.ext.lower()
        else:
            return ext.lower() in [x.lower() for x in cls.ext]

    def _get_var_info(self):
        raise NotImplementedError


def _header_matches(pattern, header):
    if isinstance(pattern, re.Pattern):
        m = re.match(pattern, header)
        if m:
            return m.group()
        else:
            return False
    else:
        return pattern if header.startswith(pattern) else False
