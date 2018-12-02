from tradssat.genotype.vars_._cropgro import cropgro_cul_vars, cropgro_eco_vars
from tradssat.tmpl.var import CharacterVar

cul_vars_COGRO = cropgro_cul_vars()

eco_vars_COGRO = cropgro_eco_vars()
eco_vars_COGRO.add(CharacterVar('KCAN', 5, info='Who knows'))
