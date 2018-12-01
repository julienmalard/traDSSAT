from tradssat.tmpl.var import CharacterVar, IntegerVar, FloatVar

miss = '9999'

cul_vars_ALFRM = {
    CharacterVar('VAR#', 6, spc=0, info='Variety (cultivar) code'),
    CharacterVar('VRNAME', 16, header_fill='.', info='Variety (cultivar) name'),
    CharacterVar('EXPNO', 5, miss=miss, info='Number of experiments used to estimate cultivar parameters'),

    CharacterVar('ECO#', 6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)'),
    FloatVar(
        'CSDL', 5, 2, miss=miss,
        info='Critical Short Day Length below which reproductive development progresses with no daylength effect '
             '(for shortday plants) (hour)'
    ),
    FloatVar(
        'PPSEN', 5, 3, miss=miss,
        info='Slope of the relative response of development to photoperiod with time'
             '(positive for shortday plants) (1/hour)'
    ),
    FloatVar('EM-FL', 5, 1, miss=miss,
             info='Time between plant emergence and flower appearance (R1) (photothermal days)'),
    FloatVar('FL-SH', 5, 1, miss=miss, info='Time between first flower and first pod (R3) (photothermal days)'),
    FloatVar('FL-SD', 5, 1, miss=miss, info='Time between first flower and first seed (R5) (photothermal days)'),
    FloatVar('SD-PM', 5, 2, miss=miss,
             info='Time between first seed (R5) and physiological maturity (R7) (photothermal days)'),
    FloatVar('FL-LF', 5, 2, miss=miss,
             info='Time between first flower (R1) and end of leaf expansion (photothermal days)'),
    FloatVar(
        'LFMAX', 5, 2, miss=miss,
        info='Maximum leaf photosynthesis rate at 30 C, 350 vpm CO2, and high light (mg CO2/m2-s)'
             'default was 1.98 - set to 1.76=40 umol m-2 s-1 yielding Boote et al.\'s 35.5 umol m-2s-1 @ '
             '2000 umol photons m-2s-1'
    ),
    FloatVar('SLAVR', 5, 0, miss=miss, info='Specific leaf area of cultivar under standard growth conditions (cm2/g)'),
    FloatVar('SIZLF', 5, 1, miss=miss, info='Maximum size of full leaf (three leaflets) (cm2)'),
    FloatVar('XFRT', 5, 2, miss=miss, info='Maximum fraction of daily growth that is partitioned to seed + shell'),
    FloatVar('WTPSD', 5, 3, miss=miss, info='Maximum weight per seed (g)'),
    FloatVar(
        'SFDUR', 5, 1, miss=miss,
        info='Seed filling duration for pod cohort at standard growth conditions (photothermal days)'
    ),
    FloatVar('SDPDV', 5, 2, miss=miss, info='Average seed per pod under standard growing conditions (#/pod)'),
    FloatVar(
        'PODUR', 5, 1, miss=miss,
        info='Time required for cultivar to reach final pod load under optimal conditions (photothermal days)'
    ),
    FloatVar('THRSH', 5, 1, miss=miss, info=''),
    FloatVar('SDPRO', 5, 3, miss=miss, info=''),
    FloatVar('SDLIP', 5, 3, miss=miss, info=''),
    FloatVar('', 5, 2, miss=miss, info=''),
}

eco_vars_ALFRM = {
    CharacterVar('ECO#', 6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul file)'),
    CharacterVar('ECONAME', 17, header_fill='.', info='Name of the ecotype, which is referenced from *.CUL file'),
    IntegerVar('MG', 2, info='Maturity group number for this ecotype, such as maturity group in soybean'),
    IntegerVar('TM', 2, info='Indicator of temperature adaptation'),
    FloatVar('THVAR', 5, 2, info='Minimum rate of reproductive development under short days and optimal temperature'),
    FloatVar('PL-EM', 5, 1, info='Time between planting and emergence (V0) (thermal days)'),
    FloatVar('EM-V1', 5, 1, info='Time required from emergence to first true leaf (V1), thermal days'),
    FloatVar('V1-JU', 5, 1, info='Time required from first true leaf to end of juvenile phase, thermal days'),
    FloatVar(
        'JU-R0', 5, 1,
        info='Time required for floral induction, equal to the minimum number of days for floral induction under '
             'optimal temperature and daylengths, photothermal days'
    ),
    FloatVar('PM06', 5, 1, info='Proportion of time between first flower and first pod for first peg (peanut only)'),
    FloatVar(
        'PM09', 5, 2,
        info='Proportion of time between first seed and physiological, maturity that the last seed can be formed'
    ),
    FloatVar('LNGSH', 5, 2, info='Time required for growth of individual shells (photothermal days)'),
    FloatVar('R7-R8', 5, 1, info='Time between physiological (R7) and harvest maturity (R8) (days)'),
    FloatVar('FL-VS', 5, 1, info='Time from first flower to last leaf on main stem (photothermal days)'),
    FloatVar(
        'TRIFL', 5, 2,
        info='Rate of appearance of leaves on the mainstem (leaves per thermal day) default was 0.10, not '
             'getting enough leaves, changed to 0.15 2/21/03'
    ),
    FloatVar(
        'RWDTH', 5, 1,
        info='Relative width of this ecotype in comparison to the standard width per node (YVSWH) defined '
             'in the species file (*.SPE)'
    ),
    FloatVar(
        'RHGHT', 5, 1,
        info='Relative height of this ecotype in comparison to the standard height per node (YVSHT) defined in the '
             'species file (*.SPE)'
    ),
    FloatVar(
        'THRSH', 5, 3,
        info='The maximum ratio of (seed/(seed+shell)) at maturity. Causes seed to stop growing as their dry weights'
             'increase until shells are filled in a cohort. (Threshing percentage).'
    ),
    FloatVar('SDPRO', 5, 3, info='Fraction protein in seeds (g(protein)/g(seed))'),
    FloatVar('SDLIP', 5, 3, info='Fraction oil in seeds (g(oil)/g(seed))'),
    FloatVar(
        'R1PPO', 5, 3,
        info='Increase in daylength sensitivity after R1 (CSDVAR and CLDVAR both decrease with the same amount) (h)'
    ),
    FloatVar(
        'OPTBI', 5, 1,
        info='Minimum daily temperature above which there is no effect on slowing normal development toward '
             'flowering (oC)'
    ),
    FloatVar(
        'SLOBI', 5, 3,
        info='Slope of relationship reducing progress toward flowering if TMIN for the day is less than OPTBI'
    ),
    FloatVar('RDRMT', 5, 3, info='Relative dormancy sensitivity of this cultivar to daylength - partitioning (0-1)'),
    FloatVar('RDRMG', 5, 3, info='Relative dormancy sensitivity of this cultivar to daylength - photosynthesis (0-1)'),
    FloatVar('RDRMM', 5, 3, info='Relative dormancy sensitivity of this cultivar to daylength - mobilization (0-1)'),
    FloatVar('RCHDP', 5, 3, info='Relative cold hardening potential (0-1)')

}
