import os

from tradssat import get_dssat_dir


class PeriphFileMgr(object):
    def get_value(self, var, level):
        raise NotImplementedError

    def set_value(self, var, val, level):
        raise NotImplementedError

    def variables(self):
        raise NotImplementedError


def get_dssat_subdir(subdir):
    dssat_dir = get_dssat_dir()
    if dssat_dir is not None:
        return os.path.join(dssat_dir, subdir)
    else:
        raise FileNotFoundError('No DSSAT directory available.')
