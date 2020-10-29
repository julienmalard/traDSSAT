from tradssat.genotype.vars_._cropsim import cropsim_cul_vars, cropsim_eco_vars

cul_vars_BACRP = cropsim_cul_vars()

eco_vars_BACRP = cropsim_eco_vars(rename={'TILPE': 'TIPHE'})
