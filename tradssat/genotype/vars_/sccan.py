from tradssat.tmpl.var import CharacterVar, FloatVar

cul_vars_SCCAN = {
    CharacterVar('VAR#', 6, spc=0, info='Identification code or number for the specific cultivar.'),
    CharacterVar('VAR-NAME', 16, header_fill='.', info='Name of cultivar.'),
    CharacterVar('EXPNO', 5, miss='.', info='Number of experiments used for calibration.'),
    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),

    FloatVar(
        'MaxPARCE', 14, 2,
        info='Maximum (no stress) radiation conversion efficiency expressed as assimilate produced before respiration, '
             'per unit PAR. (g/MJ).'
    ),
    FloatVar('APFMX', 14, 2,
             info='Maximum fraction of dry mass increments that can be allocated to aerial dry mass (t/t)'),
    FloatVar(
        'PCB', 14, 2,
        info='Partitioning coefficient: extinction coefficient of fraction of dry mass increments allocated to above '
             'ground biomass'
    ),
    FloatVar(
        'STKPFMAX', 14, 2,
        info='Fraction of daily aerial dry mass increments partitioned to stalk at high temperatures in a mature crop '
             '(t/t on a dry mass basis)'
    ),
    FloatVar(
        'DELTTMAX', 14, 2,
        info='Max. change in sucrose content per unit change in stalk mass in the unripenened section of the stalk (/t)'
    ),
    FloatVar('SUCA', 14, 2, info='Sucrose partitioning parameter: Maximum sucrose contents in the base of stalk (t/t)'),
    FloatVar(
        'TBFT', 14, 0,
        info='Sucrose partitioning:  Temperature at which partitioning of unstressed stalk mass increments to sucrose '
             'is 50% of the maximum value'
    ),
    FloatVar('Tthalfo', 14, 0, info='Thermal time to half canopy (oCd)'),
    FloatVar('TBase', 14, 0, info='Base temperature for canopy development (oCd)'),
    FloatVar(
        'LFMAX', 14, 0,
        info='Maximum number of green leaves a healthy, adequately-watered plant will have after it is old enough to '
             'lose some leaves.'
    ),
    FloatVar('MXLFAREA', 14, 0, info='Max leaf area assigned to all leaves above leaf number MXLFARNO (cm2)'),
    FloatVar('MXLFARNO', 14, 0, info='Leaf number above which leaf area is limited to MXLFAREA'),
    FloatVar('PI1', 14, 0, info='Phyllocron interval 1 (for leaf numbers below Pswitch, oC.d (base TTBASELFEX))'),
    FloatVar('PI2', 14, 0, info='Phyllocron interval 2 (for leaf numbers above Pswitch, oC.d (base TTBASELFEX))'),
    FloatVar('PSWITCH', 14, 0, info='Leaf number at which the phyllocron changes.'),
    FloatVar('MAX_POP', 14, 0, info='Maximum tiller population (stalks/m2)'),
    FloatVar('POPTT16', 14, 1, info='Stalk population at/after 1600 degree days (/m2)'),
    FloatVar('TTPLNTEM', 14, 0, info='Thermal time to emergence for a plant crop (degree C days, base TTBASEEM)'),
    FloatVar('TTRATNEM', 14, 0, info='Thermal time to emergence for a ratoon crop (degree C days, base TTBASEEM)'),
    FloatVar('CHUPIBASE', 14, 0, info='Thermal time (base TTBASEEM) from emergence to start of stalk growth'),
    FloatVar('TT_POPGROWTH', 14, 1, info='Thermal time to peak tiller population (deg C days, TTBASEPOP)'),
    FloatVar(
        'LG_AMBASE', 14, 0,
        info='Aerial mass (fresh mass of stalks, leaves, and water attached to them) at which lodging starts; t/ha'
    ),
}

eco_vars_SCCAN = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECO-NAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),

    FloatVar(
        'DELTTMAX', 14, 2,
        info='Max. change in sucrose content per unit change in stalk mass in the unripenened section'
    ),
    FloatVar('SWDF2AMP', 14, 1, info='Sucrose partitioning sensitivity to water stress parameter'),
    FloatVar('CS_CNREDUC', 14, 1, info='Canopy reduction due to water stress'),
    FloatVar('CS_CNPERIOD', 14, 0, info='Canopy water stress period (days)'),
    FloatVar('Tthalfa', 14, 0, info='Half canopy thermal time adjustment for row width'),
    FloatVar('dPERdT', 14, 3, info='Change in plant extension rate (mm/h) per unit change in temperature (oC)'),
    FloatVar('EXTCFN', 14, 2, info='Maximum canopy light extinction coefficient'),
    FloatVar('EXTCFST', 14, 2, info='Minimum canopy light extinction coefficient'),
    FloatVar(
        'LFNMXEXT', 14, 0,
        info='Leaf number (including dead leaves still attached) at which maximum light extinction occurs'
    ),
    FloatVar('AREAMX_CF(1)', 14, 0, info='Cultivar parameter for quadratic equation defining maximum leaf area'),
    FloatVar('AREAMX_CF(2)', 14, 1, info='Cultivar parameter for quadratic equation defining maximum leaf area'),
    FloatVar('AREAMX_CF(3)', 14, 1, info='Cultivar parameter for quadratic equation defining maximum leaf area'),
    FloatVar('WIDCOR', 14, 0, info='Parameter affecting the width of leaves'),
    FloatVar('WMAX_CF(1)', 14, 4, info='Cultivar parameter for quadratic equation defining leaf width'),
    FloatVar('WMAX_CF(2)', 14, 3, info='Cultivar parameter for quadratic equation defining leaf width'),
    FloatVar('WMAX_CF(3)', 14, 2, info='Cultivar parameter for quadratic equation defining leaf width'),
    FloatVar(
        'POPCF(1)', 14, 3,
        info='Stalk population coefficient, in ideal conditions (no stresses), as function of th.time'
    ),
    FloatVar(
        'POPCF(2)', 14, 5,
        info='Stalk population coefficient, in ideal conditions (no stresses), as function of th.time'
    ),
    FloatVar(
        'POPDECAY', 14, 3,
        info='Tiller senescence rate expressed as the fraction of tillers above the future mature tiller population '
             '(at a thermal time of 1600 oC Adjust by comparing simulated and observed tiller population. Varies from '
             '3.0 to 5.0'
    ),
    FloatVar('TTBASEEM', 14, 1, info='Base temperature for emergence (oC)'),
    FloatVar('TTBASELFEX', 14, 1, info='Base temperature for leaf phenology (oC)'),
    FloatVar('TTBASEPOP', 14, 1, info='Base temperature for stalk phenology (oC)'),
    FloatVar('TBASEPER', 14, 3, info='Base temperature for plant extension (oC)'),
    FloatVar('LG_AMRANGE', 14, 0, info='Range in aerial mass from the start to the end of lodging (t/ha)'),
    FloatVar('LG_GP_REDUC', 14, 2,
             info='Reduction in gross photosynthesis due to full lodging, as a fraction (Singh, et al.)'),
    FloatVar('LDG_FI_REDUC', 14, 1, info='Reduction in fractional interception by the canopy due to full lodging'),
    FloatVar('LMAX_CF(1)', 14, 3),
    FloatVar('LMAX_CF(2)', 14, 1),
    FloatVar('LMAX_CF(3)', 14, 1),
    FloatVar('MAXLFLENGTH', 14, 0),
    FloatVar('MAXLFWIDTH', 14, 1)
}
