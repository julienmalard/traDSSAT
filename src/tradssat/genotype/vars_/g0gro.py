from tradssat.genotype.vars_._cropgro import cropgro_cul_vars, cropgro_eco_vars
from tradssat.tmpl.var import FloatVar

cul_vars_G0GRO = cropgro_cul_vars(exclude=['EXPNO', 'THRESH', 'SDPRO', 'SDLIP'])

eco_vars_G0GRO = cropgro_eco_vars()
eco_vars_G0GRO.update({
    FloatVar(
        'THRSH', 5, 1,
        info='The maximum ratio of (seed/(seed+shell)) at maturity. '
             'Causes seed to stop growing as their dry weights '
             'increase until shells are filled in a cohort. '
             '(Threshing percentage).'
    ),
    FloatVar('SDPRO', 5, 3, info='Fraction protein in seeds (g(protein)/g(seed))'),
    FloatVar('SDLIP', 5, 3, info='Fraction oil in seeds (g(oil)/g(seed))'),
})
