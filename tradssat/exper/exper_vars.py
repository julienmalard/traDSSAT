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
    CharacterVar('TNAME', 25, header_fill='.', info='Treatment name'),
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

    # Cultivars
    # IntegerVar('C', 2, spc=0, info='Cultivar level'),  # todo: fixme
    CharacterVar('CR', 2, info='Crop code'),
    CharacterVar('INGENO', 6, info='Cultivar identifier (Institute code + Number)'),
    CharacterVar('CNAME', 16, info='Cultivar name'),

    # Fields
    IntegerVar('L', 2, spc=0, info='Field level '),
    CharacterVar('ID_FIELD', 8, info='Field ID (Institute + Site + Field)'),
    CharacterVar('WSTA', 8, info='Weather station code (Institute+Site)'),
    CharacterVar('FLSA', 5, info='Slope and aspect, degrees from horizontal plus direction (W, NW, etc.)'),
    FloatVar('FLOB', 5, 0, info='Obstruction to sun, degrees'),
    CharacterVar('FLDT', 5, info='Drainage type, code'),
    FloatVar('FLDD', 5, 0, info='Drain depth, cm'),
    FloatVar('FLDS', 5, 0, info='Drain spacing, m'),
    CharacterVar('FLST', 5, info='Surface stones(Abundance,%+Size,S,M,L)'),
    CharacterVar('SLTX', 5, info='Soil texture'),
    FloatVar('SLDP', 5, 0, info='Soil depth, cm'),
    CharacterVar('ID_SOIL', 10, info='Soil ID (Institute+Site+Year+Soil)'),
    CharacterVar('FLNAME', 25, info='Field level name'),  # size is guess

    # Todo: define and verify
    FloatVar('XCRD', 15, 5, header_fill='.'),
    FloatVar('YCRD', 15, 5, header_fill='.'),
    FloatVar('ELEV', 9, 2, header_fill='.'),
    FloatVar('AREA', 17, 1, header_fill='.'),
    IntegerVar('SLEN', 5, header_fill='.'),
    FloatVar('FLWR', 5, 1, header_fill='.'),
    FloatVar('SLAS', 5, 1, header_fill='.'),
    CharacterVar('FLHST', 5),
    CharacterVar('FHDUR', 5),

    # Soil analysis
    IntegerVar('A', 2, spc=0, info='Soil analysis level'),
    IntegerVar('SADAT', 5, info='Analysis date, year + days from Jan. 1'),
    CharacterVar('SMHB', 5, info='pH in buffer determination method, code'),
    CharacterVar('SMPX', 5, info='Phosphorus determination method, code'),
    CharacterVar('SMKE', 5, info='Potassium determination method, code'),
    FloatVar('SABL', 5, 0, info='Depth, base of layer, cm'),
    FloatVar('SADM', 5, 1, info='Bulk density, moist, g cm-3'),
    FloatVar('SAOC', 5, 2, info='Organic carbon, g kg-1 '),
    FloatVar('SANI', 5, 2, info='Total nitrogen, g kg-1'),
    FloatVar('SAPHW', 5, 1, info='pH in water'),
    FloatVar('SAPHB', 5, 1, info='pH in buffer'),
    FloatVar('SAPX', 5, 1, info='Phosphorus, extractable, mg kg-1 '),
    FloatVar('SAKE', 5, 1, info='Potassium, exchangeable, cmol kg-1'),
    FloatVar('SASC', 5, 1),
    CharacterVar('SANAME', 25, info='Soil analysis level name'),  # size is guess

    # Initial conditions

}
