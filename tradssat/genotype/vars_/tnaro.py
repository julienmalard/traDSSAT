from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_TNARO = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used to estimate cultivar parameters.'),
    CharacterVar(
        'ECO#', 6,
        info='Ecotype code or this cultivar, points to the Ecotype in the ECO file (currently not used).'
    ),
    FloatVar('P1', 5, 0),
    FloatVar('P3', 5, 0),
    FloatVar('P4', 5, 0),
    FloatVar('P5', 5, 0),
    FloatVar('G2', 5, 2),
    FloatVar('G3', 5, 2),
    FloatVar('G4', 5, 2),
    FloatVar('PHINT', 5, 1),
    FloatVar('PCINT', 5, 1),
    FloatVar('PCGRD', 5, 2)

}
