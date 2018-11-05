from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

cul_vars_ALFRM = {
    CharacterVar('VAR#', 6, spc=0, info='Variety (cultivar) code'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Variety (cultivar) name'),
    IntegerVar('EXPNO', 5, info='Number of experiments used to estimate cultivar parameters'),

    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),
    FloatVar('CSDL', 5, 2, info='Critical Short Day Length below which reproductive development progresses with no daylength effect (for shortday plants) (hour)'),


}

eco_vars_ALFRM = {

}