from tradssat.file import InpFile
from .soil_vars import vars_


class SoilFile(InpFile):
    def _get_var_info(self):
        return vars_

    def _get_template(self):
        pass

