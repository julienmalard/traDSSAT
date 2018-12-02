from tradssat.tmpl.var import CharacterVar, FloatVar
from ._utils import _return_vars

_standard_cul_vars = {
    'VAR#': {
        'class': CharacterVar,
        'args': dict(size=6, spc=0, info='Identification code or number for the specific cultivar.')
    },
    'VRNAME': {'class': CharacterVar, 'args': dict(size=16, header_fill='.', info='Name of cultivar.')},
    'EXPNO': {
        'class': CharacterVar, 'args': dict(size=5, miss='.', info='Number of experiments used for calibration.')
    },  # Yes, I know. Number of experiments is a character var.
    'ECO#': {'class': CharacterVar,
             'args': dict(size=6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)')},
    'CSDL': {'class': FloatVar,
             'args': dict(
                 size=5, dec=2,
                 info='Critical Short Day Length below which reproductive development progresses with no daylength '
                      'effect (for shortday plants) (hour)')
             },
    'PPSEN': {'class': FloatVar,
              'args': dict(
                  size=5, dec=4,
                  info='Slope of the relative response of development to photoperiod with time '
                       '(positive for shortday plants) (1/hour)')
              },
    'EM-FL': {'class': FloatVar,
              'args': dict(size=5, dec=2,
                           info='Time between plant emergence and flower appearance (R1) (photothermal days)')
              },
    'FL-SH': {'class': FloatVar,
              'args': dict(size=5, dec=2, info='Time between first flower and first pod (R3) (photothermal days)')},
    'FL-SD': {'class': FloatVar,
              'args': dict(size=5, dec=2, info='Time between first flower and first seed (R5) (photothermal days)')},
    'SD-PM': {'class': FloatVar,
              'args': dict(size=5, dec=2,
                           info='Time between first seed (R5) and physiological maturity (R7) (photothermal days)')
              },
    'FL-LF': {'class': FloatVar,
              'args': dict(size=5, dec=2,
                           info='Time between first flower (R1) and end of leaf expansion (photothermal days)')},
    'LFMAX': {'class': FloatVar,
              'args': dict(size=5, dec=3,
                           info='Maximum leaf photosynthesis rate at 30 C, 350 vpm CO2, and high light (mg CO2/m2-s)')},
    'SLAVR': {'class': FloatVar,
              'args': dict(size=5, dec=1,
                           info='Specific leaf area of cultivar under standard growth conditions (cm2/g)')},
    'SIZLF': {'class': FloatVar,
              'args': dict(size=5, dec=2, info='Maximum size of full leaf (three leaflets) (cm2)')},
    'XFRT': {'class': FloatVar,
             'args': dict(size=5, dec=2, info='Maximum fraction of daily growth that is partitioned to seed + shell')},
    'WTPSD': {'class': FloatVar,
              'args': dict(size=5, dec=4, info='Maximum weight per seed (g)')},
    'SFDUR': {'class': FloatVar,
              'args': dict(
                  size=5, dec=2,
                  info='Seed filling duration for pod cohort at standard growth conditions (photothermal days)')},
    'SDPDV': {'class': FloatVar,
              'args': dict(size=5, dec=2, info='Average seed per pod under standard growing conditions (#/pod)')},
    'PODUR': {'class': FloatVar,
              'args': dict(
                  size=5, dec=1,
                  info='Time required for cultivar to reach final pod load under optimal conditions (photothermal days)'
              )},
    'THRSH': {'class': FloatVar,
              'args': dict(size=5, dec=1,
                           info='The maximum ratio of (seed/(seed+shell)) at maturity. '
                                'Causes seed to stop growing as their dry weights '
                                'increase until shells are filled in a cohort. '
                                '(Threshing percentage).'
                           )},
    'SDPRO': {'class': FloatVar, 'args': dict(size=5, dec=3, info='Fraction protein in seeds (g(protein)/g(seed))')},
    'SDLIP': {'class': FloatVar, 'args': dict(size=5, dec=3, info='Fraction oil in seeds (g(oil)/g(seed))')}
}

_standard_eco_vars = {
    'ECO#': {'class': CharacterVar,
             'args': dict(size=6, spc=0, info='Code for the ecotype to which a cultivar belongs (see *.cul')
             },
    'ECONAME': {'class': CharacterVar,

                'args': dict(size=17, header_fill='.',
                             info='Name of the ecotype, which is referenced from *.CUL file')},
    'MG': {'class': CharacterVar,
           'args': dict(size=2, info='Maturity group number for this ecotype, such as maturity group in soybean')},
    'TM': {'class': CharacterVar, 'args': dict(size=2, info='Indicator of temperature adaptation')},
    'THVAR': {'class': FloatVar,
              'args': dict(size=5, dec=1,
                           info='Minimum rate of reproductive development under short days and optimal temperature')},
    'PP-SS': {'class': FloatVar, 'args': dict(size=5, dec=2, info='')},
    'PL-EM': {'class': FloatVar,
              'args': dict(size=5, dec=2, info='Time between planting and emergence (V0) (thermal days)')},
    'EM-V1': {'class': FloatVar,
              'args': dict(
                  size=5, dec=1,
                  info='Time required from emergence to first true leaf (V1), thermal days')},
    'V1-JU': {'class': FloatVar,
              'args': dict(size=5, dec=1,
                           info='Time required from first true leaf to end of juvenile phase, thermal days')},
    'JU-R0': {'class': FloatVar,
              'args': dict(
                  size=5, dec=1,
                  info='Time required for floral induction, equal to the minimum number of days for floral induction '
                       'under optimal temperature and daylengths, photothermal days')},
    'PM06': {'class': FloatVar,
             'args': dict(
                 size=5, dec=2,
                 info='Proportion of time between first flower and first pod for first peg (peanut only)')},
    'PM09': {'class': FloatVar,
             'args': dict(
                 size=5, dec=2,
                 info='Proportion of time between first seed and physiological maturity that the last seed can be '
                      'formed')},
    'LNGSH': {'class': FloatVar,
              'args': dict(
                  size=5, dec=1,
                  info='Time required for growth of individual shells (photothermal days)')},
    'R7-R8': {'class': FloatVar,
              'args': dict(
                  size=5, dec=2,
                  info='Time between physiological (R7) and harvest maturity (R8) (days)')},
    'FL-VS': {'class': FloatVar,
              'args': dict(
                  size=5, dec=2,
                  info='Time from first flower to last leaf on main stem (photothermal days)')},
    'TRIFL': {'class': FloatVar,
              'args': dict(
                  size=5, dec=2,
                  info='Rate of appearance of leaves on the mainstem (leaves per thermal day)')},
    'RWDTH': {'class': FloatVar,
              'args': dict(
                  size=5, dec=2,
                  info='Relative width of this ecotype in comparison to the standard width per node (YVSWH) defined '
                       'in the species file (*.SPE)')},
    'RHGHT': {'class': FloatVar,
              'args': dict(
                  size=5, dec=2,
                  info='Relative height of this ecotype in comparison to the standard height per node (YVSHT) defined '
                       'in the species file (*.SPE)')},
    'SIZELF': {'class': FloatVar,
               'args': dict(
                   size=5, dec=2,
                   info='The size of a normal upper node leaf (nodes 8 - 10) of variety I, used to adjust leaf area '
                        'expansion during sink-limited phase of vegetative growth, i.e., prior to VSSINK nodes on the '
                        'main stem (cm2/leaf)')},
    'R1PPO': {'class': FloatVar,
              'args': dict(
                  size=5, dec=3,
                  info='Increase in daylength sensitivity after R1 (CSDVAR and CLDVAR both decrease with the same '
                       'amount) (h)')},
    'OPTBI': {'class': FloatVar,
              'args': dict(
                  size=5, dec=1,
                  info='Minimum daily temperature above which there is no effect on slowing normal development toward '
                       'flowering (oC)')},
    'SLOBI': {'class': FloatVar,
              'args': dict(
                  size=5, dec=3,
                  info='Slope of relationship reducing progress toward flowering if TMIN for the day is less than '
                       'OPTBI')}
}

_std_frm_eco_vars = {
    'RDRMT': {
        'class': FloatVar,
        'args': dict(size=5, dec=3,
                     info='Relative dormancy sensitivity of this cultivar to daylength - partitioning (0-1)')
    },
    'RDRMG': {
        'class': FloatVar,
        'args': dict(size=5, dec=3,
                     info='Relative dormancy sensitivity of this cultivar to daylength - photosynthesis (0-1)')
    },
    'RDRMM': {
        'class': FloatVar,
        'args': dict(size=5, dec=3,
                     info='Relative dormancy sensitivity of this cultivar to daylength - mobilization (0-1)')
    },
    'RCHDP': {'class': FloatVar, 'args': dict(size=5, dec=3, info='Relative cold hardening potential (0-1)')},
}
_std_frm_eco_vars.update(_standard_eco_vars)


def cropgro_cul_vars(var_name='VRNAME', exclude=None):
    if var_name != 'VRNAME':
        rename = {'VRNAME': var_name}
    else:
        rename = None

    return _return_vars(_standard_cul_vars, rename=rename, exclude=exclude)


def cropgro_eco_vars(rename=None, exclude=None):
    return _return_vars(_standard_eco_vars, rename=rename, exclude=exclude)


def frm_eco_vars(rename=None, exclude=None):
    return _return_vars(_std_frm_eco_vars, rename=rename, exclude=exclude)
