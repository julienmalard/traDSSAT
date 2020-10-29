import re

from tradssat.tmpl.var import CharacterVar, FloatVar, IntegerVar

TRT_HEAD = re.compile(r'TREATMENTS(\W+[-]+FACTOR LEVELS[-]+)?')
GENERAL = 'GENERAL'

header_vars = [
    CharacterVar('EXPCODE', 10, info='Experiment identifier'),
    CharacterVar('ENAME', 60, info='Experiment name')
]

main_vars = {

    # General
    CharacterVar('PEOPLE', 75, sect=GENERAL, info='Names of scientists'),
    CharacterVar('ADDRESS', 75, sect=GENERAL, info='Contact address of principal scientist'),
    CharacterVar('SITE', 75, sect=GENERAL, info='Name and location of experimental site(s)'),

    FloatVar('PAREA', 6, 1, sect=GENERAL, spc=3, info='Gross plot area per rep, m-2'),
    IntegerVar('PRNO', 5, sect=GENERAL, info='Rows per plot'),
    FloatVar('PLEN', 5, 1, sect=GENERAL, info='Plot length, m'),
    IntegerVar('PLDR', 5, sect=GENERAL, info='Plots relative to drains, degrees'),
    IntegerVar('PLSP', 5, sect=GENERAL, info='Plot spacing, cm'),
    CharacterVar('PLAY', 5, sect=GENERAL, info='Plot layout'),
    FloatVar('HAREA', 5, 1, sect=GENERAL, info='Harvest area, m-2'),
    IntegerVar('HRNO', 5, sect=GENERAL, info='Harvest row number'),
    FloatVar('HLEN', 5, 1, sect=GENERAL, info='Harvest row length, m'),
    CharacterVar('HARM', 15, sect=GENERAL, info='Harvest method'),

    CharacterVar('NOTES', 500, sect=GENERAL, info='Notes'),

    # Treatments
    IntegerVar('N', 2, spc=0, sect=TRT_HEAD, info='Treatment number'),
    IntegerVar('R', 1, sect=TRT_HEAD, info='Rotation component: number (default=1)'),
    IntegerVar('O', 1, sect=TRT_HEAD, info='Rotation component: option (default=1)'),
    IntegerVar('C', 1, sect=TRT_HEAD, info='Crop component number (default = 0)'),
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
    FloatVar('ICREN', 5, 2),
    FloatVar('ICREP', 5, 0),
    FloatVar('ICRIP', 5, 0),
    FloatVar('ICRID', 5, 0),
    CharacterVar('ICNAME', 25, info='Inicial condition level name'),

    FloatVar('ICBL', 5, 0, info='Depth, base of layer, cm'),
    FloatVar('SH2O', 5, 3, info='Water, cm3 cm-3 x 100 volume percent'),
    FloatVar('SNH4', 5, 1, info='Ammonium, KCl, g elemental N Mg-1 soil'),
    FloatVar('SNO3', 5, 1, info='Nitrate, KCl, g elemental N Mg-1 soil'),

    # Planting details
    IntegerVar('P', 2, spc=0, sect='PLANTING DETAILS', info='Planting level number'),
    IntegerVar('PDATE', 5, info='Planting date, year + days from Jan. 1'),
    IntegerVar('EDATE', 5, info='Emergence date, earliest treatment'),
    FloatVar('PPOP', 5, 2, info='Plant population at seeding, plants m-2'),
    FloatVar('PPOE', 5, 2, info='Plant population at emergence, plants m-2 '),
    CharacterVar(
        'PLME', 1, spc=5, info='Planting method, transplant (T), seed (S), pregerminated seed (P) or nursery (N)'
    ),
    CharacterVar('PLDS', 1, spc=5, info='Planting distribution, row (R), broadcast (B) or hill (H) '),
    FloatVar('PLRS', 5, 1, info='Row spacing, cm'),
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
    IntegerVar('I', 2, spc=0, sect='IRRIGATION AND WATER MANAGEMENT', info='Irrigation level'),
    FloatVar('EFIR', 5, 2, info='Irrigation application efficiency, fraction'),
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
        'IRVAL', 5, 1,
        info='Irrigation amount, depth of water/water table, bund height, or percolation rate, mm or mm day -1'
    ),

    # FERTILIZERS (INORGANIC)
    IntegerVar('F', 2, spc=0, sect='FERTILIZERS (INORGANIC)', info='Fertilizer application level'),
    IntegerVar('FDATE', 5, info='Fertilization date, year + day or days from planting'),
    CharacterVar('FMCD', 5, info='Fertilizer material, code'),
    CharacterVar('FACD', 5, info='Fertilizer application/placement, code'),
    FloatVar('FDEP', 5, 0, info='Fertilizer incorporation/application depth, cm'),
    FloatVar('FAMN', 5, 0, info='N in applied fertilizer, kg ha-1'),
    FloatVar('FAMP', 5, 0, info='P in applied fertilizer, kg ha-1'),
    FloatVar('FAMK', 5, 0, info='K in applied fertilizer, kg ha-1'),
    FloatVar('FAMC', 5, 0, info='Ca in applied fertilizer, kg ha-1'),
    FloatVar('FAMO', 5, 0, info='Other elements in applied fertilizer, kg ha-1'),
    CharacterVar('FOCD', 5, info='Other element code, e.g., MG'),

    # Todo: check size
    CharacterVar('FERNAME', 25, info='Fertilizer level name'),

    # RESIDUES AND ORGANIC FERTILIZER
    IntegerVar('R', 2, spc=0, sect='RESIDUES AND ORGANIC FERTILIZER', info='Residue management level'),
    IntegerVar('RDATE', 5, info='Incorporation date, year + days'),
    CharacterVar('RCOD', 5, info='Residue material, code'),
    FloatVar('RAMT', 5, 0, info='Residue amount, kg ha-1'),
    FloatVar('RESN', 5, 2, info='Residue nitrogen concentration, %'),
    FloatVar('RESP', 5, 2, info='Residue phosphorus concentration, %'),
    FloatVar('RESK', 5, 2, info='Residue potassium concentration, %'),
    FloatVar('RINP', 5, 0, info='Residue incorporation percentage, %'),
    FloatVar('RDEP', 5, 0, info='Residue incorporation depth, cm'),

    # Todo: check
    FloatVar('RMET', 5, 0, info=''),
    CharacterVar('RENAME', 25, info='Residue management level name'),

    # CHEMICAL APPLICATIONS
    IntegerVar('C', 2, spc=0, sect='CHEMICAL APPLICATIONS', info='Chemical applications level'),
    IntegerVar('CDATE', 5, info='Application date, year + day or days from planting'),
    CharacterVar('CHCOD', 5, info='Chemical material, code'),
    FloatVar('CHAMT', 5, 2, info='Chemical application amount, kg ha-1'),
    CharacterVar('CHME', 5, info='Chemical application method, code'),
    FloatVar('CHDEP', 5, 0, info='Chemical application depth, cm'),
    CharacterVar('CHT', 5, info='Chemical targets'),
    CharacterVar('CHNAME', 25, info='Chemical application level name'),  # todo: check size

    # TILLAGE
    IntegerVar('T', 2, spc=0, info='Tillage level'),
    IntegerVar('TDATE', 5, info='Tillage date, year + day'),
    CharacterVar('TIMPL', 5, info='Tillage implement, code'),
    FloatVar('TDEP', 5, 0, info='Tillage implement, code'),

    # ENVIRONMENT MODIFICATIONS
    IntegerVar('E', 2, spc=0, info='Environment modifications level '),
    IntegerVar('ODATE', 5, info='Modification date, year + day or days from planting'),
    # The following are officially 2 variables each in DSSAT (code + value). However, as this is almost impossible
    # to implement sanely here (no space between variable names, and repeated names in the same section, we will treat
    # these as character values including both the code and value.
    CharacterVar('EDAY', size=5, info='Daylength adjustment, factor (A, S, M, R) + h'),
    CharacterVar('ERAD', size=5, info='Radiation adjustment, factor (A, S, M, R) + MJ m-2 d-1'),
    CharacterVar('EMAX', size=5, info='Temperature (maximum) adjustment, factor (A, S, M, R) + °C'),
    CharacterVar('EMIN', size=5, info='Temperature (minimum) adjustment, factor (A, S, M, R) + °C'),
    CharacterVar('ERAIN', size=5, info='Precipitation adjustment, factor (A, S, M, R) + mm'),
    CharacterVar('ECO2', size=5, info='CO2 adjustment, factor (A, S, M, R) + vpm'),
    CharacterVar('EDEW', size=5, info='Humidity (dew pt) adjustment, factor (A, S, M, R) + °C'),
    CharacterVar('EWIND', size=5, info='Daylength adjustment, factor (A, S, M, R) + h'),
    CharacterVar('ENVNAME', size=25, info='Environmental modification level name'),  # todo: check size

    # HARVEST DETAILS
    IntegerVar('H', 2, spc=0, info='Harvest level'),
    IntegerVar('HDATE', 5, info='Harvest date, year + day or days from planting'),
    CharacterVar('HSTG', 5, info='Harvest stage'),
    CharacterVar('HCOM', 5, info='Harvest component, code'),
    CharacterVar('HSIZE', 5, info='Harvest size group, code'),
    FloatVar('HPC', 5, 0, info='Harvest percentage, %'),

    # Todo: check
    FloatVar('HBPC', 5, 0, info=''),
    CharacterVar('HNAME', 25, info='Harvest details level name'),

    # SIMULATION CONTROLS
    IntegerVar('N', 2, spc=0, sect='SIMULATION CONTROLS', info='Simulation control level number'),
    CharacterVar('GENERAL', 11, info='Identifier'),
    IntegerVar('NYERS', 2, spc=4, info='Years'),
    IntegerVar('NREPS', 2, spc=4, info='Replications'),
    CharacterVar(
        'START', 1, spc=5,
        info='Start of Simulation, code: '
             'E = On reported emergence date; '
             'I = When initial conditions measured; '
             'P = On reported planting date; '
             'S = On specified date'
    ),
    IntegerVar('SDATE', 5, info='Date, year + day (if needed)'),
    IntegerVar('RSEED', 5, info='Random number seed'),
    CharacterVar('SNAME', 25, header_fill='.', info='Title'),
    CharacterVar('SMODEL', 5, info=''),  # todo: check

    CharacterVar('OPTIONS', 11, info='Identifier'),
    CharacterVar('WATER', 1, spc=5, info='Water (Y = yes; N = no)'),
    CharacterVar('NITRO', 1, spc=5, info='Nitrogen (Y = yes; N = no)'),
    CharacterVar('SYMBI', 1, spc=5, info='Symbiosis (Y= yes, N= no, U= unlimited N)'),
    CharacterVar('PHOSP', 1, spc=5, info='Phosphorus (Y = yes; N = no)'),
    CharacterVar('POTAS', 1, spc=5, info='Potassium (Y = yes; N = no)'),
    CharacterVar('DISES', 1, spc=5, info='Diseases and other pests (Y = yes; N = no)'),
    CharacterVar('CHEM', 1, spc=5, info='Chemical applications (Y = yes; N = no)'),
    CharacterVar('TILL', 1, spc=5, info='Tillage (Y = yes; N = no)'),
    CharacterVar('CO2', 1, spc=5, miss='', info='CO2 effects (Y = yes; N = no)'),

    CharacterVar('METHODS', 11, info='Identifier'),
    CharacterVar(
        'WTHER', 1, spc=5,
        info='Weather: '
             'M = Measured data, as recorded; '
             'G = Simulated data, stored as *.WTG files; '
             'S = Simulated data (Internal weather generator using monthly inputs); '
             'W = Simulated data (Internal WGEN weather generator) '
    ),
    CharacterVar(
        'INCON', 1, spc=5,
        info='Initial Soil Conditions: '
             'M = As reported; '
             'S = Simulated outputs from previous model run'
    ),
    CharacterVar(
        'LIGHT', 1, spc=5,
        info='Light interception: '
             'E = Exponential with LAI; '
             "H = ‘Hedgerow’ calculations"
    ),
    CharacterVar(
        'EVAPO', 1, spc=5,
        info='Evaporation: '
             'P = FAO - Penman; '
             'R = Ritchie modification of Priestley-Taylor'
    ),
    CharacterVar(
        'INFIL', 1, spc=5,
        info='Infiltration: '
             'R = Ritchie method; '
             'S = Soil Conservation Service routines'
    ),
    CharacterVar(
        'PHOTO', 1, spc=5,
        info='Photosynthesis: '
             'C = Canopy photosynthesis response curve; '
             'R = Radiation use efficiency; '
             'L = Leaf photosynthesis response curve'
    ),

    # Todo: check and document
    CharacterVar(
        'HYDRO', 1, spc=5,
        info=''
    ),
    IntegerVar('NSWIT', 1, spc=5, info=''),
    CharacterVar(
        'MESOM', 1, spc=5, info=''
    ),
    CharacterVar(
        'MESEV', 1, spc=5, info=''
    ),
    IntegerVar('MESOL', 1, spc=5),

    CharacterVar('MANAGEMENT', 11, info='Identifier'),
    CharacterVar(
        'PLANT', 1, spc=5,
        info='Planting/Transplanting: '
             'A = Automatic when conditions satisfactory; '
             'R = On reported date'
    ),
    CharacterVar(
        'IRRIG', 1, spc=5,
        info='Irrigation and Water Management: '
             'A = Automatic when required; '
             'N = Not irrigated; '
             'F = Automatic with fixed amounts at each irrigation date; '
             'R = On reported dates; '
             'D = As reported, in days after planting'
    ),
    CharacterVar(
        'FERTI', 1, spc=5,
        info='Fertilization: '
             'A = Automatic when required; '
             'N = Not fertilized; '
             'F = Automatic with fixed amounts at each fertilization date; '
             'R = On reported dates; '
             'D = As reported, in days after planting'
    ),
    CharacterVar(
        'RESID', 1, spc=5,
        info='Residue applications: '
             'A = Automatic for multiple years/crop sequences; '
             'N = No applications; '
             'F = Automatic with fixed amounts at each residue application date; '
             'R = On reported dates; '
             'D = As reported, in days after planting'
    ),
    CharacterVar(
        'HARVS', 1, spc=5,
        info='Harvest: '
             'A = Automatic when conditions satisfactory; '
             'G = At reported growth stage(s); '
             'M = At maturity; '
             'R = On reported date(s); '
             'D = On reported days after planting'
    ),

    CharacterVar('OUTPUTS', 11, info='Identifier'),
    CharacterVar('FNAME', 1, spc=5, info='Experiment (Y = yes, files named with the experiment code; N = no)'),
    CharacterVar('OVVEW', 1, spc=5, info='Overview (Y = yes, new; A = append; N = no)'),
    CharacterVar('SUMRY', 1, spc=5, info='Summary (Y = yes, new; A = append; N = no)'),
    IntegerVar('FROPT', 2, spc=4, info='Frequency of output (days)'),
    CharacterVar('GROUT', 1, spc=5, info='Growth (Y = yes; N = no)'),
    CharacterVar('CAOUT', 1, spc=5, info='Carbon (Y = yes; N = no)'),
    CharacterVar('WAOUT', 1, spc=5, info='Water (Y = yes; N = no)'),
    CharacterVar('NIOUT', 1, spc=5, info='Nitrogen (Y = yes; N = no)'),
    CharacterVar('MIOUT', 1, spc=5, info='Phosphorous (Y = yes; N = no)'),
    CharacterVar('DIOUT', 1, spc=5, info='Diseases and other pests (Y = yes; N = no)'),

    # todo: check and document
    CharacterVar('VBOSE', 1, spc=5, info='Wide (Y) or 80-column (N) daily outputs'),
    CharacterVar('CHOUT', 1, spc=5),
    CharacterVar('OPOUT', 1, spc=5),
    CharacterVar('FMOPT', 1, spc=5),

    # Automatic Management
    CharacterVar('AUTOMATIC MANAGEMENT', 0),  # No idea why this variable even exists

    CharacterVar('PLANTING', 11, info='Identifier'),
    IntegerVar('PFRST', 5, info='Earliest, year and day of year (YRDOY)'),
    IntegerVar('PLAST', 5, info='Latest, year and day of year (YRDOY)'),
    FloatVar('PH2OL', 5, 0, info='Lowermost soil water, % '),
    FloatVar('PH2OU', 5, 0, info='Uppermost soil water, %'),
    FloatVar('PH2OD', 5, 0, info='Management depth for water, cm'),
    FloatVar('PSTMX', 5, 0, info='Max. soil temp. (10 cm av.), °C'),
    FloatVar('PSTMN', 5, 0, info='Min. soil temp. (10 cm av.), °C'),

    CharacterVar('IRRIGATION', 11, info='Identifier'),
    FloatVar('IMDEP', 5, 0, info='Management depth, cm'),
    FloatVar('ITHRL', 5, 0, info='Threshold, % of maximum available'),
    FloatVar('ITHRU', 5, 0, info='End point, % of maximum available'),
    CharacterVar('IROFF', 5, info='End of applications, growth stage'),
    CharacterVar('IMETH', 5, info='Method, code'),
    FloatVar('IRAMT', 5, 0, info='Amount per irrigation, if fixed, mm'),
    FloatVar('IREFF', 5, 2, info='Irrigation application efficiency, fraction'),

    CharacterVar('NITROGEN', 11, info='Identifier'),
    FloatVar('NMDEP', 5, 0, info='Application depth, cm'),
    FloatVar('NMTHR', 5, 0, info='Threshold, N stress factor, %'),
    FloatVar('NAMNT', 5, 0, info='Amount per application, kg N ha-1'),
    CharacterVar('NCODE', 5, info='Material, code'),
    CharacterVar('NAOFF', 5, info='End of applications, growth stage'),

    CharacterVar('RESIDUES', 11, info='Identifier'),
    FloatVar('RIPCN', 5, 0, info='Incorporation percentage, % of remaining'),
    IntegerVar('RTIME', 5, info='Incorporation time, days after harvest'),
    FloatVar('RIDEP', 5, 0, info='Incorporation depth, cm'),

    CharacterVar('HARVEST', 11, info='Identifier'),
    IntegerVar('HFRST', 5, info='Earliest, days after maturity'),
    IntegerVar('HLAST', 5, info='Latest, year and day of year (YRDOY)'),
    FloatVar('HPCNP', 5, 0, info='Percentage of product harvested, %'),
    FloatVar('HPCNR', 5, 0, info='Percentage of residue harvested, %')

}
