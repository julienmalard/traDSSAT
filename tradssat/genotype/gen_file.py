import os

from tradssat.tmpl import InpFile

from .alfrm import cul_vars_ALFRM, eco_vars_ALFRM
from .bacer import cul_vars_BACER, eco_vars_BACER
from .cscas import cul_vars_CSCAS, eco_vars_CSCAS
from .mzcer import cul_vars_MZCER, eco_vars_MZCER
from .pialo import cul_vars_PIALO, eco_vars_PIALO
from .swcer import cul_vars_SWCER, eco_vars_SWCER
from .tnaro import cul_vars_TNARO

vars_gen = {
    'ALFRM': {'cul': cul_vars_ALFRM, 'eco': eco_vars_ALFRM},
    'BACER': {'cul': cul_vars_BACER, 'eco': eco_vars_BACER},
    'CSCAS': {'cul': cul_vars_CSCAS, 'eco': eco_vars_CSCAS},
    'MZCER': {'cul': cul_vars_MZCER, 'eco': eco_vars_MZCER},
    'SWCER': {'cul': cul_vars_SWCER, 'eco': eco_vars_SWCER},
    'TNARO': {'cul': cul_vars_TNARO},
    'PIALO': {'cul': cul_vars_PIALO, 'eco': eco_vars_PIALO},

}


class CULFile(InpFile):
    ext = '.CUL'

    def _get_var_info(self):
        file = os.path.split(self.file)[1]

        for gen, d_gen in vars_gen.items():
            if file.startswith(gen):
                try:
                    return d_gen['cul']
                except KeyError:
                    break

        raise ValueError(
            'No cultivar variables defined for {} cropping model.'.format(os.path.splitext(file)[0])
        )


class ECOFile(InpFile):
    ext = '.ECO'

    def _get_var_info(self):
        file = os.path.split(self.file)[1]

        for gen, d_gen in vars_gen.items():
            if file.startswith(gen):
                try:
                    return d_gen['eco']
                except KeyError:
                    break

        raise ValueError(
            'No ecotype variables defined for {} cropping model.'.format(os.path.splitext(file)[0])
        )
