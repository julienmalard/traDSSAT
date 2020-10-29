from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_SGCER = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar(
        'P1', 5, 1,
        info='Thermal time from seedling emergence to the end of the juvenile phase (expressed in degree days above '
             'TBASE during which the plant is not responsive to changes in photoperiod'
    ),
    FloatVar(
        'P2', 5, 1,
        info='Thermal time from the end of the juvenile stage to tassel initiation under short days (degree days above '
             'TBASE)'
    ),
    FloatVar(
        'P2O', 5, 2,
        info='Critical photoperiod or the longest day length (in hours) at which development occurs at a maximum rate.'
             ' At values higher than P2O, the rate of development is reduced'
    ),
    FloatVar(
        'P2R', 5, 1,
        info='Extent to which phasic development leading to panicle initiation (expressed in degree days) is delayed '
             'for each hour increase in photoperiod above P2O'
    ),
    FloatVar('PANTH', 5, 1,
             info='Thermal time from the end of tassel initiation to anthesis (degree days above TBASE)'),
    FloatVar('P3', 5, 1, info='Thermal time from to end of flag leaf expansion to anthesis (degree days above TBASE)'),
    FloatVar('P4', 5, 1, info='Thermal time from anthesis to beginning grain filling (degree days above TBASE)'),
    FloatVar('P5', 5, 1, info='Thermal time from beginning of grain filling to physiological maturity (degree days '
                              'above TBASE)'),
    FloatVar(
        'PHINT', 5, 2,
        info='Phylochron interval; the interval in thermal time between successive leaf tip appearances (degree days)'
    ),
    FloatVar('G1', 5, 1, info='Scaler for relative leaf size'),
    FloatVar('G2', 5, 1, info='Scaler for partitioning of assimilates to the panicle (head).'),
    FloatVar('PSAT', 5, 1, info='Critical photoperiod below which development is not delayed (optional)'),
    FloatVar('PBASE', 5, 1, info='Ceiling photoperiod above which development is delayed indefinitely (optional)')
}

eco_vars_SGCER = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('TBASE', 5, 1, info='Base temperature below which no development occurs (oC)'),
    FloatVar('TOPT', 5, 1, info='Temperature at which maximum development occurs for vegetative stages (oC)'),
    FloatVar('ROPT', 5, 1, info='Temperature at which maximum development occurs for reproductive stages (oC)'),
    FloatVar('GDDE', 5, 1, info='Growing degree days per cm seed depth required for emergence (degree days/cm)'),
    FloatVar('RUE', 5, 1, info='Radiation use efficiency (g plant dry matter/MJ PAR)'),
    FloatVar('KCAN', 5, 2, info='Canopy light extinction coefficient for daily PAR'),
    FloatVar('STPC', 5, 3, info='Partitioning to stem growth as a fraction of potential leaf growth'),
    FloatVar('RTPC', 5, 3, info='Partitioning to root growth as a fraction of available carbohydrates'),
    FloatVar('TILFC', 5, 1, info='Tillering factor (0.0 no tillering; 1.0 full tillering)')
}
