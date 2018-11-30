import os

from .utils import set_dssat_dir, get_dssat_dir, read_txt
from .exper import ExpFile
from .genotype import CULFile, ECOFile
from .out import PlantGrowOut
from .soil import SoilFile
from .weather import WTHFile
from .runs import DSSATRun, DSSATResults, GeneticMgr, WeatherFileMgr, SoilMgr

try:
    set_dssat_dir('C:/DSSAT47')
except FileNotFoundError:
    pass
__authors__ = read_txt(os.path.join(os.path.split(os.path.split(__file__)[0])[0], 'AUTHORS.txt'))