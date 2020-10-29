from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

vars_ = {
    CharacterVar('INSI', 4, spc=2, info='Institute + Site code'),
    FloatVar('LAT', 8, 3, info='Latitude, degrees (decimals)'),
    FloatVar('LONG', 8, 3, info='Longitude, degrees (decimals)'),
    FloatVar('ELEV', 5, 0, info='Elevation, m'),
    FloatVar('TAV', 5, 1, info='Air temperature average, °C'),
    FloatVar('AMP', 5, 1, info='Air temperature amplitude, monthly averages, °C'),
    FloatVar('REFHT', 5, 1, info='Height of temperature measurements, m'),
    FloatVar('WNDHT', 5, 1, info='Height of wind measurements, m'),
    IntegerVar('CCO2', 4, info='Atmospheric CO2, ppm'),

    CharacterVar('DATE', 5, spc=0, info='Year + days from Jan. 1'),
    FloatVar('SRAD', 5, 1, info='Solar radiation, MJ m-2 day-1'),
    FloatVar('TMAX', 5, 1, info='Air temperature maximum, °C'),
    FloatVar('TMIN', 5, 1, info='Air temperature minimum, °C'),
    FloatVar('RAIN', 5, 1, info='Precipitation, mm'),
    FloatVar('DEWP', 5, 1, info='Dewpoint temperature5, °C'),
    FloatVar('WIND', 5, 1, info='Wind run, km day-1'),
    FloatVar('PAR', 5, 1, info='Photosynthetic active radiation (PAR)5, moles m-2 day-1'),
    FloatVar('EVAP', 5, 1),
    FloatVar('RHUM', 5, 1)

}
