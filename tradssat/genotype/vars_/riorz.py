from tradssat.tmpl.var import CharacterVar

cul_vars_RIORZ = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ORYZA file name', 15, info='Name of ORYZA2000 crop file'),
}
