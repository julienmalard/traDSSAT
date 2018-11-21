config = {'DSSAT_DIR': 'C:/DSSAT47'}


def set_dssat_dir(dssat_dir):
    config['DSSAT_DIR'] = dssat_dir


from .exper import ExpFile
from .genotype import CULFile, ECOFile
from .out import PlantGrowOut
from .soil import SoilFile
from .weather import WTHFile
from .runs import DSSATRun, GeneticMgr
