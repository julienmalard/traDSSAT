.. traDSSAT documentation master file, created by
   sphinx-quickstart on Thu Nov 29 19:34:00 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to traDSSAT!
====================
TraDSSAT aims to reinvent the wheel, once and for all, for `DSSAT <https://www.dssat.net>`_ file management. Whether
for preparing input files for automated DSSAT runs or for analysing outputs, traDSSAT's simple Python interface and
modular structure will (we hope!) dramatically simplify your code.

.. code-block:: python

   from tradssat import SoilFile, WTHFile, ExpFile
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
   gen = GeneticMgr(crop='MZIXM', cult='PC0001')
   gen.get_value('P1')  # Returns P1 for MZIXM cultivar PC0001
   gen.get_value('TOPT')  # Returns ecotype variable TOPT for cultivar PC001

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   quickstart
   inputs
   outputs
   high_level
   api/api
   acknow



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
