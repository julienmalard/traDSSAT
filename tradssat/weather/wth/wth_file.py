from tradssat.tmpl import InpFile
from .wth_vars import vars_


class WTHFile(InpFile):
    """
    Reader for DSSAT weather (.WTH and .WTG) files.
    """

    ext = ['.WTH', '.WTG']

    def _get_var_info(self):
        return vars_
