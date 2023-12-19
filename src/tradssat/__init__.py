import os.path

from .exper import ExpFile
from .genotype import CULFile, ECOFile
from .mgrs import DSSATRun, DSSATResults, GeneticMgr, WeatherFileMgr, SoilMgr
from .out import PlantGroOut, SummaryOut, SoilNiOut, SoilTempOut, SoilWatOut, ETOut
from .soil import SoilFile
from .utils import set_dssat_dir, get_dssat_dir, read_txt
from .weather import WTHFile, MTHFile, CLIFile

try:
    set_dssat_dir(os.path.join('C:', 'DSSAT47'))
except FileNotFoundError:
    print("DSSAT root directory was not automatically found. You can set it with `set_dssat_dir('path/to/DSSAT')`.")
    pass
