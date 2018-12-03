from tradssat.tmpl.var import CharacterVar, FloatVar
from ._utils import _return_vars

_standard_cul_vars = {
    'VAR#': {
        'class': CharacterVar,
        'args': dict(size=6, spc=0, info='Identification code or number for the specific cultivar.')
    },
    'VAR-NAME': {
        'class': CharacterVar,
        'args': dict(size=16, header_fill='.', info='Name of cultivar.')
    },
    'EXP#': {
        'class': CharacterVar,
        'args': dict(size=5, miss='.', info='Number of experiments,treatments used to estimate coefficients.')
    },
    'ECO#': {
        'class': CharacterVar,
        'args': dict(size=6, info='Code for the ecotype to which this cultivar belongs (see *.eco file)')
    },
    'G#WTS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Standard grain number per unit canopy weight at anthesis (#/g)')
    },
    'GWTS': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Standard grain size,optimum conditions,normal plant density (mg)')
    },
    'LA1S': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Area of standard first leaf (cm2)')
    },
    'LAFV': {
        'class': FloatVar,
        'args': dict(size=5, dec=2, info='Increase in potential area of leaves,vegetative phase (fr/leaf)')
    },
    'LAFR': {
        'class': FloatVar,
        'args': dict(size=5, dec=2, info='Increase in potential area of leaves,reproductive phase (fr/leaf)')
    },
    'P1': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Duration of phase number 1 (PVoC.D)')
    },
    'P2': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Duration of phase number 2 (PVoC.D)')
    },
    'P3': {
        'class': FloatVar,
        'args': dict(
            size=5, dec=0,
            info='Duration of phase number 3 (PVoC.D) BUT P3 and P4 are \'dummy\' values inserted to set the total '
                 'duration of the P3+P4 phase. The actual balance between P3 and P4 is determined internally depending '
                 'on the leaf number at the end of phase 1.'
        )
    },
    'P4': {
        'class': FloatVar,
        'args': dict(
            size=5, dec=0,
            info='Duration of phase number 4 (PVoC.D) BUT P3 and P4 are \'dummy\' values inserted to set the total '
                 'duration of the P3+P4 phase. The actual balance between P3 and P4 is determined internally depending '
                 'othe leaf number at the end of phase 1.'
        )
    },
    'P5': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Duration of phase number 5 (PVoC.D)')
    },
    'P6': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Duration of phase number 6 (PVoC.D)')
    },
    'P7': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Duration of phase number 7 (PVoC.D)')
    },
    'P8': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Duration of phase number 8 (PVoC.D)')
    },
    'PPS1': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Photoperiod sensitivity,phase(1). % drop in rate,10h pp.change.')
    },
    'PPS2': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Photoperiod sensitivity,phase(2). % drop in rate,10h pp.change.')
    },
    'PHINT': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Interval between successive leaf appearances. (oC.d)')
    },
    'SHWTS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Standard,non-stressed shoot dry weight (incl.grain),maturity (g)')
    },
    'SLAS': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Specific leaf area,standard (cm2/g)')
    },
    'VREQ': {
        'class': FloatVar,
        'args': dict(size=5, dec=4, info='Vernalization required for max.development rate (VDays)')
    },
    'VBASE': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Vernalization requirement before any effect (VDays)')
    },
    'VEFF': {
        'class': FloatVar,
        'args': dict(size=5, dec=2, info='Vernalization effect (Rate reduction when unvernalized (fr)')
    },

}
_standard_eco_vars = {
    'ECO#': {
        'class': CharacterVar,
        'args': dict(size=6, spc=0, info='Ecotype code (text)')
    },
    'ECONAME': {
        'class': CharacterVar,
        'args': dict(size=17, header_fill='.', info='Ecotype name')
    },
    'AWNS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Awn score (0-10; 10=very long)')
    },
    'G#RF': {
        'class': FloatVar,
        'args': dict(size=5, dec=3, info='Grain number radiation factor (fr increase/(MJ/m2.d) radiation in phase 5)')
    },
    'GM%H': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Grain moisture percentage at harvest (%)')
    },
    'GN%MN': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Minimum grain nitrogen (%)')
    },
    'GN%S': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Standard grain nitrogen concentration (%)')
    },
    'GWTAF': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Grain weight adjustment factor (fr/10000kg/ha canopy wt>threshold)')
    },
    'GWTAT': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Grain weight adjustment threshold (kg/ha canopy weight at anthesis)')
    },
    'HTSTD': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Standard canopy height (cm)')
    },
    'KCAN': {
        'class': FloatVar,
        'args': dict(size=5, dec=2, info='PAR extinction coefficient (#)')
    },
    'LSENI': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Leaf senescence,intermediate phases (%/standard day)')
    },
    'LSPHE': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Leaf senescence (final) phase end stage (GrowthStage)')
    },
    'LSPHS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Leaf senescence (final) phase start stage (GrowthStage)')
    },
    'NUPNF': {
        'class': FloatVar,
        'args': dict(size=5, dec=2, info='NO3 uptake vs conc exponent adjustment factor (0-2;0=no uptake,1=standard)')
    },
    'NUPWF': {
        'class': FloatVar,
        'args': dict(
            size=5, dec=1, info='Soil water effect on N uptake adjustment factor (0-2;1.0=no effect,1=standard)'
        )
    },
    'PARU2': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='PAR conversion factor,after change (g dry matter/MJ)')
    },
    'PARUE': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='PAR conversion factor,standard (g dry matter/MJ)')
    },
    'PHF3': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Factor by which PHINTS multiplied -> PHINT for particular phase (#)')
    },
    'PHL2': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Leaf # at end of phyllochron phase (ie,at which PHINT changes) (#)')
    },
    'RDGS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Root depth growth rate,standard (cm/standard day)')
    },
    'RS%A': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Reserves concentration in tops at start of anthesis (%)')
    },
    'RTNUP': {
        'class': FloatVar,
        'args': dict(size=5, dec=3, info='NO3 uptake/root length  (mg N/cm.day)')
    },
    'SLAS': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Specific leaf area,standard (cm2/g)')
    },
    'SSPHE': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Stem senescence (final) phase end stage (GrowthStage)')
    },
    'SSPHS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Stem senescence (final) phase start stage (GrowthStage)')
    },
    'TDFAC': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Tiller death factor (%/st.day when tiller wt 2xstandard wt)')
    },
    'TDPHE': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Tiller death phase end stage (GrowthStage)')
    },
    'TDPHS': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Tiller death phase start stage (GrowthStage)')
    },
    'TDSF': {
        'class': FloatVar,
        'args': dict(size=5, dec=2, info='Tiller death stress factor (#;0,2->no,full stress acceleration)')
    },
    'TIFAC': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Tiller initiation (rate) factor (fr of phyllochron based) (#)')
    },
    'TIL#S': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Tillering phase (production) start stage (leaf #)')
    },
    'TILPE': {
        'class': FloatVar,
        'args': dict(size=5, dec=1, info='Tillering phase (production) end (GrowthStage)')
    },
    'TKFH': {
        'class': FloatVar,
        'args': dict(size=5, dec=0, info='Cold tolerance when fully hardened (oC)')
    }
}


def cropsim_cul_vars(rename=None, exclude=None):
    return _return_vars(_standard_cul_vars, rename=rename, exclude=exclude)


def cropsim_eco_vars(rename=None, exclude=None):
    return _return_vars(_standard_eco_vars, rename=rename, exclude=exclude)
