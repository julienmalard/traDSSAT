Output files
============
Output files can only be read from, not written to. The following classes are available:

* ``PlantGroOut`` (PlantGro.OUT)
* ``SoilNiOut`` (SoilNi.OUT)
* ``SoilTempOut`` (SoilTemp.OUT)
* ``SummaryOut`` (Summary.OUT)

These classes can all be used to read the corresponding output file. Note that it is generally more straightforward
and pleasant to use a :class:`~tradssat.mgrs.DSSATResults` object instead of accessing individual output files
directly.

.. code-block:: python

   from tradssat.out import PlantGroOut

   plant = PlantGroOut('path/to/my/PlantGro.OUT')

   # Get Leaf Area Index time series
   plant.get_value('LAID')
