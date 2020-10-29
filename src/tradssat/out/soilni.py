from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class SoilNiOut(OutFile):
    """
    Reader for DSSAT soil nitrogen (SOILNI.OUT) files.
    """
    filename = 'SoilNi.Out'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 3, info='Day after start'),
    IntegerVar('NAPC', 4, info='Cumulative inorganic N applied, kg/ha'),
    IntegerVar('NI#M', 4, info='N application numbers'),
    FloatVar('NIAD', 4, 1, info='Inorganic N in soil, kg/ha'),
    FloatVar('NITD', 4, 1, info='Amount of total NO3, kg/ha'),
    FloatVar('NHTD', 4, 1, info='Amount of total NH4, kg/ha'),
    FloatVar('NI1D', 4, 2, info='NO3 at 0-5 cm soil depth, ppm'),
    FloatVar('NI2D', 4, 2, info='NO3 at 5-15 cm soil depth, ppm'),
    FloatVar('NI3D', 4, 2, info='NO3 at 15-30 cm soil depth, ppm'),
    FloatVar('NI4D', 4, 2, info='NO3 at 30-45 cm soil depth, ppm'),
    FloatVar('NI5D', 4, 2, info='NO3 at 45-60 cm soil depth, ppm'),
    FloatVar('NI6D', 4, 2, info='NO3 at 60-90 cm soil depth, ppm'),
    FloatVar('NI7D', 4, 2, info='NO3 at 90-110 cm soil depth, ppm'),
    FloatVar('NH1D', 4, 2, info='NH4 at 0-5 cm soil depth, ppm'),
    FloatVar('NH2D', 4, 2, info='NH4 at 5-15 cm soil depth, ppm'),
    FloatVar('NH3D', 4, 2, info='NH4 at 15-30 cm soil depth, ppm'),
    FloatVar('NH4D', 4, 2, info='NH4 at 30-45 cm soil depth, ppm'),
    FloatVar('NH5D', 4, 2, info='NH4 at 45-60 cm soil depth, ppm'),
    FloatVar('NH6D', 4, 2, info='NH4 at 60-90 cm soil depth, ppm'),
    FloatVar('NH7D', 4, 2, info='NH4 at 90-110 cm soil depth, ppm'),
    FloatVar('NMNC', 4, 0, info=''),
    FloatVar('NITC', 4, 0, info=''),
    FloatVar('NDNC', 4, 0, info=''),
    FloatVar('NIMC', 4, 0, info=''),
    FloatVar('AMLC', 4, 0, info=''),
    FloatVar('NNMNC', 5, 0, info=''),
    FloatVar('NUCM', 4, 0, info='N uptake, kg/ha'),
    FloatVar('NLCC', 4, 0, info='Cumulative N leached, kg/ha'),
}
