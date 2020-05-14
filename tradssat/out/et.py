from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class ETOut(OutFile):
    filename = 'ET.OUT'

    def _get_var_info(self):
        return vars_


vars_ = {
    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 3, info='Day after start'),
    FloatVar('SRAA', 4, 2, info='Average solar radiation (MJ/(m2.day'),
    FloatVar('TMAXA', 5, 2, info='Average maximum air temperature (°C)'),
    FloatVar('TMINA', 5, 2, info='Average minimum air temperature (°C)'),
    FloatVar('EOAA', 4, 3, info='Average potential evapotranspiration (mm/d)'),
    FloatVar('EOPA', 4, 3, info=' Average potential transpiration (mm/d)'),
    FloatVar('EOSA', 4, 3, info='Average potential soil evaporation per day (mm/day)'),
    FloatVar('ETAA', 4, 3, info='Average evapotranspiration (mm/d)'),
    FloatVar('EPAA', 4, 0, info=' Average plant transpiration (mm/d)'),
    FloatVar('ESAA', 4, 3, info='Average soil evaporation (mm/d)'),
    FloatVar('EFAA', 4, 0, info='Average flood evaporation (mm/d)'),
    FloatVar('EMAA', 4, 3, info='Average mulch evaporation (mm/d)'),
    FloatVar('EOAC', 4, 2, info='Cumulative potential evapotranspiration (mm)'),
    FloatVar('ETAC', 4, 2, info='Cumulative evapotranspiration (mm)'),
    FloatVar('EPAC', 4, 0, info=' Cumulative transpiration (mm)'),
    FloatVar('ESAC', 4, 2, info='Cumulative soil evaporation (mm)'),
    FloatVar('EFAC', 4, 0, info='Cumulative floodwater evaporation (mm)'),
    FloatVar('EMAC', 4, 2, info='Cumulative mulch evaporation (mm)'),

    # Recently added (#19)
    FloatVar('REFA', 4, 3, info='ASCE standardized reference ET'),
    FloatVar('KCAA', 4, 3, info='FAO-56 single crop coefficient'),
    FloatVar('KCBA', 4, 3, info='FAO-56 basal crop coefficient'),
    FloatVar('KEAA', 4, 3, info='FAO-56 evaporation coefficient'),
    FloatVar('ES1D', 4, 3, info='Soil evaporation Layer 1 (mm/d)'),
    FloatVar('ES2D', 4, 3, info='Soil evaporation Layer 2 (mm/d)'),
    FloatVar('ES3D', 4, 3, info='Soil evaporation Layer 3 (mm/d)'),
    FloatVar('ES4D', 4, 3, info='Soil evaporation Layer 4 (mm/d)'),
    FloatVar('ES5D', 4, 3, info='Soil evaporation Layer 5 (mm/d)'),
    FloatVar('ES6D', 4, 3, info='Soil evaporation Layer 6 (mm/d)'),
    FloatVar('ES7D', 4, 3, info='Soil evaporation Layer 7 (mm/d)'),
    FloatVar('ES8D', 4, 3, info='Soil evaporation Layer 8 (mm/d)'),
    FloatVar('TRWUD', 5, 3, info='Root water uptake (cm/d)'),
}
