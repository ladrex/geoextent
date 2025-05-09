
Command-Line Interface (CLI)
============================

Basics
------

``geoextent`` can be called on the command line with this command :
   
.. autoprogram:: geoextent.__main__:arg_parser
   :prog: \

Examples
--------

.. note::
   Depending on the local configuration, **geoextent** might need to be called with the python interpreter prepended:
   
   `python -m geoextent ...`

Show help message
^^^^^^^^^^^^^^^^^

::

   geoextent -h

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.__main__ as geoextent
   geoextent.print_help()

Extract bounding box from a single file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   You can find the file used in the examples of this section from `muenster_ring_zeit <https://raw.githubusercontent.com/o2r-project/geoextent/master/tests/testdata/geojson/muenster_ring_zeit.geojson>`_. Furthermore, for displaying the rendering of the file contents, see `rendered blob <https://github.com/o2r-project/geoextent/blob/master/tests/testdata/geojson/muenster_ring_zeit.geojson>`_.

::

   geoextent -b muenster_ring_zeit.geojson

Output:

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.lib.extent as geoextent
   geoextent.fromFile('../tests/testdata/geojson/muenster_ring_zeit.geojson', True, False)

Extract time interval from a single file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   You can find the file used in the examples of this section from `muenster_ring_zeit <https://raw.githubusercontent.com/o2r-project/geoextent/master/tests/testdata/geojson/muenster_ring_zeit.geojson>`_. Furthermore, for displaying the rendering of the file contents, see `rendered blob <https://github.com/o2r-project/geoextent/blob/master/tests/testdata/geojson/muenster_ring_zeit.geojson>`_.

::

   geoextent -t muenster_ring_zeit.geojson

Output:

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.lib.extent as geoextent
   geoextent.fromFile('../tests/testdata/geojson/muenster_ring_zeit.geojson', False, True)

Extract both bounding box and time interval from a single file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
   You can find the file used in the examples of this section from `muenster_ring_zeit <https://raw.githubusercontent.com/o2r-project/geoextent/master/tests/testdata/geojson/muenster_ring_zeit.geojson>`_. Furthermore, for displaying the rendering of the file contents, see `rendered blob <https://github.com/o2r-project/geoextent/blob/master/tests/testdata/geojson/muenster_ring_zeit.geojson>`_.

::

   geoextent -b -t muenster_ring_zeit.geojson

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.lib.extent as geoextent
   geoextent.fromFile('../tests/testdata/geojson/muenster_ring_zeit.geojson', True, True)

Folders or ZIP files(s)
-----------------------

Geoextent also supports queries for multiple files inside **folders** or **ZIP file(s)**. 

Extract both bounding box and time interval from a folder or zipfile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   geoextent -b -t folder_two_files

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.lib.extent as geoextent
   geoextent.fromDirectory('../tests/testdata/folders/folder_two_files', True, True)

The output of this function is the combined bbox or tbox resulting from merging all results of individual files (see: :doc:`../supportedformats/index_supportedformats`) inside the folder or zipfile. The resulting coordinate reference system  ``CRS`` of the combined bbox is always in the `EPSG: 4326 <https://epsg.io/4326>`_ system.


Zenodo repositories
-----------------------

Geoextent also supports queries from (Open) Zenodo repositories.

Extract both bounding box and time interval from Zenodo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

   geoextent -b -t https://zenodo.org/record/820562

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.lib.extent as geoextent
   geoextent.from_repository('https://zenodo.org/record/820562', True, True)

The output of this function is the combined bbox or tbox resulting from merging all results of individual files (see: :doc:`../supportedformats/index_supportedformats`) inside the Zenodo repository. The resulting coordinate reference system  ``CRS`` of the combined bbox is always in the `EPSG: 4326 <https://epsg.io/4326>`_ system.

Debugging
^^^^^^^^^

You can enable detailed logs by passing the ``--debug`` option, or by setting the environment variable ``GEOEXTENT_DEBUG=1``.

::

   geoextent --debug -b -t muenster_ring_zeit.geojson

   GEOEXTENT_DEBUG=1 geoextent -b -t muenster_ring_zeit.geojson

Details
^^^^^^^
You can enable details for folders and ZIP files by passing the ``--details`` option, this option allows you to access
to the geoextent of the individual files inside the folders/ ZIP files used to compute the aggregated bounding box (bbox)
or time box (tbox).

::

   geoextent --details -b -t folder_one_file

.. jupyter-execute::
   :hide-code:
   :stderr:

   import geoextent.lib.extent as geoextent
   geoextent.fromDirectory('../tests/testdata/folders/folder_one_file', True, True,True)

Export function
^^^^^^^^^^^^^^^
You can export the result of Geoextent to a Geopackage file. This file contains the output of all files within the
folder or repository.

::

    geoextent -b -t --output path/to/output/geopackage_file.gpkg folder_path



