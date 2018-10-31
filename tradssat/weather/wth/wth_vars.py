from tradssat.file.var import CharacterVar, FloatVar, IntegerVar

sect = 'WEATHER'
vars_ = {
    CharacterVar('INSI', sect, 4, info='Institute + Site code'),
    FloatVar('LAT', sect, 8, 3, info='Latitude, degrees (decimals)'),
    FloatVar('LONG', sect, 8, 3, info='Longitude, degrees (decimals)'),
    FloatVar('ELEV', sect, 5, 0, info='Elevation, m'),
    FloatVar('TAV', sect, 5, 1, info='Air temperature average, °C'),
    FloatVar('AMP', sect, 5, 1, info='Air temperature amplitude, monthly averages, °C'),
    FloatVar('REFHT', sect, 5, 1, info='Height of temperature measurements, m'),
    FloatVar('WNDHT', sect, 5, 1, info='Height of wind measurements, m'),

    IntegerVar('DATE', sect, 5, info='Year + days from Jan. 1'),
    FloatVar('SRAD', sect, 5, 1, info='Solar radiation, MJ m-2 day-1'),
    FloatVar('TMAX', sect, 5, 1, info='Air temperature maximum, °C'),
    FloatVar('TMIN', sect, 5, 1, info='Air temperature minimum, °C'),
    FloatVar('RAIN', sect, 5, 1, info='Precipitation, mm'),
    FloatVar('DEWP', sect, 5, 1, info='Dewpoint temperature5, °C'),
    FloatVar('WIND', sect, 5, 1, info='Wind run5, km day-1'),
    FloatVar('PAR', sect, 5, 1, info='Photosynthetic active radiation (PAR)5, moles m-2 day-1')

}
