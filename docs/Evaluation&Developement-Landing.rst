.. _Evaluation&Dev:

Evaluation & Developement
=========================

BDWS is hosted on github and publically available at https://github.com/konradhafen/beaver-dam-water-storage.
The entire repository can be cloned to your machine directly from github, downloaded as a compressed folder,
or individual files can be downloaded. Repository directories and files are described below.

docs/
    contains the pages for this documentation website
sphinx/
    contains the source code for building documentation website pages with the :code:`sphinx` module
tutorials/
    contains data for use in the BDWS tutorials
bdws.py
    source code for the :code:`BDLoG` and :code:`BDSWEA` classes
bdflopy.py
    source code for the :code:`BDflopy` class
run.py
    example script for usage of BDWS

:code:`BDflopy` code is in a separate file because it requires use of MODFLOW-2005 and the :code:`flopy` module.
Some users may wish to use :code:`BDLoG` and/or :code:`BDSWEA` without :code:`BDflopy`.

To clone the github repository, enter the following from a terminal.

.. code:: shell

   $ cd /path/to/project
   $ git clone https://github.com/konradhafen/beaver-dam-water-storage

This will create a new directory containing everything in the repository at the location:
::
    /path/to/project/beaver-dam-water-storage

Operating systems
-----------------

The BDWS python code is cross platform (Windows, Mac, Linux), and code for the :code:`BDLoG` and :code:`BDSWEA` packages has been
tested on Windows (10) and Ubuntu (16.04) operating systems.
However, for use of the :code:`BDflopy` class Microsoft Windows is recommended as the USGS only provides compiled MODFLOW-2005
executables for this platform. USGS does provide source code that can be compiled on Unix platforms.
Code for the :code:`BDflopy` class is cross platform but has only been tested on Windows.

Dependencies
------------

1. Python version 2.7.x is recommended.
2. Python modules: :code:`gdal` :code:`numpy` :code:`flopy`
3. Executable programs: :code:`MODFLOW-2005`

Installing python
-----------------

Python can be installed from a number of sources, including https://www.python.org/downloads/. Anaconda is another option which
provides additional tools for python https://www.anaconda.com/download/. This is a recommended option for novice users.
Python version 2.7.x is recommended.

Installing modules
------------------

Python modules can be installed with :code:`pip`.

1. Make sure :code:`pip` is up-to-date. From a terminal or the Anaconda command prompt enter the following.
::
    >>> pip install --upgrade pip

2. Install any dependencies as follows.
::
    >>> pip install gdal


Full documentation for module dependencies can be found at the following sources.

- gdal http://gdal.org/python/
- numpy https://docs.scipy.org/doc/
- flopy https://modflowpy.github.io/flopydoc

Only the :code:`BDflopy` class depends on the :code:`flopy` module

Installing MODFLOW-2005
-----------------------

MODFLOW-2005 executables and documentation can be found at https://water.usgs.gov/ogw/modflow/mf2005.html. Download and
unpack the .zip file for your operating system. Unix users will need to compile the source code.