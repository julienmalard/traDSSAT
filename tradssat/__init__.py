import os

from .utils import set_dssat_dir, get_dssat_dir, read_txt
from .exper import ExpFile
from .genotype import CULFile, ECOFile
from .out import PlantGroOut, SummaryOut, SoilNiOut, SoilTempOut, SoilWatOut, ETOut
from .soil import SoilFile
from .weather import WTHFile, MTHFile, CLIFile
from .mgrs import DSSATRun, DSSATResults, GeneticMgr, WeatherFileMgr, SoilMgr

try:
    set_dssat_dir('C:/DSSAT47')
except FileNotFoundError:
    pass

_base_dir = os.path.split(__file__)[0]
__version__ = read_txt(os.path.join(_base_dir, 'version.txt'))
__authors__ = read_txt(os.path.join(_base_dir, 'AUTHORS.txt'))
