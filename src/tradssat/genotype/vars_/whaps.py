from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_WHAPS = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar('VSEN', 5, 2, info='sensitivity to vernalisation'),
    FloatVar('PPSEN', 5, 2, info='sensitivity to photoperiod'),
    FloatVar('P1', 5, 1, info='Thermal time from seedling emergence to the end of the juvenile phase'),
    FloatVar('P5', 5, 1, info='Thermal time (base 0oC) from beginning of grainfill to maturity: range 500 to 700'),
    FloatVar('PHINT', 5, 1, info='Phyllochron interval'),
    FloatVar(
        'GRNO ', 5, 2,
        info='Coefficient of kernel number per stem weight at the beginning of grain filling [kernels (g stem)-1]'
    ),
    FloatVar('MXFIL', 5, 2, info='Potential kernel growth rate [mg kernel-1 day-1]:  Values between 1.0 and 3.0'),
    FloatVar(
        'STMMX', 5, 2,
        info='Potential final dry weight of a single tiller (excluding grain) (g stem-1) values 1.0 - 3.0'
    ),
    FloatVar('SLAP1', 5, 1, info='ratio of leaf area to mass at emergence (cm2/g)'),
    FloatVar('SLAP2', 5, 1, info='ratio of leaf area to mass at end of leaf growth (cm2/g)'),
    FloatVar('TC1P1', 5, 2, info='for calculating tc1: tiller number from emerg. to term. spik.(=stem elongation)'),
    FloatVar('TC1P2', 5, 2, info='tc1 = tc1_p1 + tc1_p2 *cumph_nw(istage)'),
    FloatVar('DTNP1', 5, 3, info='for calculating dtiln: tiller number after term. spik.(=stem elongation)'),
    FloatVar('PLGP1', 5, 0, info='for calculating plag: potential leaf growth.  plag= plag_p1*cumph(istage)**plag_p2'),
    FloatVar('PLGP2', 5, 2, info='for calculating plag: potential leaf growth.  plag= plag_p1*cumph(istage)**plag_p2'),
    FloatVar('P2AF', 5, 2, info='threshold AD in a layer becoming effective on root growth'),
    FloatVar('P3AF', 5, 1, info='length of downwards root not effected under aeration deficit'),
    FloatVar('P4AF', 5, 2, info='days to be accumulated before aeration deficit effects root growth'),
    FloatVar('P5AF', 5, 2, info='power term at af1'),
    FloatVar('P6AF', 5, 2, info='days to be accumulated before aeration deficit effects crop growth'),
    FloatVar('ADLAI', 5, 2,
             info='threshold aeration deficit (AF2) affecting LAI        (set to 1.0 for no stress run)'),
    FloatVar('ADTIL', 5, 2,
             info='threshold aeration deficit (AF2) effecting tillering  (set to 1.0 for no stress run)'),
    FloatVar('ADPHO', 5, 2,
             info='threshold aeration deficit (AF2) effecting photosyn.  (set to 1.0 for no stress run)'),
    FloatVar(
        'STEMN', 5, 2,
        info='0=original C to grain translocation, >0 to 1.0 sets % of C of stem to be transloc. to grain'
    ),
    FloatVar('MXNUP', 5, 2, info='max N uptake per day'),
    FloatVar('MXNCR', 5, 3, info='0.035=20%, .04=23% protein, max n:c ratio of grain growth'),
    FloatVar('WFNU', 5, 2, info='power term for water effect on N supply'),
    FloatVar('PNUPR', 5, 3, info='potential uptake rate (mg/meter/day)'),
    FloatVar('EXNO3', 5, 2, info='exponent for NO3 supply factor'),
    FloatVar('MNNO3', 5, 2, info='minimum for NO3 supply factor'),
    FloatVar('EXNH4', 5, 2, info='exponent for NH4 supply factor'),
    FloatVar('MNNH4', 5, 2, info='minimum for NH4 supply factor'),
    FloatVar('INGWT', 5, 2, info='initial grain weight  (mg/grain?)'),
    FloatVar(
        'INGNC', 5, 3,
        info='% protein, initial grain N conc   (init_grain_nconc or p_init_grain_nconc from APSIM Nwheat)'
    ),
    FloatVar(
        'FREAR', 5, 3,
        info='fraction between end ear and begin grainfilling, setting min stem weight for remobilisation'
    ),
    FloatVar('MNNCR', 5, 3, info='% protein, min n:c ratio of grain growth'),
    FloatVar(
        'GPPSS', 5, 2,
        info='gpp_start_stage - Grain per plant: 2=stem elong., 3=end leaf stage at which to start accumo. stem for '
             'gpp calc.'
    ),
    FloatVar(
        'GPPES', 5, 2,
        info='gpp_end_stage - Start grainfilling stage at which to end accumulation stem for Grain per plant calc'
    ),
    FloatVar('MXGWT', 5, 2, info='maximum kernal weight  [100 = no effect]'),
    FloatVar(
        'MNRTN', 5, 2,
        info='min root n due to grain n initialisation [0 = off] (root_n_min or p_root_n_min from APSIM Nwheat)'
    ),
    FloatVar('NOMOB', 5, 3, info='fraction of accum stem weight that is not mobile [0 = original]'),
    FloatVar('RTDP1', 5, 2, info='sw effect, 0 = old version'),
    FloatVar('RTDP2', 5, 2, info='crop stress effect, 0 = old version')
}

eco_vars_WHAPS = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('TBASE', 5, 1, info='base temperature below which no development occurs, C'),
    FloatVar('TOPT', 5, 1, info='temperature at which maximum development rate occurs during vegetative stages, C'),
    FloatVar(
        'ROPT ', 5, 1, info='temperature at which maximum development rate occurs for reproductive stages, C (no '
                            'effect, WHAPS)'
    ),
    FloatVar('TTOP', 5, 1, info='temperature above which no development occurs, C'),
    FloatVar(
        'P20', 5, 1, info='Daylength below which daylength does not affect development rate, hours (no effect, WHAPS)'
    ),
    FloatVar('VREQ', 5, 0, info='Vernalization required for max.development rate (VDays)'),
    FloatVar('GDDE', 5, 1, info='Growing degree days per cm seed depth required for emergence, GDD/cm'),
    FloatVar('DSGFT', 5, 0, info='GDD from End Ear Growth to Start Grain Filling period, C'),
    FloatVar('RUE', 5, 1, info='Radiation use efficiency, g plant dry matter/MJ PAR (no effect, WHAPS)'),
    FloatVar('KCAN', 5, 2, info='Canopy light extinction coefficient for daily PAR. (no effect, WHAPS)'),
    FloatVar('TSEN', 5, 1, info='Critical temperature below which leaf damage occurs (default 6°C)'),
    FloatVar('CDAY', 5, 1, info='')
}
