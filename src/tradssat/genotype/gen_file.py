import os

from tradssat.tmpl import InpFile
from .vars_.alfrm import cul_vars_ALFRM, eco_vars_ALFRM
from .vars_.bacer import cul_vars_BACER, eco_vars_BACER
from .vars_.bacrp import cul_vars_BACRP, eco_vars_BACRP
from .vars_.bhgro import cul_vars_BHGRO, eco_vars_BHGRO
from .vars_.bmfrm import cul_vars_BMFRM, eco_vars_BMFRM
from .vars_.bmgro import cul_vars_BMGRO, eco_vars_BMGRO
from .vars_.bngro import cul_vars_BNGRO, eco_vars_BNGRO
from .vars_.brfrm import cul_vars_BRFRM, eco_vars_BRFRM
from .vars_.brgro import cul_vars_BRGRO, eco_vars_BRGRO
from .vars_.bscer import cul_vars_BSCER, eco_vars_BSCER
from .vars_.cbgro import cul_vars_CBGRO, eco_vars_CBGRO
from .vars_.chgro import cul_vars_CHGRO, eco_vars_CHGRO
from .vars_.cngro import cul_vars_CNGRO, eco_vars_CNGRO
from .vars_.cogro import cul_vars_COGRO, eco_vars_COGRO
from .vars_.cpgro import cul_vars_CPGRO, eco_vars_CPGRO
from .vars_.cscas import cul_vars_CSCAS, eco_vars_CSCAS
from .vars_.csyca import cul_vars_CSYCA, eco_vars_CSYCA
from .vars_.fbgro import cul_vars_FBGRO, eco_vars_FBGRO
from .vars_.g0gro import cul_vars_G0GRO, eco_vars_G0GRO
from .vars_.gbgro import cul_vars_GBGRO, eco_vars_GBGRO
from .vars_.mlcer import cul_vars_MLCER, eco_vars_MLCER
from .vars_.mzcer import cul_vars_MZCER, eco_vars_MZCER
from .vars_.mzixm import cul_vars_MZIXM, eco_vars_MZIXM
from .vars_.pialo import cul_vars_PIALO
from .vars_.pngro import cul_vars_PNGRO, eco_vars_PNGRO
from .vars_.ppgro import cul_vars_PPGRO, eco_vars_PPGRO
from .vars_.prgro import cul_vars_PRGRO, eco_vars_PRGRO
from .vars_.ptsub import cul_vars_PTSUB, eco_vars_PTSUB
from .vars_.ricer import cul_vars_RICER
from .vars_.riorz import cul_vars_RIORZ
from .vars_.sbgro import cul_vars_SBGRO, eco_vars_SBGRO
from .vars_.sccan import cul_vars_SCCAN, eco_vars_SCCAN
from .vars_.sccsp import cul_vars_SCCSP
from .vars_.sfgro import cul_vars_SFGRO, eco_vars_SFGRO
from .vars_.sgcer import cul_vars_SGCER, eco_vars_SGCER
from .vars_.sugro import cul_vars_SUGRO, eco_vars_SUGRO
from .vars_.swcer import cul_vars_SWCER, eco_vars_SWCER
from .vars_.tmgro import cul_vars_TMGRO, eco_vars_TMGRO
from .vars_.tnaro import cul_vars_TNARO
from .vars_.traro import cul_vars_TRARO
from .vars_.vbgro import cul_vars_VBGRO, eco_vars_VBGRO
from .vars_.whaps import cul_vars_WHAPS, eco_vars_WHAPS
from .vars_.whcer import cul_vars_WHCER, eco_vars_WHCER
from .vars_.whcrp import cul_vars_WHCRP, eco_vars_WHCRP

