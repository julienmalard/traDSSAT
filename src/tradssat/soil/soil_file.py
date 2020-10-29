import re

from tradssat.tmpl import InpFile
from .soil_vars import main_vars, header_vars


class SoilFile(InpFile):
    """
    File reader for soil (.SOL) DSSAT files.
    """
    ext = '.SOL'

    def _get_var_info(self):
        return main_vars

    def _get_header_vars(self):
        return {re.compile('[A-Z0-9]{10}'): header_vars}
