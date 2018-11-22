class PeriphFileMgr(object):
    def get_val(self, var, level):
        raise NotImplementedError

    def set_val(self, var, val, level):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError
