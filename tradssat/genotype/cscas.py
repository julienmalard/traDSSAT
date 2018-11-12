from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_CSCAS = {
    CharacterVar('VAR#', 6, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    FloatVar('EXP#', 6, 0, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Ecotype code for this cultivar,points to entry in the ECO file'),

}

('BxyND   ', info='Duration from branch x to branch y (ie.tier x,node number)'),

('HMPC    ', info='Harvest product moisture content (%)'),
('LA1S    ', info='Area/leaf (cm2) of the first leaves when growing without stress.'),
('LAFND   ', info='Node # at which the end of cycle area/leaf reached (#)'),
('LAFS    ', info='End of cycle area/leaf (cm2)'),
('LAXND   ', info='Node # at which maximum potential area/leaf reached (#)'),
('LAXN2   ', info='Node # at which potential area/leaf begins to decline (#)'),
('LAXS    ', info='Area/leaf at maximum area/leaf (cm2)'),
('LLIFA   ', info='Leaf life,from full expansion to start senescence (Thermal units)'),
('LPEFR   ', info='Leaf petiole fraction (fr of lamina+petiole)'),
('PHINT   ', info='Interval between leaf tip appearances for first leaves (oC.d)'),
('PPSn    ', info='Photoperiod sensitivity for phase n. (% drop for 10h pp.change)'),
('SLAS    ', info='Specific leaf lamina area when crop growing without stress (cm2/g)'),
('SRFR    ', info='Fr.of assimilate designated for tops sent to storage root (#)'),
('SR#W    ', info='Storage root number per unit canopy weight at initiation (#/g)'),
('STFR    ', info='Stem fraction of assimilate destined for canopy growth (#)'),



eco_vars_CSCAS = {

}