vars_gen = {
    'ALFRM': {'.cul': cul_vars_ALFRM, '.eco': eco_vars_ALFRM},
    'BACER': {'.cul': cul_vars_BACER, '.eco': eco_vars_BACER},
    'BACRP': {'.cul': cul_vars_BACRP, '.eco': eco_vars_BACRP},
    'BHGRO': {'.cul': cul_vars_BHGRO, '.eco': eco_vars_BHGRO},
    'BMFRM': {'.cul': cul_vars_BMFRM, '.eco': eco_vars_BMFRM},
    'BMGRO': {'.cul': cul_vars_BMGRO, '.eco': eco_vars_BMGRO},
    'BNGRO': {'.cul': cul_vars_BNGRO, '.eco': eco_vars_BNGRO},
    'BRFRM': {'.cul': cul_vars_BRFRM, '.eco': eco_vars_BRFRM},
    'BRGRO': {'.cul': cul_vars_BRGRO, '.eco': eco_vars_BRGRO},
    'BSCER': {'.cul': cul_vars_BSCER, '.eco': eco_vars_BSCER},
    'CBGRO': {'.cul': cul_vars_CBGRO, '.eco': eco_vars_CBGRO},
    'CHGRO': {'.cul': cul_vars_CHGRO, '.eco': eco_vars_CHGRO},
    'CNGRO': {'.cul': cul_vars_CNGRO, '.eco': eco_vars_CNGRO},
    'COGRO': {'.cul': cul_vars_COGRO, '.eco': eco_vars_COGRO},
    'CPGRO': {'.cul': cul_vars_CPGRO, '.eco': eco_vars_CPGRO},
    'CSCAS': {'.cul': cul_vars_CSCAS, '.eco': eco_vars_CSCAS},
    'CSYCA': {'.cul': cul_vars_CSYCA, '.eco': eco_vars_CSYCA},
    'FBGRO': {'.cul': cul_vars_FBGRO, '.eco': eco_vars_FBGRO},
    'G0GRO': {'.cul': cul_vars_G0GRO, '.eco': eco_vars_G0GRO},
    'GBGRO': {'.cul': cul_vars_GBGRO, '.eco': eco_vars_GBGRO},
    'MLCER': {'.cul': cul_vars_MLCER, '.eco': eco_vars_MLCER},
    'MZCER': {'.cul': cul_vars_MZCER, '.eco': eco_vars_MZCER},
    'MZIXM': {'.cul': cul_vars_MZIXM, '.eco': eco_vars_MZIXM},
    'PIALO': {'.cul': cul_vars_PIALO},
    'PNGRO': {'.cul': cul_vars_PNGRO, '.eco': eco_vars_PNGRO},
    'PPGRO': {'.cul': cul_vars_PPGRO, '.eco': eco_vars_PPGRO},
    'PRGRO': {'.cul': cul_vars_PRGRO, '.eco': eco_vars_PRGRO},
    'PTSUB': {'.cul': cul_vars_PTSUB, '.eco': eco_vars_PTSUB},
    'RICER': {'.cul': cul_vars_RICER},
    'RIORZ': {'.cul': cul_vars_RIORZ},
    'SBGRO': {'.cul': cul_vars_SBGRO, '.eco': eco_vars_SBGRO},
    'SCCAN': {'.cul': cul_vars_SCCAN, '.eco': eco_vars_SCCAN},
    'SCCSP': {'.cul': cul_vars_SCCSP},
    'SFGRO': {'.cul': cul_vars_SFGRO, '.eco': eco_vars_SFGRO},
    'SGCER': {'.cul': cul_vars_SGCER, '.eco': eco_vars_SGCER},
    'SUGRO': {'.cul': cul_vars_SUGRO, '.eco': eco_vars_SUGRO},
    'SWCER': {'.cul': cul_vars_SWCER, '.eco': eco_vars_SWCER},
    'TNARO': {'.cul': cul_vars_TNARO},
    'TMGRO': {'.cul': cul_vars_TMGRO, '.eco': eco_vars_TMGRO},
    'TRARO': {'.cul': cul_vars_TRARO},
    'VBGRO': {'.cul': cul_vars_VBGRO, '.eco': eco_vars_VBGRO},
    'WHAPS': {'.cul': cul_vars_WHAPS, '.eco': eco_vars_WHAPS},
    'WHCER': {'.cul': cul_vars_WHCER, '.eco': eco_vars_WHCER},
    'WHCRP': {'.cul': cul_vars_WHCRP, '.eco': eco_vars_WHCRP},
}


class GenFile(InpFile):
    """
    Template for genotype input file readers.
    """
    ext = None  # type: str

    def _get_var_info(self):
        file = os.path.split(self.file)[1]

        for gen, d_gen in vars_gen.items():
            if file.startswith(gen):
                try:
                    return d_gen[self.ext.lower()]
                except KeyError:
                    break

        raise ValueError(
            'No {ext} variables defined for {f} cropping model.'.format(ext=self.ext, f=os.path.splitext(file)[0])
        )


class CULFile(GenFile):
    """
    Cultivar (.CUL) input file reader.
    """
    ext = '.CUL'


class ECOFile(GenFile):
    """
    Ecotype (.ECO) input file reader.
    """
    ext = '.ECO'
