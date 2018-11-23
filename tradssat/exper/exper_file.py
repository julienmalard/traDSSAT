from tradssat.tmpl import InpFile
from .exper_vars import vars_


class ExpFile(InpFile):
    ext = [
        '.ALX', '.ARX', '.BAX', '.BNX', '.BWX', '.COX', '.CSX', '.FAX', '.GWX', '.MLX', '.MZX', '.PIX', '.PNX', '.PTX',
        '.RIX', '.SBX', '.SCX', '.SGX', '.STX', '.WHX', '.SQX', '.SNX'
    ]  # Todo: add all DSSAT 47 crop extension codes

    def _get_var_info(self):
        return vars_
