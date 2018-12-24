from tradssat.tmpl.var import FloatVar, IntegerVar

vars_ = {
    IntegerVar('StYr', 5, info='Start year'),
    IntegerVar('StMn', 5, info='Start month'),
    IntegerVar('SpYr', 5, info='Stop year'),
    IntegerVar('SpMn', 5, info='Stop month'),

    IntegerVar('yr', 4, spc=0, info='Year'),
    IntegerVar('mo', 2, info='Month'),
    FloatVar('srmn', 5, 2, info=''),
FloatVar('srsd', 5, 2, info=''),
FloatVar('txmn', 5, 2, info=''),
FloatVar('txsd', 5, 2, info=''),
FloatVar('tnmn', 5, 2, info=''),
FloatVar('tnsd', 5, 2, info=''),
FloatVar('ramn', 5, 2, info=''),
FloatVar('rasd', 5, 2, info=''),
    FloatVar('LAT', 8, 3, info='Latitude, degrees (decimals)'),
    FloatVar('LONG', 8, 3, info='Longitude, degrees (decimals)'),
    FloatVar('ELEV', 5, 0, info='Elevation, m'),
    FloatVar('TAV', 5, 1, info='Air temperature average, °C'),
    FloatVar('AMP', 5, 1, info='Air temperature amplitude, monthly averages, °C'),
    FloatVar('REFHT', 5, 1, info='Height of temperature measurements, m'),
    FloatVar('WNDHT', 5, 1, info='Height of wind measurements, m'),

    IntegerVar('DATE', 5, spc=0, info='Year + days from Jan. 1'),
    FloatVar('SRAD', 5, 1, info='Solar radiation, MJ m-2 day-1'),
    FloatVar('TMAX', 5, 1, info='Air temperature maximum, °C'),
    FloatVar('TMIN', 5, 1, info='Air temperature minimum, °C'),
    FloatVar('RAIN', 5, 1, info='Precipitation, mm'),
    FloatVar('DEWP', 5, 1, info='Dewpoint temperature5, °C'),
    FloatVar('WIND', 5, 1, info='Wind run5, km day-1'),
    FloatVar('PAR', 5, 1, info='Photosynthetic active radiation (PAR)5, moles m-2 day-1'),
    FloatVar('EVAP', 5, 1),
    FloatVar('RHUM', 5, 1)

}
