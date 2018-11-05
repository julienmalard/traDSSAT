from tradssat.tmpl import InpFile
from .gen_vars import cul_vars, eco_vars


class CULFile(InpFile):
    ext = '.CUL'

    def _get_var_info(self):
        return cul_vars


class ECOFile(InpFile):
    ext = '.ECO'

    def _get_var_info(self):
        return eco_vars
