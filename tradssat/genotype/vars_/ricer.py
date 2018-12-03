from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_RICER = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (currently not used)'),

    FloatVar(
        'P1 ', 5, 1,
        info='Time period (expressed as growing degree days [GDD] in øC above a base temperature of 9øC) from seedling '
             'emergence during which the rice plant is not responsive to changes in photoperiod. This period is also '
             'referred to as the basic vegetative phase of the plant.'
    ),
    FloatVar(
        'P2O', 5, 1,
        info='Critical photoperiod or the longest day length (in hours) at which the development occurs at a maximum '
             'rate. At values higher than P2O developmental rate is slowed, hence there is delay due to longer day '
             'lengths.'
    ),
    FloatVar(
        'P2R', 5, 1,
        info='Extent to which phasic development leading to panicle initiation is delayed (expressed as GDD in øC) '
             'for each hour increase in photoperiod above P2O.'
    ),
    FloatVar(
        'P5 ', 5, 1,
        info='Time period in GDD øC) from beginning of grain filling (3 to 4 days after flowering) to physiological '
             'maturity with a base temperature of 9øC.'
    ),
    FloatVar(
        'G1 ', 5, 1,
        info='Potential spikelet number coefficient as estimated from the number of spikelets per g of main culm dry '
             'weight (less lead blades and sheaths plus spikes) at anthesis. A typical value is 55.'
    ),
    FloatVar(
        'G2 ', 5, 4,
        info='Single grain weight (g) under ideal growing conditions, i.e. nonlimiting light, water, nutrients, '
             'and absence of pests and diseases.'
    ),
    FloatVar(
        'G3 ', 5, 2,
        info='Tillering coefficient (scaler value) relative to IR64 cultivar under ideal conditions. A higher '
             'tillering cultivar would have coefficient greater than 1.0.'
    ),
    FloatVar(
        'G4 ', 5, 2,
        info='Temperature tolerance coefficient. Usually 1.0 for varieties grown in normal environments. G4 for '
             'japonica type rice growing in a warmer environment would be 1.0 or greater. Likewise, the G4 value for '
             'indica type rice in very cool environments or season would be less than 1.0.'
    ),
    FloatVar('PHINT', 5, 1, info=''),
    FloatVar('G5', 5, 1, info='')

}
