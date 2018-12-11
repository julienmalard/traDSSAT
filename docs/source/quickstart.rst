Quick start
===========

Installation
------------
traDSSAT requires ``numpy`` and ``chardet`` to run. You can install it from pip with:
   :command:`pip install tradssat`

You can also install the most cutting-edge version directly from GitHub with:
   :command:`pip install git+git://github.com/julienmalard/tradssat.git@master`

You will need a local installation of DSSAT to use the high-level interface's automatic file managers (since these
will need to find soil, weather, and other files in the DSSAT installation directory). TraDSSAT should find your
DSSAT installation by itself, but if it needs help you can specify it with:

.. code-block:: python

   from tradssat import set_dssat_dir
   set_dssat_dir('C:/My/odd/path/to/DSSAT47')

A quick example
---------------

.. code-block:: python

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
   gen.get_value('TOPT')  # Returns ecotype variable TOPT for cultivar PC001
