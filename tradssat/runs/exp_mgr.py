from tradssat import ExpFile
from tradssat.exper.exper_vars import TRT_HEAD
from .mgr import PeriphFileMgr


class ExpFileMgr(PeriphFileMgr):

    def __init__(self, file):
        self.file = ExpFile(file)

    def get_file_val(self, var, subsect=None, sect=None):
        return self.file.get_value(var, subsect=subsect, sect=sect)

    def set_file_val(self, var, val, subsect=None, sect=None, cond=None):
        self.file.set_value(var, val, sect=sect, subsect=subsect, cond=cond)

    def get_trt_nums(self):
        return self.file.get_value('N', sect=TRT_HEAD)

    def get_trt_names(self):
        return self.file.get_value('TNAME', sect=TRT_HEAD)

    def add_row(self, sect, subsect=None, vals=None):
        self.file.add_row(sect=sect, subsect=subsect, vals=vals)

    def remove_row(self, sect, subsect=None, cond=None):
        self.file.remove_row(sect=sect, subsect=subsect, cond=cond)

    def find_var_sect(self, var):
        return self.file.find_var_sect(var)

    def get_value(self, var, level):
        sect = self.file.find_var_sect(var)
        lv_cd = _level_codes[_factor_to_code[sect]]

        return self.file.get_value(var, sect=sect, cond={lv_cd: level})

    def set_value(self, var, val, level):
        sect = self.file.find_var_sect(var)
        lv_cd = _level_codes[_factor_to_code[sect]]

        self.file.set_value(var, val, sect=sect, cond={lv_cd: level})

    def variables(self):
        return self.file.variables()


_level_codes = {
    'CU': 'C',
    'FL': 'L',
    'SA': 'A',
    'IC': 'C',
    'MP': 'P',
    'MI': 'I',
    'MF': 'F',
    'MR': 'R',
    'MC': 'C',
    'MT': 'T',
    'ME': 'E',
    'MH': 'H',
    'SM': 'N'
}
_factor_codes = {
    'CU': 'CULTIVARS',
    'FL': 'FIELDS',
    'SA': 'SOIL ANALYSIS',
    'IC': 'INITIAL CONDITIONS',
    'MP': 'PLANTING DETAILS',
    'MI': 'IRRIGATION AND WATER MANAGEMENT',
    'MF': 'FERTILIZERS (INORGANIC)',
    'MR': 'RESIDUES AND ORGANIC FERTILIZER',
    'MC': 'CHEMICAL APPLICATIONS',
    'MT': 'TILLAGE AND ROTATIONS',
    'ME': 'ENVIRONMENT MODIFICATIONS',
    'MH': 'HARVEST DETAILS',
    'SM': 'SIMULATION CONTROLS'
}
_factor_to_code = {fct: cd for cd, fct in _factor_codes.items()}
