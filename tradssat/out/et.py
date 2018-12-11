from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class ETOut(OutFile):
    filename = 'ET.OUT'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 5, info='Day after start'),
    FloatVar('SRAA', 6, 2, info='Average solar radiation (MJ/(m2.day'),
    FloatVar('TMAXA', 6, 2, info='Average maximum air temperature (°C)'),
    FloatVar('TMINA', 6, 2, info='Average minimum air temperature (°C)'),
    FloatVar('EOAA', 6, 3, info='Average potential evapotranspiration (mm/d)'),
    FloatVar('EOPA', 6, 3, info=' Average potential transpiration (mm/d)'),
    FloatVar('EOSA', 6, 3, info='Average potential soil evaporation per day (mm/day)'),
    FloatVar('ETAA', 6, 3, info='Average evapotranspiration (mm/d)'),
    FloatVar('EPAA', 6, 0, info=' Average plant transpiration (mm/d)'),
    FloatVar('ESAA', 6, 3, info='Average soil evaporation (mm/d)'),
    FloatVar('EFAA', 6, 0, info='Average flood evaporation (mm/d)'),
    FloatVar('EMAA', 6, 3, info='Average mulch evaporation (mm/d)'),
    FloatVar('EOAC', 7, 2, info='Cumulative potential evapotranspiration (mm)'),
    FloatVar('ETAC', 7, 2, info='Cumulative evapotranspiration (mm)'),
    FloatVar('EPAC', 7, 0, info=' Cumulative transpiration (mm)'),
    FloatVar('ESAC', 7, 2, info='Cumulative soil evaporation (mm)'),
    FloatVar('EFAC', 7, 0, info='Cumulative floodwater evaporation (mm)'),
    FloatVar('EMAC', 7, 2, info='Cumulative mulch evaporation (mm)'),
}

