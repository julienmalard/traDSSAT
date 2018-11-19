from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_GBGRO = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Name of cultivar.'),
    IntegerVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar(
        'ECO#', 6,
        info='Ecotype code or this cultivar, points to the Ecotype in the ECO file.'
    ),

    FloatVar(
        'P1', 5, 1,
        info='Thermal time from seedling emergence to the end of the juvenile '
             'phase (expressed in degree days above a base temperature of 8 deg.C) '
             'during which the plant is not responsive to changes in photoperiod.'
    ),

    FloatVar(
        'P2', 5, 3,
        info='Extent to which development (expressed as days) is delayed for '
             'each hour increase in photoperiod above the longest photoperiod '
             'at which development proceeds at a maximum rate (which is '
             'considered to be 12.5 hours).'
    ),
    FloatVar(
        'P5', 5, 1,
        info='Extent to which development (expressed as days) is delayed for '
             'each hour increase in photoperiod above the longest photoperiod.'
    ),

    FloatVar('G2', 5, 1, info='Maximum possible number of kernels per plant.'),
    FloatVar(
        'G3', 5, 2,
        info='Kernel filling rate during the linear grain filling stage and under optimum conditions (mg/day).'
    ),
    FloatVar(
        'PHINT', 5, 2,
        info='Phylochron interval; the interval in thermal time (degree days) between successive leaf tip appearances.'
    )
}

eco_vars_GBGRO = {

}
