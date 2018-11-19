from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_SCCSP = {
    CharacterVar(
        'VAR#', 6, spc=0, info='Identification code or number for a specific cultivar used by  DSSAT program.'
    ),
    CharacterVar(
        'VAR-NAME', 16, header_fill='.', info='Name of cultivar as recognized commercially or within industry.'
    ),
    IntegerVar('EXPNO', 5, miss='.', info='Number of experiments used to estimate cultivar parameters.'),
    CharacterVar('ECO#', 6, info='Ecotype code of this cultivar in the ECO input file'),


}

eco_vars_SCCSP = {

}
