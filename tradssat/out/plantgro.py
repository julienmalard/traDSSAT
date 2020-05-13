from tradssat.tmpl.output import OutFile
from tradssat.tmpl.var import FloatVar, IntegerVar


class PlantGroOut(OutFile):
    """
    File reader for DSSAT plant growth (PLANTGRO.OUT) output files.
    """
    filename = 'PlantGro.OUT'

    def _get_var_info(self):
        return vars_

vars_ = {
    IntegerVar('TREATMENT', 2, info='Treatment number'),

    IntegerVar('YEAR', 4, info='Year'),
    IntegerVar('DOY', 3, info='Day of year starting on Jan 1.'),
    IntegerVar('DAS', 3, info='Day after start'),
    IntegerVar('DAP', 3, info='Days after planting'),
    FloatVar('L#SD', 4, 0, info='Leaf number'),
    FloatVar('GSTD', 4, 4, info='Growth stage'),
    FloatVar('LAID', 4, 2, info='Leaf Area Index'),
    IntegerVar('CWAD', 4, info='Tops dry weight, kg/Ha'),
    IntegerVar('VWAD', 4, info='Veg dry weight, kg/Ha'),
    IntegerVar('LWAD', 4, info='Leaf dry weight, kg/Ha'),
    IntegerVar('SWAD', 4, info='Stem dry weight, kg/Ha'),
    IntegerVar('FLWAD', 5, info='Flower dry weight, kg/Ha'),
    IntegerVar('FWAD', 4, info='Fruit dry weight, kg/Ha'),
    IntegerVar('CRAD', 4, info='Crown dry weight, kg/Ha'),
    IntegerVar('BWAD', 4, info='Basal dry weight, kg/Ha'),
    IntegerVar('SUGD', 4, info='Suck dry weight, kg/Ha'),
    IntegerVar('RWAD', 4, info='Root dry weight, kg/Ha'),
    FloatVar('HIAD', 4, 3, info='Harvest index'),
    IntegerVar('EYWAD', 5, info='Eye Weight, kg/Ha'),
    IntegerVar('EY#AD', 5, info='Eye number'),
    FloatVar('WSPD', 4, 3, info='Water stress in photosynthesis'),
    FloatVar('WSGD', 4, 3, info='Water stress in growth'),
    FloatVar('NSTD', 4, 3, info='Nitrogen stress'),
    FloatVar('LN%D', 4, 2, info='Leaf Nitrogen percentage'),
    FloatVar('SLAD', 4, 1, info='Specific Leaf area'),
    FloatVar('RDPD', 4, 1, info='Root depth, m'),
    FloatVar('RL1D', 4, 2, info='Level 1 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL2D', 4, 2, info='Level 2 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL3D', 4, 2, info='Level 3 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL4D', 4, 2, info='Level 4 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL5D', 4, 2, info='Level 5 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL6D', 4, 2, info='Level 6 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL7D', 4, 2, info='Level 7 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL8D', 4, 2, info='Level 8 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL9D', 4, 2, info='Level 9 Root Length density, cm3/cm3 of soil'),
    FloatVar('RL10', 4, 2, info='Level 10 Root Length density, cm3/cm3 of soil'),

    # Recently added (#19)
    FloatVar('TMEAN', 5, 1, info='Mean Temperature (TMAX + TMIN/2, ºC'),
    FloatVar('PARID', 5, 3, info='PAR interception (%)'),
    FloatVar('PARUD', 5, 2, info='PAR utilization efficiency (g/MJ)'),
    FloatVar('AWAD', 4, 1, info='Assimilate Production (kg/(ha.d))'),
    FloatVar('SAID', 4, 3, info='Stem Area Index (m2/m2)'),
    FloatVar('CAID', 4, 4, info='Canopy Area Index'),
    IntegerVar('TWAD', 4, info='Tops + Roots + storage wt (kg[dm]/ha)'),
    IntegerVar('SDWAD', 5, info='Seed weight (kg/ha)'),
    IntegerVar('HWAD', 4, info='Harvest Product wt (kg [dm]/ha)'),
    IntegerVar('RSWAD', 5, info='Reserves weight (kg/ha)'),
    FloatVar('SNWLD', 5, 3, info='Senesced OM added to surface (kg/ha)'),
    FloatVar('SNWSD', 5, 4, info='Senesced OM added to soil (kg/ha)'),
    FloatVar('RS%D', 4, 2, info='Reserves Concentration (%)'),
    IntegerVar('S#AD', 4, info='Shoot (apex) Number (no/m2)'),
    FloatVar('SWXD', 4, 1, info='Extractable water (mm)'),
    FloatVar('WAVRD', 5, 1, info='Water available to demand ratio (#)'),
    FloatVar('WUPRD', 5, 2, info='Water uptake to demand ratio (#)'),
    FloatVar('WFPD', 4, 2, info='Water factor for photosynthesis (0-1)'),
    FloatVar('WFGD', 4, 2, info='Water factor for growth (0-1)'),
    FloatVar('NFPD', 4, 2, info='N factor for photosynthesis (0-1)'),
    FloatVar('NFGD', 4, 2, info='N factor for leaf growth (0-1)'),
    FloatVar('NUPRD', 5, 1, info='N uptake to demand ratio (#)'),
    FloatVar('TFPD', 4, 2, info='Temperature factor for photosyntesis (0-1)'),
    FloatVar('TFGD', 4, 2, info='Temperature factor for leaf growth (0-1)'),
    FloatVar('DYLFD', 5, 2, info='Daylength factor for development (0-1)')

}

