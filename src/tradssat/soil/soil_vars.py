from tradssat.tmpl.var import CharacterVar, FloatVar

header_vars = [
    CharacterVar('SLSOURCE', 11, spc=2, info='Source'),
    CharacterVar('SLTX', 5, info='Texture, code'),
    FloatVar('SLDP', 5, 0, info='Depth, cm'),
    CharacterVar('SLDESCRIP', 50, info='Description or local classification')
]

main_vars = {
    CharacterVar('SITE', 11, info='Site name'),
    CharacterVar('COUNTRY', 12, info='Country name'),
    FloatVar('LAT', 8, 3, info='Latitude'),
    FloatVar('LONG', 7, 3, info='Longitude'),
    CharacterVar('SCS FAMILY', 50, info='Family, SCS system'),

    CharacterVar('SCOM', 5, info='Color, moist, Munsell hue'),
    FloatVar('SALB', 5, 2, info='Albedo, fraction '),
    FloatVar('SLU1', 5, 1, info='Evaporation limit, cm'),
    FloatVar('SLDR', 5, 2, info='Drainage rate, fraction day-1'),
    FloatVar('SLRO', 5, 1, info='Runoff curve number (Soil Conservation Service)'),
    FloatVar('SLNF', 5, 2, info='Mineralization factor, 0 to 1 scale'),
    FloatVar('SLPF', 5, 2, info='Photosynthesis factor, 0 to 1 scale'),
    CharacterVar('SMHB', 5, info='pH in buffer determination method, code'),
    CharacterVar('SMPX', 5, info='Phosphorus, extractable, determination code'),
    CharacterVar('SMKE', 5, info='Potassium determination method, code'),
    CharacterVar('SGRP', 5, info='Probably soil group'),

    FloatVar('SLB', 5, 0, info='Depth, base of layer, cm'),
    CharacterVar('SLMH', 5, info='Master horizon'),
    FloatVar('SLLL', 5, 3, info='Lower limit, cm3 cm-3'),
    FloatVar('SDUL', 5, 3, info='Upper limit, drained, cm3 cm-3'),
    FloatVar('SSAT', 5, 3, info='Upper limit, saturated, cm3 cm-3'),
    FloatVar('SRGF', 5, 3, info='Root growth factor, 0.0 to 1.0 '),
    FloatVar('SSKS', 5, 3, info='Sat. hydraulic conductivity, macropore, cm h-1'),
    FloatVar('SBDM', 5, 2, info='Bulk density, moist, g cm-3'),
    FloatVar('SLOC', 5, 3, info='Organic carbon, %'),
    FloatVar('SLCL', 5, 1, info='Clay (<0.002 mm), %'),
    FloatVar('SLSI', 5, 1, info='Silt (0.05 to 0.002 mm), %'),
    FloatVar('SLCF', 5, 1, info='Coarse fraction (>2 mm), %'),
    FloatVar('SLNI', 5, 3, info='Total nitrogen, %'),
    FloatVar('SLHW', 5, 1, info='pH in water'),
    FloatVar('SLHB', 5, 2, info='pH in buffer'),
    FloatVar('SCEC', 5, 1, info='Cation exchange capacity, cmol kg-1'),
    FloatVar('SADC', 5, 1, info=''),

    FloatVar('SLPX', 5, 1, info='Phosphorus, extractable, mg kg-1'),
    FloatVar('SLPT', 5, 1, info='Phosphorus, total, mg kg-1'),
    FloatVar('SLPO', 5, 1, info='Phosphorus, total, mg kg-1'),
    FloatVar('CACO3', 5, 1, info='CaCO3 content, g kg-1'),
    FloatVar('SLAL', 5, 1, info='Aluminum'),
    FloatVar('SLFE', 5, 1, info='Iron'),
    FloatVar('SLMN', 5, 1, info='Manganese'),
    FloatVar('SLBS', 5, 1, info='Base saturation, cmol kg-1'),
    FloatVar('SLPA', 5, 1, info='Phosphorus isotherm A, mmol kg-1'),
    FloatVar('SLPB', 5, 1, info='Phosphorus iostherm B, mmol kg-1'),
    FloatVar('SLKE', 5, 1, info='Potassium, exchangeable, cmol kg-1'),
    FloatVar('SLMG', 5, 1, info='Magnesium, cmol kg-1'),
    FloatVar('SLNA', 5, 1, info='Sodium, cmol kg-1'),
    FloatVar('SLSU', 5, 1, info='Sulfur'),
    FloatVar('SLEC', 5, 1, info='Electric conductivity, seimen'),
    FloatVar('SLCA', 5, 1, info='Ca level?'),

    FloatVar('ALFVG', 5, 3, info='Who knows?'),
    FloatVar('MVG', 5, 3),
    FloatVar('NVG', 5, 3),
    FloatVar('WCRES', 5, 3)

}
