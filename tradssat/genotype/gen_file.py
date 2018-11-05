import os

from tradssat.tmpl import InpFile

from . import gen_vars as vrs


class CULFile(InpFile):
    ext = '.CUL'

    def _get_var_info(self):
        file = os.path.split(self.file)[1]
        if self.file.startswith('ALFRM'):
            return vrs.cul_vars_ALFRM
        elif self.file.startswith('PIALO'):
            return vrs.cul_vars_PIALO
        else:
            raise ValueError('No variables defined for {} cropping model.'.format(os.path.splitext(file)[0]))


class ECOFile(InpFile):
    ext = '.ECO'

    def _get_var_info(self):
        file = os.path.split(self.file)[1]
        if file.startswith('ALFRM'):
            return vrs.eco_vars_ALFRM
        elif file.startswith('PIALO'):
            return vrs.eco_vars_PIALO
        else:
            raise ValueError('No variables defined for {} cropping model.'.format(os.path.splitext(file)[0]))
