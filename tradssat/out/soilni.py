from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class SoilNitrogen (OutFile):
    filename = 'SoilNi.Out'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 5, info='Day after start' ),
    IntegerVar('NAPC', 5, info='Cumulative inorganic N applied, kg/ha'),
    IntegerVar('NI#M', 5, info='N application numbers'),
    FloatVar('NIAD', 7, 1, info='Inorganic N in soil, kg/ha'),
    FloatVar('NITD', 6, 1, info= 'Amount of total N, kg/ha' ),
}
