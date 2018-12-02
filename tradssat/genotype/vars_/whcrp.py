from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_WHCRP = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXP#', 5, miss='.', info='Number of experiments,treatments used to estimate coefficients.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),
    FloatVar('G#WTS', 5, 1, info='Standard grain number per unit canopy weight at anthesis (#/g)'),
    FloatVar('GWTS', 5, 0, info='Standard grain size,optimum conditions,normal plant density (mg)'),
    FloatVar('LA1S', 5, 1, info='Area of standard first leaf (cm2)'),
    FloatVar('LAFV', 5, 2, info='Increase in potential area of leaves,vegetative phase (fr/leaf)'),
    FloatVar('LAFR', 5, 2, info='Increase in potential area of leaves,reproductive phase (fr/leaf)'),
    FloatVar('P1', 5, 0, info='Duration of phase number 1 (PVoC.D)'),
    FloatVar('P2', 5, 0, info='Duration of phase number 2 (PVoC.D)'),
    FloatVar(
        'P3', 5, 0,
        info='Duration of phase number 3 (PVoC.D) BUT P3 and P4 are \'dummy\' values inserted to set the total '
             'duration of the P3+P4 phase. The actual balance between P3 and P4 is determined internally depending on '
             'the leaf number at the end of phase 1.'
    ),
    FloatVar(
        'P4', 5, 0,
        info='Duration of phase number 4 (PVoC.D) BUT P3 and P4 are \'dummy\' values inserted to set the total '
             'duration of the P3+P4 phase. The actual balance between P3 and P4 is determined internally depending on '
             'the leaf number at the end of phase 1.'
    ),
    FloatVar('P5', 5, 0, info='Duration of phase number 5 (PVoC.D)'),
    FloatVar('P6', 5, 0, info='Duration of phase number 6 (PVoC.D)'),
    FloatVar('P7', 5, 0, info='Duration of phase number 7 (PVoC.D)'),
    FloatVar('P8', 5, 1, info='Duration of phase number 8 (PVoC.D)'),
    FloatVar('PPS1', 5, 1, info='Photoperiod sensitivity,phase(1). % drop in rate,10h pp.change.'),
    FloatVar('PPS2', 5, 0, info='Photoperiod sensitivity,phase(2). % drop in rate,10h pp.change.'),
    FloatVar('PHINT', 5, 0, info='Interval between successive leaf appearances. (oC.d)'),
    FloatVar('SHWTS', 5, 1, info='Standard,non-stressed shoot dry weight (incl.grain),maturity (g)'),
    FloatVar('SLAS', 5, 0, info='Specific leaf area,standard (cm2/g)'),
    FloatVar('VREQ', 5, 4, info='Vernalization required for max.development rate (VDays)'),
    FloatVar('VBASE', 5, 0, info='Vernalization requirement before any effect (VDays)'),
    FloatVar('VEFF', 5, 2, info='Vernalization effect (Rate reduction when unvernalized (fr)'),
}

eco_vars_WHCRP = {

}
