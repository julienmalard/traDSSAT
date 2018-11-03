from tradssat.tmpl import InpFile
from .exper_vars import vars_


class ExpFile(InpFile):
    ext = ['.MZX', 'PIX']

    def _get_var_info(self):
        return vars_
