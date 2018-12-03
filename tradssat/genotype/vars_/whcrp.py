from tradssat.genotype.vars_._cropsim import cropsim_cul_vars, cropsim_eco_vars

cul_vars_WHCRP = cropsim_cul_vars()

eco_vars_WHCRP = cropsim_eco_vars(exclude=['GWTAF', 'GWTAT', 'G#RF', 'RTNUP', 'NUPNF', 'NUPWF'])
