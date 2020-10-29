from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class MulchOut(OutFile):
    filename = 'Mulch.Out'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 5, info='Day after start'),
    FloatVar('MCFD', 4, 3, info='fraction of soil covered by mulch'),
    FloatVar('MDEPD', 5, 2, info='thickness of mulch layer, cm'),
    IntegerVar('MWAD', 4, info='mass of mulch layer, kg/ha'),
    FloatVar('MWTD', 4, 2, info='water stored in mulch layer, mm'),
}
