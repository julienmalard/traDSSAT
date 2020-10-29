from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class SoilTempOut(OutFile):
    """
    Reader for DSSAT soil temperature (SOILTEMP.OUT) output files.
    """
    filename = 'SoilTemp.Out'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 3, info='Day after start'),
    FloatVar('TS0D', 4, 1, info='temperature at the surface, oC'),
    FloatVar('TS1D', 4, 1, info='Temperature at soil depth 0-5 cm, oC'),
    FloatVar('TS2D', 4, 1, info='Temperature at soil depth 5-15 cm, oC'),
    FloatVar('TS3D', 4, 1, info='Temperature at soil depth 15-30 cm, oC'),
    FloatVar('TS4D', 4, 1, info='Temperature at soil depth 30-45 cm, oC'),
    FloatVar('TS5D', 4, 1, info='Temperature at soil depth 45-60 cm, oC'),
    FloatVar('TS6D', 4, 1, info='Temperature at soil depth 60-90 cm, oC'),
    FloatVar('TS7D', 4, 1, info='Temperature at soil depth 90-110 cm, oC'),
}
