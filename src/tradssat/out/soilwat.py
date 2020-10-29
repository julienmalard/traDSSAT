from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class SoilWatOut(OutFile):
    filename = 'SoilWat.Out'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 3, info='Day after start'),
    IntegerVar('SWTD', 4, info='total soil water in profile, mm'),
    IntegerVar('SWXD', 4, info='potentially extractable water, cm'),
    IntegerVar('ROFC', 4, info='cumulative runoff'),
    IntegerVar('DRNC', 4, info='cumulative drainage'),
    IntegerVar('PREC', 4, info='cumulative precipitation'),
    IntegerVar('IR#C', 4, info='irrigation'),
    IntegerVar('IRRC', 4, info='cumulative irrigation'),
    IntegerVar('DTWT', 4, info='water table depth, cm'),
    FloatVar('MWTD', 4, 2, info='water stored in mulch layer, mm'),
    FloatVar('TDFD', 4, 0, info='water lost to tile drainage, mm/d'),
    FloatVar('TDFC', 4, 0, info='cumulative water lost to tile drainage, mm'),
    FloatVar('ROFD', 4, 0, info='total daily surface runoff, mm/d'),
    FloatVar('SW1D', 4, 3, info='soil water content at 0-5 cm depth, mm3/mm3'),
    FloatVar('SW2D', 4, 3, info='soil water content at 5-15 cm depth, mm3/mm3'),
    FloatVar('SW3D', 4, 3, info='soil water content at 15-30 cm depth, mm3/mm3'),
    FloatVar('SW4D', 4, 3, info='soil water content at 30-45 cm depth, mm3/mm3'),
    FloatVar('SW5D', 4, 3, info='soil water content at 45-60 cm depth, mm3/mm3'),
    FloatVar('SW6D', 4, 3, info='soil water content at 60-90 cm depth, mm3/mm3'),
    FloatVar('SW7D', 4, 3, info='soil water content at 90-110 cm depth, mm3/mm3'),

    # Recently added (#19)
    FloatVar('SW8D', 4, 3, info='soil water content at 120-150 cm depth, mm3/mm3'),

}
