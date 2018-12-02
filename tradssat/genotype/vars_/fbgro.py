from tradssat.genotype.vars_._cropgro import cropgro_cul_vars, cropgro_eco_vars

cul_vars_FBGRO = cropgro_cul_vars()

eco_vars_FBGRO = cropgro_eco_vars(rename={'LNGSH': 'LNHSH'})
