High-level interface
====================
The high-level interface simplifies many tasks while working with DSSAT input and output files.

Input files
-----------
Each of these managers creates a more friendly interface to DSSAT files than that of the base input file reader.

Experiment file manager
^^^^^^^^^^^^^^^^^^^^^^^
:class:`~tradssat.mgrs.DSSATRun` allows you to read, edit and write experiments, with automatic access to referenced
external soil, genetic and weather files. TraDSSAT will also automagically manage the link between DSSAT treatments
and associated factor levels (if you don't know what this means, now would be a great time to stop reading this and
read the DSSAT docs instead).

.. code-block:: python

   from tradssat import DSSATRun

   run = DSSATRun('path/to/my/experiment.EXP')

   # Get cultivar for treatment 1
   run.get_trt_val('INGENO', trt=1)

   # Change level of treatment factor
   run.set_trt_factor_level(trt=1, factor='CULTIVARS', level=2)

   # Change value of a factor level (in this case cultivar type)
   run.set_factor_level_val('INGENO', 'IB0067', level=1)

   # Access soil variable SLLL for treatment 2
   run.get_trt_val('SLLL', trt=2)

Genetic file manager
^^^^^^^^^^^^^^^^^^^^
DSSAT's crop modules generally split coefficients between cultivar, ecotype and species files. TraDSSAT provides a
:class:`~tradssat.mgrs.GeneticMgr` class to automagically manage all genetic coefficients for a particular crop
and cultivar type.

.. code-block:: python

   from tradssat import GeneticMgr

   gen = GeneticMgr(crop='MZIXM', cult='PC0001')

   # Returns P1 for MZIXM cultivar PC0001
   gen.get_value('P1')

   # Returns ecotype variable TOPT for cultivar PC001
   gen.get_value('TOPT')

.. note::

   It is currently not possible to access species coefficients with traDSSAT, because these are in practice model
   constants and should not be written or changed (and, if they were, would also by default affect **all future**
   DSSAT simulations run on your DSSAT installation). More practically, they also come in a variety of formats
   and would be a pain to parse.

Soil file manager
^^^^^^^^^^^^^^^^^
Soil files can be hard to manage, since they can contain data for many different soils in the same file. With
:class:`~tradssat.mgrs.SoilMgr`, simply pass the soil code and traDSSAT will find the correct file and file section.

.. code-block:: python

   from tradssat.mgrs import SoilMgr

   soil_mgr = SoilMgr('IB00000005')
   soil_mgr.get_value('SLU1')

Weather file manager
^^^^^^^^^^^^^^^^^^^^
Don't feel like finding your weather file yourself? Just give the station code to
:class:`~tradssat.mgrs.WeatherFileMgr` and let it find it for you.

.. code-block:: python

   from tradssat.mgrs import WeatherFileMgr

   wth_mgr = WeatherFileMgr('ACNM')
   wth_mgr.get_value('RAIN')

Output files
------------
You can access output from a run using a :class:`~tradssat.mgrs.DSSATResults` object instantiated with the output
directory.

.. code-block:: python

   from tradssat import DSSATResults

   out = DSSATResults('path/to/my/output/dir')

   # Get FWAD results for treatment 1 (as a time series)
   out.get_value('FWAD', trt=1)

   # Get results at specific time

    # Get result at 13 days after start
   out.get_value('FWAD', trt=1, t=13, at='DAS')

   # Get result at 13 days after planting
   out.get_value('FWAD', trt=1, t=13, at='DAP')

   # Get result at 123th day of year 1989
   out.get_value('FWAD', trt=1, t='1989 123', at='DOY')
