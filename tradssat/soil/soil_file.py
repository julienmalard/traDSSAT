from tradssat.tmpl import InpFile
from .soil_vars import vars_


class SoilFile(InpFile):
    ext = '.SOL'

    def _get_var_info(self):
        return vars_

