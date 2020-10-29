import os

import numpy as np

from tradssat import CULFile, ECOFile
from .mgr import get_dssat_subdir, PeriphFileMgr


class PeriphGenMgr(PeriphFileMgr):

    def __init__(self, crops, cultivars, levels, model=None):
        self.crops = crops
        self.cultivars = cultivars

        self.files = {
            lvl: GeneticMgr(_get_model(crp, model), cult) for lvl, crp, cult in zip(levels, crops, cultivars)
        }

    def get_value(self, var, level):
        return self.files[level].get_value(var)

    def set_value(self, var, val, level):
        return self.files[level].set_value(var, val)

    def variables(self):
        return {str(vr) for f in self.files.values() for vr in f.variables()}


class GeneticMgr(object):

    def __init__(self, crop, cult):
        self.crop = crop
        self.cult = cult

        geno_dir = get_dssat_subdir('Genotype')

        self.eco_file = self.cult_file = None
        for f in os.listdir(geno_dir):
            name = os.path.split(f)[1]
            if CULFile.matches_file(name) and name.startswith(self.crop):
                self.cult_file = CULFile(os.path.join(geno_dir, f))
            elif ECOFile.matches_file(name) and name.startswith(self.crop):
                self.eco_file = ECOFile(os.path.join(geno_dir, f))

            if self.eco_file is not None and self.cult_file is not None:
                break

        if self.cult_file is None:
            raise ValueError('No cultivar file (.CUL) found for crop "{}".'.format(self.crop))

        eco_codes = self.cult_file.get_value('ECO#')
        cult_codes = self.cult_file.get_value('VAR#')
        if self.cult not in cult_codes:
            raise ValueError('Cultivar {} not found in cultivar file (.CUL).'.format(self.cult))
        eco = eco_codes[cult_codes == self.cult]

        self.eco_n = np.where(self.eco_file.get_value('ECO#') == eco)
        self.cult_n = np.where(cult_codes == cult)

    def get_value(self, var):
        if var in self.cult_file.variables():
            return self.cult_file.get_value(var, cond={'VAR#': self.cult})
        elif self.eco_file is not None and var in self.eco_file.variables():
            return self.eco_file.get_value(var)
        else:
            raise ValueError('No genetic variable named "{}" was found.'.format(var))

    def set_value(self, var, val):
        if var in self.cult_file.variables():
            return self.cult_file.set_value(var, val)
        elif self.eco_file is not None and var in self.eco_file.variables():
            return self.eco_file.set_value(var, val)
        else:
            raise ValueError('No genetic variable named "{}" was found.'.format(var))

    def variables(self):
        vars_ = {*self.cult_file.variables()}
        if self.eco_file is not None:
            vars_.update(self.eco_file.variables())

        return vars_


_crop_models = {
    'AL': ['ALFRM'],
    'BA': ['BACER', 'BACRP'],
    'BH': ['BHGRO'],
    'BM': ['BMFRM', 'BMGRO'],
    'BN': ['BNGRO'],
    'BR': ['BRFRM', 'BRGRO'],
    'BS': ['BSCER'],
    'CB': ['CBGRO'],
    'CH': ['CHGRO'],
    'CN': ['CNGRO'],
    'CO': ['COGRO'],
    'CP': ['CPGRO'],
    'CS': ['CSCAS', 'CSYCA'],
    'FB': ['FBGRO'],
    'G0': ['G0GRO'],
    'GB': ['GBGRO'],
    'ML': ['MLCER'],
    'MZ': ['MZCER', 'MZIXM'],
    'PI': ['PIALO'],
    'PN': ['PNGRO'],
    'PP': ['PPGRO'],
    'PR': ['PRGRO'],
    'PT': ['PTSUB'],
    'RI': ['RICER', 'RIORZ'],
    'SB': ['SBGRO'],
    'SC': ['SCCAN', 'SCCSP'],
    'SF': ['SFGRO'],
    'SG': ['SGCER'],
    'SU': ['SUGRO'],
    'SW': ['SWCER'],
    'TM': ['TMGRO'],
    'TN': ['TNARO'],
    'VB': ['VBGRO'],
    'WH': ['WHAPS', 'WHCER', 'WHCRP']
}


def _get_model(crop, mod):
    try:
        m = _crop_models[crop]
    except KeyError:
        raise ValueError('No model defined for crop "{}" in traDSSAT.'.format(crop))
    if mod in m:
        return mod
    else:
        return m[0]
