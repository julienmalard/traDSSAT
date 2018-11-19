from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_MZIXM = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Name of cultivar.'),
    IntegerVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

}

eco_vars_MZIXM = {

}
