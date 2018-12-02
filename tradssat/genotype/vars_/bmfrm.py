from tradssat.tmpl.var import FloatVar
from ._cropgro import cropgro_cul_vars, cropgro_eco_vars

cul_vars_BMFRM = cropgro_cul_vars()

eco_vars_BMFRM = cropgro_eco_vars()
eco_vars_BMFRM.update({
    FloatVar('RDRMT', 5, 3, info='Relative dormancy sensitivity of this cultivar to daylength - partitioning (0-1)'),
    FloatVar('RDRMG', 5, 3, info='Relative dormancy sensitivity of this cultivar to daylength - photosynthesis (0-1)'),
    FloatVar('RDRMM', 5, 3, info='Relative dormancy sensitivity of this cultivar to daylength - mobilization (0-1)'),
    FloatVar('RCHDP', 5, 3, info='Relative cold hardening potential (0-1)'),
})
