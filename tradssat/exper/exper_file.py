from tradssat.tmpl import InpFile
from .exper_vars import main_vars, header_vars


class ExpFile(InpFile):
    """
    File reader for all DSSAT (.ccX) experiment files.
    """
    ext = [
        '.ALX', '.ARX', '.BAX', '.BNX', '.BWX', '.COX', '.CSX', '.FAX', '.GWX', '.MLX', '.MZX', '.PIX', '.PNX', '.PTX',
        '.RIX', '.SBX', '.SCX', '.SGX', '.STX', '.WHX', '.SQX', '.SNX'
    ]  # Todo: add all DSSAT 47 crop extension codes

    def _get_var_info(self):
        return main_vars

    def _get_header_vars(self):
        return {'EXP.DETAILS: ': header_vars}
