from tradssat.genotype.vars_._cropgro import cropgro_cul_vars, cropgro_eco_vars
from tradssat.tmpl.var import FloatVar

cul_vars_BMGRO = cropgro_cul_vars()

eco_vars_BMGRO = cropgro_eco_vars()
eco_vars_BMGRO.update({
    FloatVar('RDRMT', 5, dec=3,
             info='Relative dormancy sensitivity of this cultivar to daylength - partitioning (0-1)'),
    FloatVar('RDRMG', 5, dec=3,
             info='Relative dormancy sensitivity of this cultivar to daylength - photosynthesis (0-1)'),
    FloatVar('RDRMM', 5, dec=3,
             info='Relative dormancy sensitivity of this cultivar to daylength - mobilization (0-1)'),
    FloatVar('RCHDP', 5, dec=3, info='Relative cold hardening potential (0-1)')
})
