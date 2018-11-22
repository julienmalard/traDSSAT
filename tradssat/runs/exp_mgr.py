from tradssat import ExpFile
from tradssat.exper.exper_vars import TRT_HEAD
from .mgr import PeriphFileMgr


class ExpFileMgr(PeriphFileMgr):
    def __init__(self, file):
        self.file = ExpFile(file)

    def get_file_val(self, var, subsect=None, sect=None):
        return self.file.get_val(var, subsect=subsect, sect=sect)

    def set_file_val(self, var, val, subsect=None, sect=None, cond=None):
        self.file.set_val(var, val, sect=sect, subsect=subsect, cond=cond)

    def get_trt_nums(self):
        return self.file.get_val('N', sect=TRT_HEAD)

    def get_trt_names(self):
        return self.file.get_val('TNAME', sect=TRT_HEAD)

    def add_row(self, sect, subsect=None, vals=None):
        self.file.add_row(sect=sect, subsect=subsect, vals=vals)

    def remove_row(self, sect, subsect=None, cond=None):
        self.file.remove_row(sect=sect, subsect=subsect, cond=None)

    def get_val(self, var, level):
        pass

    def set_val(self, var, val, level):
        pass

    def find_var_sect(self, var):
        self.file.find_var_sect(var)
