# traDSSAT
TraDSSAT is a library to easily read and write DSSAT input and output files.

## Status
[![Build Status](https://travis-ci.org/julienmalard/traDSSAT.svg?branch=master)](https://travis-ci.org/julienmalard/traDSSAT)
[![Coverage Status](https://coveralls.io/repos/github/julienmalard/traDSSAT/badge.svg?branch=master&service=github)](https://coveralls.io/github/julienmalard/traDSSAT?branch=master)

## Installation
`pip install tradssat`

## Examples

Parse and edit any DSSAT file directly:
```python
from tradssat import SoilFile, WTHFile, ExpFile, set_dssat_dir
from tradssat import GeneticMgr, CULFile, ECOFile

# Read, edit and write soil files
soil = SoilFile('path/to/my/file.SOL')

# Read and write weather files as well
wth = WTHFile('path/to/my/WTHR0001.WTH')

# ...and experiment files
exp = ExpFile('path/to/my/experiment.EXP')


# Access genetic coefficients by cultivar file or ecotype file
cul = CULFile('path/to/my/MZIXM.CUL')
eco = ECOFile('path/to/my/MZIXM.ECO')

cul.get_val('P1')  # returns array of all varieties' P1
eco.get_val('TOPT')  # returns array of all ecotypes' TOPT

# ...or automagically!
set_dssat_dir('C:/DSSAT47')
gen = GeneticMgr(crop='MZIXM', cult='PC0001')
gen.get_val('P1')  # Returns P1 for MZIXM cultivar PC0001
gen.get_val('TOPT')  # Returns ecotype variable TOPT for cultivar PC001

```

Read, edit and write experiments, with automatic access to referenced
external soil, genetic and weather files:
```python
from tradssat import DSSATRun

run = DSSATRun('path/to/my/experiment.EXP')


```

Access output from a run:
```python
from tradssat import PlantGrowOut

out = PlantGrowOut('path/to/my/output/dir')
out.get_val('FWAD')

```

## Contributing
Don't forget to add your name to the `AUTHORS.txt` list!

## Licensing
MIT License
