Input files
===========
TraDSSAT has specific classes to read and edit DSSAT input files. Each class defines its own allowed variables
and variable information. All files have the same general structure:

#. Section (named; header line starts with ``*`` or ``$`` in DSSAT files)
#. Section header variables (optional)
#. Subsection (numbered; header line starts with ``@`` followed by variable names in DSSAT files)
#. Subsection variables

Specific classes used to read DSSAT input files are:

* :class:`~tradssat.SoilFile` (.SOL)
* :class:`~tradssat.WTHFile` (.WTH, .WTG)
* :class:`~tradssat.ExpFile` (.ccX)
* :class:`~tradssat.CULFile` (.CUL)
* :class:`~tradssat.ECOFile` (.ECO)

As all input files inherit from :class:`~tradssat.tmpl.InpFile`, the same interface to reading, editing and writing
holds for all DSSAT input files.

Reading files
-------------
Input files are instantiated with the path to the file to be read.

.. code-block:: python

   from tradssat import WTHFile
   wth = WTHFile('path/to/my/WTHR0001.WTH')

Values of all variables can then be read directly.

.. code-block:: python

   # Get solar radiation data time series
   wth.get_value('SRAD')

   # Conditions can also be set

   # Only get data from 2 Jan, 2013.
   wth.get_value('SRAD', cond={'DATE': '13002'})

   # Only get data from dry days
   wth.get_value('SRAD', cond={'RAIN': 0})

Getting a list of all allowed variable names for the file type is also easy.

.. code-block:: python

   wth.variables()

Editing files
-------------
Variable values can be changed, either for the whole file or for specific sections and/or subsections, as well as by
condition.

.. code-block:: python

   from tradssat import SoilFile
   soil = SoilFile('path/to/my/file.SOL')

   # Set all soils' SALB to 0.15
   soil.set_value('SALB', 0.15)

   # Only set soil IB00000002's SALB to 0.2
   soil.set_value('SALB', 0.20, sect='IB00000002')

   # Increase clay, but only for the first 5 cm of soil IB00000002
   soil.set_value('SLCL', 0.50, sect='IB00000002', cond={'SLB': 5})

You can also add rows to specific subsections of a file, or remove existing rows. Subsection variables not included
in ``vals`` will be set to missing (usually -99).

.. code-block:: python

   # Add new soil layer
   soil.add_row(
       sect='IB00000002', subsect=2, vals={'SLB': 180, 'SLLL': 0.260}
   )

You can save the data to json format, or else write a DSSAT-format file back to disk.

.. code-block:: python

   # Convert to dict...
   json_d = soil.to_dict()

   # ...or save to disk
   wth.write('path/to/my/new/SOIL.SOL')
