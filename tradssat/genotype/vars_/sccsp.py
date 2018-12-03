from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_SCCSP = {  # Todo: add info for all vars
    CharacterVar(
        'VAR#', 6, spc=0, info='Identification code or number for a specific cultivar used by  DSSAT program.'
    ),
    CharacterVar(
        'VAR-NAME', 16, header_fill='.', info='Name of cultivar as recognized commercially or within industry.'
    ),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used to estimate cultivar parameters.'),
    CharacterVar('ECO#', 6, info='Ecotype code of this cultivar in the ECO input file'),

    FloatVar(
        'LFMAX', 5, 3,
        info='Maximum leaf photosynthesis rate, 30 C, 350 ppm CO2 and high '
             'light (used in leaf-level ET routine - Not yet in CASUPRO). mg CO2/m2-s'),
    FloatVar(
        'PHTMX', 5, 1, info='Maximum amount of CH20 which can be produced if PAR is very high, g[CH2O]/m2-d'
    ),
    FloatVar('Stalk', 5, 3),
    FloatVar('Sucro', 5, 3),
    IntegerVar('Null1', 5),
    FloatVar('PLF1', 5, 3),
    FloatVar('PLF2', 5, 3),
    FloatVar('Gamma', 5, 3),
    FloatVar('StkB', 5, 3),
    FloatVar('StkM', 5, 3),
    IntegerVar('Null3', 5),
    FloatVar('SIZLF', 5, 2),
    FloatVar('PLF2', 5, 3),
    FloatVar('LIsun', 5, 3),
    FloatVar('LIshd', 5, 3),
    IntegerVar('Null4', 5),
    FloatVar('TB(1)', 5, 3),
    FloatVar('TO1(1)', 5, 2),
    FloatVar('TO2(1)', 5, 2),
    FloatVar('TM(1)', 5, 2),
    FloatVar('PI1', 5, 2),
    FloatVar('PI2', 5, 2),
    FloatVar('DTPI', 5, 1),
    FloatVar('LSFAC', 5, 3),
    IntegerVar('Null5', 5),
    FloatVar('LI1', 5, 3),
    FloatVar('TELOM', 5, 1),
    FloatVar('TB(2)', 5, 2),
    FloatVar('TO1(2)', 5, 2),
    FloatVar('TO2(2)', 5, 2),
    FloatVar('TM(2)', 5, 2),
    FloatVar('Ph1P', 5, 1),
    FloatVar('Ph1R', 5, 1),
    FloatVar('Ph2', 5, 3),
    FloatVar('Ph3', 5, 0),
    FloatVar('Ph4', 5, 0),
    FloatVar('StHrv', 5, 3),
    FloatVar('RTNFAC', 5, 3),
    FloatVar('MinGr', 5, 2),
    IntegerVar('Null7', 5),
    FloatVar('RES30C', 5, 3),
    FloatVar('RLF30C', 5, 3),
    FloatVar('R30C2', 5, 3),

}
