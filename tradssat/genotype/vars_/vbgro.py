from tradssat.genotype.vars_._cropgro import cropgro_cul_vars, cropgro_eco_vars

cul_vars_VBGRO = cropgro_cul_vars()

eco_vars_VBGRO = cropgro_eco_vars(rename={'LNGSH': 'LNHSH'})
