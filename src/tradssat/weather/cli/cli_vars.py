from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

vars_ = {
    CharacterVar('INSI', 4, spc=2, info='Institute + Site code'),
    FloatVar('LAT', 8, 3, info='Latitude, degrees (decimals)'),
    FloatVar('LONG', 8, 3, info='Longitude, degrees (decimals)'),
    FloatVar('ELEV', 5, 0, info='Elevation, m'),
    FloatVar('TAV', 5, 1, info='Air temperature average, °C'),
    FloatVar('AMP', 5, 1, info='Air temperature amplitude, monthly averages, °C'),
    FloatVar('SRAY', 5, 1, info=''),
    FloatVar('TMXY', 5, 1, info=''),
    FloatVar('TMNY', 5, 1, info=''),
    IntegerVar('RAIY', 5, info=''),

    IntegerVar('START', 5, spc=0, info=''),
    IntegerVar('DURN', 5, info=''),
    FloatVar('ANGA', 5, 2, info=''),
    FloatVar('ANGB', 5, 2, info=''),
    FloatVar('REFHT', 5, 1, info=''),
    FloatVar('WNDHT', 5, 1, info=''),
    CharacterVar('SOURCE', 50, info=''),
    IntegerVar('GSST', 5, info=''),
    IntegerVar('GSDU', 5),

}
