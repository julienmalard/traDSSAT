from tradssat import SummaryOut, PlantGroOut, SoilWatOut, SoilNiOut, SoilTempOut


class DSSATResults(object):
    """
    Facilitates the reading of DSSAT results. Instead of having to read each output file individually, you can simply
    point this class to a DSSAT run output folder containing the output files and it will find the desired variables
    for you.
    """

    def __init__(self, folder):
        """
        Initialise with the base folder.

        Parameters
        ----------
        folder: str
            The DSSAT run output folder.
        """

        self.folder = folder

        self._outfiles_clases = {f.filename: f for f in [PlantGroOut, SoilWatOut, SoilNiOut, SoilTempOut]}
        self._outfiles = {f: None for f in self._outfiles_clases}

        self._sumoutclass = SummaryOut
        self._sumoutfile = None

    def reload(self):
        """
        Reload data (useful if a new DSSAT simulation has been run).
        """

        for out_class in self._outfiles:
            self._outfiles[out_class.filename] = None
        self._sumoutfile = None

    def get_value(self, var, trt, t=None, at='YEAR DOY', run=None):
        """
        Returns the value (point or time-series) of a variable from a DSSAT run.

        Parameters
        ----------
        var: str
            The variable name.
        trt: int
            The treatment number of interest.
        t: str | int
            The time at which one wants the results. If ``None``, results will be given for all time steps.
        at: str
            Must be one of ``DAS`` (days after start), ``DAP`` (days after planting), or ``YEAR DOY`` (year,
            day of year; default). Only used if ``t`` is not ``None``.
        Returns
        -------
        np.ndarray:
            The value of the variable.
        """
        if t is not None:
            if at in ['DAS', 'DAP']:
                cond = {at: int(t)}
            elif at in ['DOY', 'YEAR DOY']:
                year, doy = t.split()
                cond = {'YEAR': int(year), 'DOY': int(doy)}
            else:
                raise ValueError(at)
        else:
            cond = None

        if run is None:
            sect = {'TREATMENT': trt}
        else:
            sect = {'TREATMENT': trt, 'RUN': run}

        for c, f in self._outfiles.items():

            if f is None:
                try:
                    f = self._outfiles[c] = self._outfiles_clases[c](self.folder)
                except FileNotFoundError:
                    pass

            if var in f.variables():
                if t is None:
                    return f.get_value(var, sect=sect)
                return f.get_value(var, sect=sect, cond=cond)

        raise ValueError('Output variable "{}" could not be found in any output file.'.format(var))

    def get_final_value(self, var, trt):
        """
        Returns a variable's final value. Faster than :func:`get_value` if the variable is available
        in `Summary.OUT`.

        Parameters
        ----------
        var: str
            The variable name.
        trt: int
            The treatment number of interest.

        Returns
        -------
        str | float | int
            The variable's final value.
        """

        if self._sumoutfile is None:
            self._sumoutfile = self._sumoutclass(self.folder)
        if var in self._sumoutfile.variables():
            return self._sumoutfile.get_value(var, cond={'TRNO': trt})[0]
        vals = self.get_value(var=var, trt=trt)
        return vals[-1]
