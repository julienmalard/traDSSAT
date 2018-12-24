from tradssat.tmpl.var import FloatVar, IntegerVar

vars_ = {
    IntegerVar('StYr', 5, info='Start year'),
    IntegerVar('StMn', 5, info='Start month'),
    IntegerVar('SpYr', 5, info='Stop year'),
    IntegerVar('SpMn', 5, info='Stop month'),

    IntegerVar('yr', 4, spc=0, info='Year'),
    IntegerVar('mo', 2, info='Month'),
    FloatVar('srmn', 5, 2, info='Solar radiation mean, MJ m-2 day-1'),
    FloatVar('srsd', 5, 2, info='Solar radiation standard deviation, MJ m-2 day-1'),
    FloatVar('txmn', 5, 2, info='Temperature maximum mean, °C'),
    FloatVar('txsd', 5, 2, info='Temperature maximum standard deviation, °C'),
    FloatVar('tnmn', 5, 2, info='Temperature minimum mean, °C'),
    FloatVar('tnsd', 5, 2, info='Temperature minimum standard deviation, °C'),
    FloatVar('ramn', 5, 2, info='Rainfall mean, mm'),
    FloatVar('rasd', 5, 2, info='Rainfall standard deviation, mm'),

}
