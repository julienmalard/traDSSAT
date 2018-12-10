import numpy as np

from tradssat.exper.exper_vars import TRT_HEAD, GENERAL
from tradssat.mgrs.exp_mgr import _level_codes, _factor_codes, _factor_to_code
from .exp_mgr import ExpFileMgr
from .gen_mgr import PeriphGenMgr
from .soil_mgr import PeriphSoilMgr
from .wth_mgr import PeriphWeatherMgr


def _valid_factor(factor):
    if factor in _factor_codes:
        return factor
    else:
        try:
            return _factor_to_code[factor]
        except KeyError:
            raise ValueError('Factor "{}" not recognised.'.format(factor))


class DSSATRun(object):
    """
    General manager for DSSAT run input files.
    """

    def __init__(self, file, model=None):
        """
        
        Parameters
        ----------
        file: str
            Input experiment file (.ccX).
        model: str
            Crop model code (optional). Useful when a crop can be simulated by more than one DSSAT crop model.
        """
        self.file = file
        self.exp = ExpFileMgr(file)

        field_levels = self.exp.get_file_val('L', sect='FIELDS')
        self.soil = PeriphSoilMgr(self.exp.get_file_val('ID_SOIL'), field_levels)
        self.weather = PeriphWeatherMgr(self.exp.get_file_val('WSTA'), levels=field_levels)

        cult_levels = self.exp.get_file_val('C', sect='CULTIVARS')
        crops = self.exp.get_file_val('CR')
        cults = self.exp.get_file_val('INGENO')
        self.genetics = PeriphGenMgr(crops, cults, cult_levels, model)

        self.peripherals = [self.soil, self.weather, self.genetics]

        self.check()

    def get_general_val(self, var):
        """
        Obtain a variable value from the `GENERAL` section of the EXP file.
        
        Parameters
        ----------
        var: str
            Variable name

        Returns
        -------
        np.ndarray
            Variable value.
        """
        return self.exp.get_file_val(var, sect=GENERAL)

    def set_general_val(self, var, val):
        """
        Sets a variable value in the `GENERAL` section of the EXP file.

        Parameters
        ----------
        var: str
            Variable name.
        val: str | float | int | np.ndarray
            New value for the variable.
        """
        self.exp.set_file_val(var, val, sect=GENERAL)

    def add_treatment(self, name, ops=None, factors=None):
        """
        Adds a treatment level to the experiment.
        
        Parameters
        ----------
        name: str
            Name of the new treatment.
        ops: dict
            Dictionnary of values for the `R`, `O`, and `C` treatment level options (optional).
        factors: dict
            Dictionnary of values for the treatment's factor levels (optional). Missing factors will be assigned 
            level 0.
        """
        if factors is None:
            factors = {}
        if ops is None:
            ops = {}

        default_ops = {'R': 1, 'O': 0, 'C': 0}
        default_ops.update(ops)

        factors = {_valid_factor(cd): vl for cd, vl in factors.items()}

        n = self.treatments().size + 1
        d_vals = {
            'N': n,
            'TNAME': name,
            **default_ops,
            **{cd: 0 for cd in _factor_codes}
        }
        d_vals.update(factors)

        self.exp.add_row(sect=TRT_HEAD, subsect=0, vals=d_vals)

    def remove_treatment(self, trt):
        """
        Removes a treatment from the experiment.
        
        Parameters
        ----------
        trt: str | int
            Treatment name or number.
        """
        if isinstance(trt, str):
            trt = self.get_trt_num(trt)
        self.exp.remove_row(sect=TRT_HEAD, subsect=0, cond={'N': trt})

    def add_factor_level(self, factor, vals):
        """
        Adds a factor level to the experiment.
        
        Parameters
        ----------
        factor: str
            Factor code or name.
        vals: dict
            Dictionnary of variable values for that factor level's variables. Missing variables will be assigned
            the corresponding missing code (usually -99).

        """
        factor = _valid_factor(factor)
        factor_name = _factor_codes[factor]
        level = self.n_factor_levels(factor) + 1
        lv_code = _level_codes[factor]
        level_vals = {
            lv_code: level,
            **vals
        }
        self.exp.add_row(sect=factor_name, vals=level_vals)

    def get_trt_factor_level(self, trt, factor):
        """
        Obtain the factor level for a specific treatment.

        Parameters
        ----------
        trt: str | int
            Treatment name or number.
        factor: str
            Factor name or code.

        Returns
        -------
        int
            The factor level corresponding to the given treatment.
        """
        factor = _valid_factor(factor)
        trt = self._valid_trt(trt)

        trt_nums = self.treatments()
        levels = self.exp.get_file_val(factor, sect=TRT_HEAD)

        return levels[trt_nums == trt][0]

    def set_trt_factor_level(self, trt, factor, level):
        """
        Sets the factor level for a treatment.
        
        Parameters
        ----------
        trt: str | int
            The treatment name or number.
        factor: str
            The factor name or code.
        level: int
            The new factor level.
        """
        factor = _valid_factor(factor)
        trt = self._valid_trt(trt)

        self.exp.set_file_val(factor, level, sect=TRT_HEAD, subsect=0, cond={'N': trt})

    def get_factor_level_val(self, var, level):
        """
        Obtain the variable value for a specific factor level.
        
        Parameters
        ----------
        var: str
            The variable of interest.
        level: int
            The factor level corresponding to the specified variable.

        Returns
        -------
        np.ndarray
            The variable value at the factor level.
        """
        file = self._locate_var(var)
        return file.get_value(var, level=level)

    def set_factor_level_val(self, var, val, level):
        file = self._locate_var(var)
        file.set_value(var, val, level=level)

    def get_trt_val(self, var, trt):
        """
        Returns the value of a treatment's variable.
        
        Parameters
        ----------
        var: str
            The variable of interest.
        trt: int | str
            The treatment name or number.

        Returns
        -------
        np.ndarray
            The variable value for the treatment.
        """
        var_loc = self._locate_var(var)
        factor = self._get_var_factor(var, var_loc)
        level = self.get_trt_factor_level(trt, factor)

        return var_loc.get_value(var, level)

    def set_trt_val(self, var, val, trt):

        var_loc = self._locate_var(var)
        factor = self._get_var_factor(var, var_loc)
        level = self.get_trt_factor_level(trt, factor)

        var_loc.set_value(var, val, level)

    def treatments(self, name=False):
        """
        Returns the treatments in the run.
        
        Parameters
        ----------
        name: bool
            Whether to return treatment names or numbers.

        Returns
        -------
        np.ndarray
            The list of treatments.
        """
        
        if name:
            return self.exp.get_trt_names()
        else:
            return self.exp.get_trt_nums()

    def n_factor_levels(self, factor):
        factor = _valid_factor(factor)
        factor_name = _factor_codes[factor]
        lv_var = _level_codes[factor]

        levels = self.exp.get_file_val(lv_var, sect=factor_name)

        return np.unique(levels).size

    def get_trt_name(self, n):
        """
        Returns the treatment name corresponding to a treatment number.
        
        Parameters
        ----------
        n: int
            The treatment number.

        Returns
        -------
        str
            The treatment name.
        """
        nums = self.treatments()
        names = self.treatments(name=True)

        return names[np.where(nums == n)][0]

    def get_trt_num(self, trt):
        """
        Returns the treatment number corresponding to a specified treatment name.
        
        Parameters
        ----------
        trt: str
            The treatment name.

        Returns
        -------
        int
            The corresponding treatment number.
        """
        nums = self.treatments()
        names = self.treatments(name=True)

        return nums[np.where(names == trt)]

    def check(self):
        # check consistent treatment numbering (numeric order)
        # Check all treatments exist
        # check no ununsed treatments (warn)
        # check all external soil, weather, genetic files exist
        # Check all treatment factor levels exist in sections
        pass

    def clean(self):
        # remove factor levels not used in any treatment

        # renumber treatments
        trts = np.arange(self.treatments().size)
        self.exp.set_file_val('N', trts, sect=TRT_HEAD)

        # renumber factor levels, and reorder them in subsections
        pass

    def write(self, file=None, force=False, clean=True, override=False):
        if clean:
            self.clean()

        for prph in self.peripherals:
            prph.write(force=force)

        self.exp.file.write(file=file, force=force)

    def _valid_trt(self, trt):

        if trt is None:
            return self.treatments()

        elif isinstance(trt, int):
            trt = [self.get_trt_name(trt)]
        elif isinstance(trt, str):
            trt = [trt]

        for i, t in enumerate(trt):
            if isinstance(t, str):
                trt[i] = self.get_trt_num(t)[0]

            elif t not in self.treatments():
                raise ValueError('Treatment "{t}" not found.'.format(t=t))

        return trt

    def _locate_var(self, var):

        for f in [self.exp, self.soil, self.genetics, self.weather]:
            if var in f.variables():
                return f

        raise ValueError('Could not find variable "{}".'.format(var))

    def _get_var_factor(self, var, var_loc):
        if isinstance(var_loc, (PeriphSoilMgr, PeriphWeatherMgr)):
            sect = 'FIELDS'
        elif isinstance(var_loc, PeriphGenMgr):
            sect = 'CULTIVARS'
        else:
            sect = self.exp.find_var_sect(var)

        return _factor_to_code[sect]
