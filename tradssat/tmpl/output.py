import os

from .file import File


class OutFile(File):

    filename = None  # type: str

    def _process_section_header(self, lines):

        section_name = lines[0][1:]
        self._values.add_section(section_name)
        i = 0
        for l in lines:
            if 'TREATMENT' in l:
                trt_no = l.split(' : ')[0].split()[1].strip()
                self._values[section_name].add_header_var('TREATMENT', trt_no)

            elif '@' in l:
                break
            i += 1

        return section_name, lines[i:]

    def _get_var_info(self):
        raise NotImplementedError

    @classmethod
    def matches_file(cls, file):
        fname = os.path.split(file)[1]
        return fname.lower() == cls.filename.lower()
