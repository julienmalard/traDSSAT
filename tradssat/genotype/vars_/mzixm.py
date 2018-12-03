from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_MZIXM = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar(
        'P1', 5, 1,
        info='Thermal time from seedling emergence to the end of the juvenile phase (expressed in degree days above a '
             'base temperature of 8 deg.C) during which the plant is not responsive to changes in photoperiod.'
    ),
    FloatVar(
        'P2', 5, 3,
        info='Extent to which development (expressed as days) is delayed for each hour increase in photoperiod above '
             'the longest photoperiod at which development proceeds at a maximum rate (which is considered to be 12.5 '
             'hours).'
    ),
    FloatVar(
        'P5', 5, 1,
        info='Thermal time from silking to physiological maturity (expressed in degree days above a base temperature '
             'of 8 deg.C).'
    ),
    FloatVar('G2', 5, 1, info='Maximum possible number of kernels on topmost ear.'),
    FloatVar(
        'G3', 5, 2,
        info='Kernel filling rate during the linear grain filling stage and under optimum conditions (mg/day).'
    ),
    FloatVar(
        'PHINT', 5, 2,
        info='Phylochron interval; the interval in thermal time (degree days) between successive leaf tip appearances.'
    ),
    FloatVar('AX', 5, 1, info='Leaf surface area (cm2/leaf) of largest leaf.'),
    FloatVar('ALL', 5, 1, info='Leaf longevity (degree days) of the most longevous leaf.')
}

eco_vars_MZIXM = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('TBASE', 5, 1, info='Base temperature below which no development occurs, C'),
    FloatVar('TOPT', 5, 1, info='Temperature at which maximum development rate occurs during vegetative stages, C'),
    FloatVar('ROPT', 5, 1, info='Temperature at which maximum development rate occurs for reproductive stages, C'),
    FloatVar('P20', 5, 1, info='Daylength below which daylength does not affect development rate, hours'),
    FloatVar(
        'DJTI', 5, 1, info='Minimum days from end of juvenile stage to tassel initiation if the cultivar is not '
                           'photoperiod sensitive, days'
    ),
    FloatVar('GDDE ', 5, 1, info='Growing degree days per cm seed depth required for emergence, GDD/cm'),
    FloatVar('DSGFT', 5, 0, info='GDD from silking to effective grain filling period, C'),
    FloatVar('RUE', 5, 1, info='Radiation use efficiency, g plant dry matter/MJ PAR'),
    FloatVar('KCAN', 5, 2, info='Canopy light extinction coefficient for daily PAR.'),
    FloatVar(
        'PSTM', 5, 2, info='Parameter controlling stem C partitioning during ISTAGES 3, 4 (0-1) Higher PSTM, more DM '
                           'into stem, less into leaves'
    ),
    FloatVar(
        'PEAR', 5, 2, info='Parameter controlling ear C partitioning during ear growth  (250 GDD before flowering-end'
                           ' ISTAGE 4)'
    ),
    FloatVar('TSEN', 5, 2, info='Critical temperature below which leaf damage occurs (default 6°C)'),
    FloatVar('CDAY', 5, 2, info='Number of cold days parameter (default 15.0 )')
}
