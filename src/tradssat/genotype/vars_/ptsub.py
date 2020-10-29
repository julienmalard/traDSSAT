from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_PTSUB = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar(
        'ECO#', 6, info='Ecotype code or this cultivar, points to the Ecotype in the ECO file (currently not used).'
    ),

    FloatVar('G2', 5, 0, info='Leaf area expansion rate after tuber initiation (cm2/m2 d)'),
    FloatVar('G3', 5, 1, info='Potential tuber growth rate (g/m2 d)'),
    FloatVar('PD', 5, 1,
             info='Index that supresses tuber growth during the period that immediately follows tuber induction'),
    FloatVar('P2', 5, 1, info='Tuber initiation sensitivity to long photoperiods'),
    FloatVar('TC', 5, 1, info='Upper critical temperature for tuber initiation (C)'),

}

eco_vars_PTSUB = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 18, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar('RUE1', 5, 1, info='Radiation use efficiency, ISTAGE=1, g plant dry matter/MJ PAR'),
    FloatVar('RUE2', 5, 1, info='Radiation use efficiency, ISTAGE>1, g plant dry matter/MJ PAR')

}
