from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_CSYCA = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXP#', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar('PPS1', 5, 0, info='Photoperiod sensitivity for phase 1. (% drop for 10h pp.change)'),
    FloatVar('B01ND', 5, 0, info='Duration from branch 0 to branch 1 (ie.tier x,node number)'),
    FloatVar('B12ND', 5, 0, info='Duration from branch 1 to branch 2 (ie.tier x,node number)'),
    FloatVar(
        'HMPC', 5, 0,
        info='Harvest product moisture content (%) (currently this variable doesn\'t affect calibration)'
    ),
    FloatVar('LA1S', 5, 0, info='Area/leaf (cm2) of the first leaves when growing without stress.'),
    FloatVar('LAXS', 5, 0, info='Area/leaf at maximum area/leaf (cm2)'),
    FloatVar('SLAS', 5, 0, info='Specific leaf lamina area when crop growing without stress (cm2/g)'),
    FloatVar('LLIFA', 5, 0, info='Leaf life,from full expansion to start senescence (Thermal units)'),
    FloatVar('LPEFR', 5, 2, info='Leaf petiole fraction (fr of lamina+petiole)'),
    FloatVar('LNSLP', 5, 1, info='Slope for leaf production (0.8 low rate, 1.0 medium rate, 1.2 high rate)'),
    FloatVar('NODWT', 5, 1, info='Node weight for the first stem of the shoot before branching at 3400 ˚Cd'),
    FloatVar(
        'NODLT', 5, 0,
        info='Mean internode length (cm) for for the first stem of the shoot before branching when is lignified'
    )
}

eco_vars_CSYCA = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('PARUE', 5, 2, info='PAR conversion factor,standard (g dry matter/MJ)'),
    FloatVar('TBLSZ', 5, 1, info='Base temperature for leaf development (˚C)'),
    FloatVar('BR1FX', 5, 1, info='Branch number per fork at fork 1, maximum (#)'),
    FloatVar('BR2FX', 5, 1, info='Branch number per fork at fork 2, maximum (#)'),
    FloatVar('BR3FX', 5, 1, info='Branch number per fork at fork 3, maximum (#)'),
    FloatVar('BR4FX', 5, 1, info='Branch number per fork at fork 4, maximum (#)'),
    FloatVar('DUSRI', 5, 1, info='Degree days at which storage root number determined (oC.d)'),
    FloatVar('SRN%S', 5, 2, info='Storage root standard N concentration (% dm)'),
    FloatVar('KCAN', 5, 2, info='PAR extinction coefficient (#)')
}
