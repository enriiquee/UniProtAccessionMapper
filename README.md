UniProt-AccessionMapper
===============

# About UniProt-AccessionMapper

This script allows to map multiples accessions from different databases. 

# Getting UniProt-AccessionMapper

## Installation Requirements

* Python: Python 3.7.* (or above), which you can download for free [here](https://www.python.org/downloads/). (Note: most computers should have Python installed already).
* Operating System: The current version has been tested on Windows 7, Windows Vista, Linux and Max OS X, it should also work on other platforms. If you come across any problems on your platform, please contact me.
* Memory: Accessions files can be very large sometimes, in order to get good performance from AccessionMapper, we recommend you to have 4G of free memory.

## Launch via

To start the script, simply run from Windows/Linux/Mac terminal. Select the path of your accession file and run it. 





If this fails, try to download and install Java 1.7 or above, as explained in the previous section. (The program can also be started from the command line using the following command: java -jar pride-inspector-X.Y.jar.)

The zip file contains also an examples folder with 2 sample files: one in mzML format (mzml-example.mzML) and the other in PRIDE xml format (pride-example.xml) so you can upload them in pride inspector and try the application. There is and additional folder, config, that contains a file called config.props where you can modify the amount of memory assigned to your application (only change if you are trying to view files and is causing the software crash because of a "Out of memory..." exception). The additional 2 directories, lib and log, contain all the java libraries necessary for the application to run and some debugging information if the application crashes.
