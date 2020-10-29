from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_CSCAS = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXP#', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Ecotype code for this cultivar,points to entry in the ECO file'),

    FloatVar('PPS1', 5, 0, info='Photoperiod sensitivity for phase n. (% drop for 10h pp.change)'),

    FloatVar('B01ND', 5, 2, info='Duration from branch 0 to branch 1 (ie.tier x,node number)'),
    FloatVar('B12ND', 5, 2, info='Duration from branch 1 to branch 2 (ie.tier x,node number)'),
    FloatVar('B23ND', 5, 2, info='Duration from branch 2 to branch 3 (ie.tier x,node number)'),
    FloatVar('B34ND', 5, 2, info='Duration from branch 3 to branch 4 (ie.tier x,node number)'),
    FloatVar('B45ND', 5, 2, info='Duration from branch 4 to branch 5 (ie.tier x,node number)'),
    FloatVar('B56ND', 5, 2, info='Duration from branch 5 to branch 6 (ie.tier x,node number)'),

    FloatVar('SR#WT', 5, 2, info='Storage root number per unit canopy weight at initiation (#/g)'),
    FloatVar('SRFR', 5, 2, info='Fr.of assimilate designated for tops sent to storage root (#)'),
    FloatVar('HMPC', 5, 0, info='Harvest product moisture content (%)'),
    FloatVar('PHINT', 5, 0, info='Interval between leaf tip appearances for first leaves (oC.d)'),
    FloatVar('LA1S', 5, 0, info='Area/leaf (cm2) of the first leaves when growing without stress.'),
    FloatVar('LAXS', 5, 0, info='Area/leaf at maximum area/leaf (cm2)'),
    IntegerVar('LAXND', 5, info='Node # at which maximum potential area/leaf reached (#)'),
    IntegerVar('LAXN2', 5, info='Node # at which potential area/leaf begins to decline (#)'),
    FloatVar('LAFS', 5, 0, info='End of cycle area/leaf (cm2)'),
    IntegerVar('LAFND', 5, info='Node # at which the end of cycle area/leaf reached (#)'),
    IntegerVar('SLAS', 5, info='Specific leaf lamina area when crop growing without stress (cm2/g)'),
    FloatVar('LLIFA', 5, 0, info='Leaf life,from full expansion to start senescence (Thermal units)'),
    FloatVar('LPEFR', 5, 2, info='Leaf petiole fraction (fr of lamina+petiole)'),
    FloatVar('STFR', 5, 2, info='Stem fraction of assimilate destined for canopy growth (fr)'),

}

eco_vars_CSCAS = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('BR1FX', 5, 0, info='Branch number per fork at fork 1, maximum (#)'),
    FloatVar('BR2FX', 5, 0, info='Branch number per fork at fork 2, maximum (#)'),
    FloatVar('BR3FX', 5, 0, info='Branch number per fork at fork 3, maximum (#)'),
    FloatVar('BR4FX', 5, 0, info='Branch number per fork at fork 4, maximum (#)'),
    FloatVar('BR5FX', 5, 0, info='Branch number per fork at fork 5, maximum (#)'),
    FloatVar('BR6FX', 5, 0, info='Branch number per fork at fork 6, maximum (#)'),
    FloatVar('PARUE', 5, 2, info='PAR conversion factor,standard (g dry matter/MJ)'),
    FloatVar('DUSRI', 5, 0, info='Degree days at which storage root number determined (oC.d)'),
    FloatVar('SRN%S', 5, 2, info='Storage root standard N concentration (% dm)'),
    FloatVar('HTSTD', 5, 0, info='Standard canopy height (cm)')
}
