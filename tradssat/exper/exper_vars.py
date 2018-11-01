from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

vars_ = {
    CharacterVar('PEOPLE', 75, info='Names of scientists'),
    CharacterVar('ADDRESS', 75, info='Contact address of principal scientist'),
    CharacterVar('SITE', 75, info='Name and location of experimental site(s)'),

    FloatVar('PAREA', 6, 1, spc=3, info='Gross plot area per rep, m-2'),
    IntegerVar('PRNO', 5, info='Rows per plot'),
    FloatVar('PLEN', 5, 1, info='Plot length, m'),
    IntegerVar('PLDR', 5, info='Plots relative to drains, degrees'),
    IntegerVar('PLSP', 5, info='Plot spacing, cm'),
    CharacterVar('PLAY', 5, info='Plot layout'),
    FloatVar('HAREA', 5, 1, info='Harvest area, m-2'),
    IntegerVar('HRNO', 5, info='Harvest row number'),
    FloatVar('HLEN', 5, 1, info='Harvest row length, m'),
    CharacterVar('HARM', 15, info='Harvest method'),

    CharacterVar('NOTES', 75, info='Notes'),

    IntegerVar('N', 2, spc=0, info='Treatment number'),
    IntegerVar('R', 1, info='Rotation component: number (default=1)'),
    IntegerVar('O', 1, info='Rotation component: option (default=1)'),
    IntegerVar('C', 1, info='Crop component number (default = 0)'),
    CharacterVar('TNAME', 25, info='Treatment name'),
    IntegerVar('CU', 2, info='Cultivar level'),
    IntegerVar('FL', 2, info='Field level'),
    IntegerVar('SA', 2, info='Soil analysis level'),
    IntegerVar('IC', 2, info='Initial conditions level'),
    IntegerVar('MP', 2, info='Planting level'),
    IntegerVar('MI', 2, info='Irrigation level'),
    IntegerVar('MF', 2, info='Fertilizer level'),
    IntegerVar('MR', 2, info='Residue level'),
    IntegerVar('MC', 2, info='Chemical applications level'),
    IntegerVar('MT', 2, info='Tillage and rotations level'),
    IntegerVar('ME', 2, info='Environmental modifications level'),
    IntegerVar('MH', 2, info='Harvest level'),
    IntegerVar('SM', 2, info='Simulation control level'),

    IntegerVar('C', 2, info='Cultivar level'),
    CharacterVar('CR', 2, info='Crop code'),
    CharacterVar('INGENO', 6, info='Cultivar identifier (Institute code + Number)'),
    CharacterVar('CNAME', 16, info='Cultivar name'),



}
