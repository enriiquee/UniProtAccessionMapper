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

To start the script, simply run `Python` from Windows/Linux/Mac terminal. Select the path of your accession file and run it. 

`python UniProtAccesionMapper.py accession_file.txt`

The program will finish with the next message: 

``` INFO - Saving results...
    INFO - Saved
    INFO - Done. Exiting program.
```

After this, a `excel` file would be created in the same directory where the script is located, with the name: `AccesionUniprot.xlsx`

