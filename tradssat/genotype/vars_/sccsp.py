from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_SCCSP = {
    CharacterVar(
        'VAR#', 6, spc=0, info='Identification code or number for a specific cultivar used by  DSSAT program.'
    ),
    CharacterVar(
        'VAR-NAME', 16, header_fill='.', info='Name of cultivar as recognized commercially or within industry.'
    ),
    IntegerVar('EXPNO', 5, miss='.', info='Number of experiments used to estimate cultivar parameters.'),
    CharacterVar('ECO#', 6, info='Ecotype code of this cultivar in the ECO input file'),

    FloatVar(
        'LFMAX', 5, 3,
        info='Maximum leaf photosynthesis rate, 30 C, 350 ppm CO2 and high '
             'light (used in leaf-level ET routine - Not yet in CASUPRO). mg CO2/m2-s')

}

eco_vars_SCCSP = {

}
