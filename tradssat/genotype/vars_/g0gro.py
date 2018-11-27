from tradssat.genotype.vars_.cropgro import cropgro_cul_vars, cropgro_eco_vars

cul_vars_G0GRO = cropgro_cul_vars(exclude=['EXPNO', 'THRESH', 'SDPRO', 'SDLIP'])

eco_vars_G0GRO = cropgro_eco_vars()
