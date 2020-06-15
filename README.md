# traDSSAT
TraDSSAT is a library to easily read and write DSSAT input and output files.

## Status
[![Build Status](https://travis-ci.org/julienmalard/traDSSAT.svg?branch=master)](https://travis-ci.org/julienmalard/traDSSAT)
[![codecov](https://codecov.io/gh/julienmalard/traDSSAT/branch/master/graph/badge.svg)](https://codecov.io/gh/julienmalard/traDSSAT)
[![Documentation Status](https://readthedocs.org/projects/tradssat/badge/?version=latest)](https://tradssat.readthedocs.io/en/latest/?badge=latest)

## Installation
`pip install tradssat`

## Full docs
Read the full thing [here](https://tradssat.readthedocs.io/en/latest/).

## Quick examples

Parse and edit any DSSAT file directly:
```python
from tradssat import SoilFile, WTHFile, ExpFile, set_dssat_dir
from tradssat import GeneticMgr, CULFile, ECOFile

# Read, edit and write soil files
soil = SoilFile('path/to/my/file.SOL')

# Read and write weather files as well
wth = WTHFile('path/to/my/WTHR0001.WTH')

# ...and experiment files!
exp = ExpFile('path/to/my/experiment.EXP')


# Access genetic coefficients by cultivar file or ecotype file
cul = CULFile('path/to/my/MZIXM.CUL')
eco = ECOFile('path/to/my/MZIXM.ECO')

cul.get_value('P1')  # returns array of all varieties' P1
eco.get_value('TOPT')  # returns array of all ecotypes' TOPT

# ...or automagically!
set_dssat_dir('C:/DSSAT47')
gen = GeneticMgr(crop='MZIXM', cult='PC0001')
gen.get_value('P1')  # Returns P1 for MZIXM cultivar PC0001
gen.get_value('TOPT')  # Returns ecotype variable TOPT for cultivar PC0001

```

Read, edit and write experiments, with automatic access to referenced
external soil, genetic and weather files:
```python
from tradssat import DSSATRun

run = DSSATRun('path/to/my/experiment.EXP')
run.get_trt_val('INGENO', trt=1)  # Get cultivar for treatment 1
run.set_trt_factor_level(trt=1, factor='CULTIVARS', level=2)  # Change level of treatment factor
run.set_factor_level_val('INGENO', 'IB0067', level=1)  # Change value of a factor level (in this case cultivar type)

```

Access output from a run:
```python
from tradssat import DSSATResults

out = DSSATResults('path/to/my/output/dir')
out.get_value('FWAD', trt=1)

# Get results at specific time (day of year, days after planting or days after start)
out.get_value('FWAD', trt=1, t=13, at='DAS')  # Get result at 13 days after start
out.get_value('FWAD', trt=1, t=13, at='DAP')  # Get result at 13 days after planting
out.get_value('FWAD', trt=1, t='1989 123', at='DOY')  # Get result at 123th day of year 1989

```

## Contributing
Don't forget to add your name to the authors list in the `docs/source/acknow.rst` file!

## Licensing
MIT License
