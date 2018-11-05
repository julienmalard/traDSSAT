import numpy as np

from .file import File


class InpFile(File):

    ext = None

    def write(self, file, check=True):
        lines = []

        self._values.write(lines, self.var_info)

        with open(file, 'w', encoding='utf8') as f:
            f.writelines(l + "\n" for l in lines)

    def set_var(self, var, val):
        if isinstance(val, np.ndarray) and val.shape != self.get_dims_val(var):
            self._values[var] = val
        else:
            self._values[var][:] = val

    def get_var_section(self, var):
        return self.var_info[var].sect

    def get_var_lims(self, var):
        return self.var_info[var].lims

    def equals(self, other):
        self._values.equals(other._values)

    def _get_var_info(self):
        raise NotImplementedError
