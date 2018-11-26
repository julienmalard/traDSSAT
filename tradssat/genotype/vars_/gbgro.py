from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_GBGRO = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Name of cultivar.'),
    IntegerVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar(
        'CSDL', 5, 2,
        info='Critical Short Day Length below which reproductive development progresses with no daylength effect '
             '(for shortday plants) (hour)'
    ),

    FloatVar(
        'PPSEN', 5, 3,
        info='Slope of the relative response of development to photoperiod with time '
             '(positive for shortday plants) (1/hour)'
    ),
    FloatVar('EM-FL', 5, 1, info='Time between plant emergence and flower appearance (R1) (photothermal days)'),
    FloatVar('FL-SH', 5, 1, info='Time between first flower and first pod (R3) (photothermal days)'),
    FloatVar('FL-SD', 5, 1, info='Time between first flower and first seed (R5) (photothermal days)'),
    FloatVar('SD-PM', 5, 2, info='Time between first seed (R5) and physiological maturity (R7) (photothermal days)'),
    FloatVar('FL-LF', 5, 2, info='Time between first flower (R1) and end of leaf expansion (photothermal days)'),
    FloatVar('LFMAX', 5, 2, info='Maximum leaf photosynthesis rate at 30 C, 350 vpm CO2, and high light (mg CO2/m2-s)'),
    FloatVar('SLAVR', 5, 0, info='Specific leaf area of cultivar under standard growth conditions (cm2/g)'),
    FloatVar('SIZLF', 5, 1, info='Maximum size of full leaf (three leaflets) (cm2)'),
    FloatVar('XFRT', 5, 2, info='Maximum fraction of daily growth that is partitioned to seed + shell'),
    FloatVar('WTPSD', 5, 3, info='Maximum weight per seed (g)'),
    FloatVar(
        'SFDUR', 5, 1, info='Seed filling duration for pod cohort at standard growth conditions (photothermal days)'
    ),
    FloatVar('SDPDV', 5, 2, info='Average seed per pod under standard growing conditions (#/pod)'),
    FloatVar(
        'PODUR', 5, 1,
        info='Time required for cultivar to reach final pod load under optimal conditions (photothermal days)'
    ),
    FloatVar(
        'THRSH', 5, 1,
        info='The maximum ratio of (seed/(seed+shell)) at maturity. '
             'Causes seed to stop growing as their dry weights '
             'increase until shells are filled in a cohort. '
             '(Threshing percentage).'
    ),
    FloatVar('SDPRO', 5, 3, info='Fraction protein in seeds (g(protein)/g(seed))'),
    FloatVar('SDLIP', 5, 3, info='Fraction oil in seeds (g(oil)/g(seed))')

}

eco_vars_GBGRO = {

}
