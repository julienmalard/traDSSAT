from .utils import set_dssat_dir, get_dssat_dir
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
