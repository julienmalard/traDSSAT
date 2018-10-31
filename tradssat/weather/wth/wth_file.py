from tradssat.file.input import InpFile
from .wth_vars import vars_


class WTHFile(InpFile):
    ext = ['.WTH', '.WTG']

    def _get_var_info(self):
        return vars_

    def _get_template(self):
        pass
