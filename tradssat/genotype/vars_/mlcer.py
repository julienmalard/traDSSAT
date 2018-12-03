from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_MLCER = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar(
        'P1', 5, 1,
        info='Thermal time from seedling emergence to the end of the juvenile phase (expressed in degree days above a'
             ' base temperature of 10øC) during which the plant is not responsive to changes in photoperiod.'
    ),
    FloatVar(
        'P20', 5, 2,
        info='Critical photoperiod or the longest day length (in hours) at which development occurs at a maximum rate. '
             'At values greater than P2O, the rate of development is reduced.'
    ),
    FloatVar(
        'P2R', 5, 1,
        info='Extent to which phasic development leading to panicle initiation (expressed in degree days) is delayed '
             'for each hour increase in photoperiod above P2O.'
    ),
    FloatVar(
        'P5', 5, 1,
        info='Thermal time (degree days above a base temperature of 10øC) from beginning of grain filling (3-4 days '
             'after flowering) to physiological maturity.'
    ),
    FloatVar('G1', 5, 2, info='Scaler for relative leaf size.'),
    FloatVar('G4', 5, 2, info='Scaler for partitioning of assimilates to the panicle (head).'),
    FloatVar(
        'PHINT', 5, 2,
        info='Phylochron interval; the interval in thermal time (degree days) between successive leaf tip appearances.'
             ''),
    FloatVar('GT', 5, 2, info='Tillering coefficient, equivalent to G1, but on tillers'),
    FloatVar('G5', 5, 1, info='Potential grain size, mg')

}

eco_vars_MLCER = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('TBASE', 5, 1, info='base temperature below which no development occurs, C'),
    FloatVar('TOPT', 5, 1, info='temperature at which maximum development rate occurs during vegetative stages, C'),
    FloatVar('ROPT', 5, 1, info='temperature at which maximum development rate occurs for reproductive stages, C'),
    FloatVar(
        'DJTI', 5, 1,
        info='Minimum days from end of juvenile stage to tassel initiation if the cultivar is not photoperiod '
             'sensitive, days'
    ),
    FloatVar('GDDE', 5, 1, info='Growing degree days per cm seed depth required for emergence, GDD/cm'),
    FloatVar('RUE', 5, 1, info='Radiation use efficiency, g plant dry matter/MJ PAR'),
    FloatVar('KCAN', 5, 2, info='Canopy light extinction coefficient for daily PAR.')
}
