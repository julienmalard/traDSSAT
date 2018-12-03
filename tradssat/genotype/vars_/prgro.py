from tradssat.genotype.vars_._cropgro import cropgro_cul_vars, cropgro_eco_vars

cul_vars_PRGRO = cropgro_cul_vars()

eco_vars_PRGRO = cropgro_eco_vars(rename={'LNGSH': 'LNHSH'})
