from tradssat.tmpl.var import FloatVar, CharacterVar

cul_vars_PIALO = {
    CharacterVar('VAR#', 6, spc=0, info=''),
    CharacterVar('VAR-NAME', 16, header_fill='.', info=''),
    CharacterVar('EXPNO', 5, miss='', info=''),
    CharacterVar('ECO#', 6, info=''),

    FloatVar('P1', 5, 1, info='Growing degree days from first leaf emerged to end of stem growth'),
    FloatVar('P2', 5, 0, info='Growing degree days from forcing to sepals closed on youngest flower'),
    FloatVar('P3', 5, 0, info='Growing degree days from SCY to early flowering'),
    FloatVar('P4', 5, 0, info='Cumulative growing degree days from early flowering to maturity'),
    FloatVar('P5', 5, 0, info='Growing degree days from fruit harvest to physiological maturity'),
    FloatVar('P6', 5, 1, info='Growing degree days from root initiation to first leaf emerged'),
    FloatVar('G2', 5, 0, info='Potential eye number'),
    FloatVar('G3', 5, 1, info='Potential eye growth rate'),
    FloatVar('PHINT', 5, 1, info='')
}
