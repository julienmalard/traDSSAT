from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

trt = 'TREATMENTS'

vars_ = {

    # General
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

    # Treatments
    IntegerVar('N', 2, spc=0, sect=trt, info='Treatment number'),
    IntegerVar('R', 1, sect=trt, info='Rotation component: number (default=1)'),
    IntegerVar('O', 1, sect=trt, info='Rotation component: option (default=1)'),
    IntegerVar('C', 1, sect=trt, info='Crop component number (default = 0)'),
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
    IntegerVar('C', 2, spc=0, sect='CULTIVARS', info='Cultivar level'),
    CharacterVar('CR', 2, info='Crop code'),
    CharacterVar('INGENO', 6, info='Cultivar identifier (Institute code + Number)'),
    CharacterVar('CNAME', 16, info='Cultivar name'),

    # Fields
    IntegerVar('L', 2, spc=0, sect='FIELDS', info='Field level '),
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
    IntegerVar('A', 2, spc=0, sect='SOIL ANALYSIS', info='Soil analysis level'),
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
    IntegerVar('C', 2, spc=0, sect='INITIAL CONDITIONS', info='Initial conditions level'),
    CharacterVar('PCR', 5, info='Previous crop code'),
    IntegerVar('ICDAT', 5, info='Initial conditions measurement date, year + days'),
    FloatVar('ICRT', 5, 0, info='Root weight from previous crop, kg ha-1'),
    FloatVar('ICND', 5, 0, info='Nodule weight from previous crop, kg ha-1'),
    FloatVar('ICRN', 5, 2, info='Rhizobia number, 0 to 1 scale (default = 1)'),
    FloatVar('ICRE', 5, 2, info='Rhizobia effectiveness, 0 to 1 scale (default = 1)'),

    # todo: define and verify
    FloatVar('ICWD', 5, 2),
    FloatVar('ICRES', 5, 0),
    FloatVar('ICREN', 5, 1),
    FloatVar('ICREP', 5, 0),
    FloatVar('ICRIP', 5, 0),
    FloatVar('ICRID', 5, 0),
    CharacterVar('ICNAME', 25, info='Inicial condition level name'),

    FloatVar('ICBL', 5, 2, info='Depth, base of layer, cm'),
    FloatVar('SH2O', 5, 3, info='Water, cm3 cm-3 x 100 volume percent'),
    FloatVar('SNH4', 5, 1, info='Ammonium, KCl, g elemental N Mg-1 soil'),
    FloatVar('SNO3', 5, 1, info='Nitrate, KCl, g elemental N Mg-1 soil'),

    # Planting details
    IntegerVar('P', 2, spc=0, sect='PLANTING DETAILS', info='Planting level number'),
    IntegerVar('PDATE', 5, info='Planting date, year + days from Jan. 1'),
    IntegerVar('EDATE', 5, info='Emergence date, earliest treatment'),
    FloatVar('PPOP', 5, 1, info='Plant population at seeding, plants m-2'),
    FloatVar('PPOE', 5, 1, info='Plant population at emergence, plants m-2 '),
    CharacterVar(
        'PLME', 1, spc=5, info='Planting method, transplant (T), seed (S), pregerminated seed (P) or nursery (N)'
    ),
    CharacterVar('PLDS', 1, spc=5, info='Planting distribution, row (R), broadcast (B) or hill (H) '),
    FloatVar('PLRS', 5, 0, info='Row spacing, cm'),
    FloatVar('PLRD', 5, 0, info='Row direction, degrees from N'),
    FloatVar('PLDP', 5, 1, info='Planting depth, cm'),
    FloatVar('PLWT', 5, 0, info='Planting material dry weight, kg ha-1'),
    FloatVar('PAGE', 5, 0, info='Transplant age, days '),
    FloatVar('PENV', 5, 1, info='Temp. of transplant environment, °C'),
    FloatVar('PLPH', 5, 1, info='Plants per hill (if appropriate)'),

    # Todo: check and document
    FloatVar('SPRL', 5, 0),
    CharacterVar('PLNAME', 35, info='Planting details level name'),

    # IRRIGATION AND WATER MANAGEMENT
    CharacterVar('I', 2, spc=0, sect='IRRIGATION AND WATER MANAGEMENT', info='Irrigation level'),
    FloatVar('EFIR', 5, 1, info='Irrigation application efficiency, fraction'),
    FloatVar('IDEP', 5, 0, info='Management depth for automatic application, cm'),
    FloatVar('ITHR', 5, 0, info='Threshold for automatic appl., % of max. available'),
    FloatVar('IEPT', 5, 0, info='End point for automatic appl., % of max. available'),
    CharacterVar('IOFF', 5, info='End of applications, growth stage '),
    CharacterVar('IAME', 5, info='Method for automatic applications, code'),
    FloatVar('IAMT', 5, 0, info='Amount per irrigation if fixed, mm'),

    # Todo: check size
    CharacterVar('IRNAME', 25, info='Irrigation level name'),

    IntegerVar('IDATE', 5, info='Irrigation date, year + day or days from planting'),
    CharacterVar('IROP', 5, info='Irrigation operation, code'),
    FloatVar(
        'IRVAL', 5, 0,
        info='Irrigation amount, depth of water/water table, bund height, or percolation rate, mm or mm day -1'
    ),

    # FERTILIZERS (INORGANIC)
    IntegerVar('F', 2, spc=0, sect='FERTILIZERS (INORGANIC)', info='Fertilizer application level'),
    IntegerVar('FDATE', 5, info='Fertilization date, year + day or days from planting'),
    CharacterVar('FMCD', 5, info='Fertilizer material, code'),
    CharacterVar('FACD', 5, info='Fertilizer application/placement, code'),
    FloatVar('FDEP', 5, 0, info='Fertilizer incorporation/application depth, cm'),


}
