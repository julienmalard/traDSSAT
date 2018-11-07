from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class PlantGrowOut(OutFile):
    filename = 'PlantGro.OUT'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('TREATMENT', 2, info='Treatment number'),

    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 5, info='Day after start'),
    IntegerVar('DAP', 5, info='Days after planting'),
    FloatVar('L#SD', 6, 0, info='Leaf number'),
    IntegerVar('GSTD', 6, info='Growth stage'),
    FloatVar('LAID', 6, 2, info='Leaf Area Index'),
    IntegerVar('CWAD', 6, info='Tops dry weight, kg/Ha'),
    IntegerVar('VWAD', 6, info='Veg dry weight, kg/Ha'),
    IntegerVar('LWAD', 6, info='Leaf dry weight, kg/Ha'),
    IntegerVar('SWAD', 6, info='Stem dry weight, kg/Ha'),
    IntegerVar('FLWAD', 6, info='Flower dry weight, kg/Ha'),
    IntegerVar('FWAD', 6, info='Fruit dry weight, kg/Ha'),
    IntegerVar('CRAD', 6, info='Crown dry weight, kg/Ha'),
    IntegerVar('BWAD', 6, info='Basal dry weight, kg/Ha'),
    IntegerVar('SUGD', 6, info='Suck dry weight, kg/Ha'),
    IntegerVar('RWAD', 6, info='Root dry weight, kg/Ha'),
    FloatVar('HIAD', 6, 3, info='Harvest index'),





}
