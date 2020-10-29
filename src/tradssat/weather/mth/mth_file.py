from tradssat.tmpl import InpFile
from .mth_vars import vars_


class MTHFile(InpFile):
    """
    Reader for DSSAT monthly weather (.MTH) files.
    """

    ext = '.MTH'

    def _get_var_info(self):
        return vars_
