from tradssat.tmpl import InpFile
from .cli_vars import vars_


class CLIFile(InpFile):
    """
    Reader for DSSAT climate (.CLI) files.
    """

    ext = ['.CLI']

    def _get_var_info(self):
        return vars_
