from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar


class EvalOut(OutFile):
    def _get_var_info(self):
        return vars_


vars_ = {

    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 5, info='Day of simulation'),
    IntegerVar('DAP', 5, info='Days after planting'),

    FloatVar('L#SD', 6, 0, info='Leaf number'),

    IntegerVar('GSTD', 6, info='Growth stage'),
    FloatVar('LAID', 6, 2, info='Leaf Area Index'),
    IntegerVar('CWAD', 6, info='Tops dry weight, kg/Ha'),


}
