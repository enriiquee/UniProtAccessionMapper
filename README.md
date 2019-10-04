UniProt-AccessionMapper
===============

# About UniProt-AccessionMapper

This script allows to map multiples accessions from different databases to UniProt. 

# Getting UniProt-AccessionMapper

## Installation Requirements

* Python: Python 3.7.* (or above), which you can download for free [here](https://www.python.org/downloads/). (Note: most computers should have Python installed already).
* Operating System: The current version has been tested on Windows 7, Windows Vista, Linux and Max OS X, it should also work on other platforms. If you come across any problems on your platform, please contact me.
* Memory: Accessions files can be very large sometimes, in order to get good performance from AccessionMapper, we recommend you to have 4G of free memory.

## Launch via

To start the script, simply run `Python` from Windows/Linux/Mac terminal. Select the path of your accession file and run it. 

`python UniProtAccesionMapper.py accession_file.txt`

Sometimes `python` PATH is not in recognised. Try to use just:

`py UniProtAccesionMapper.py accession_file.txt`

The program will start and finish with the next message: 

``` 
    INFO - Starting execution
    INFO - Reading file...
    INFO - Saving results...
    INFO - Saved
    INFO - Done. Exiting program.
```

After this, a `excel` file would be created in the same directory where the script is located, with the name: `AccesionUniprot.xlsx`

If you have any error, try to check this line of the code: 
`fp = urllib.request.urlopen("https://www.uniprot.org/uniprot/?query=" + i + "&sort=score")`

In order to fix this, performs a manual search in UniProt and replaces the url of this line of code with the new one, taking into account that `i` is the number of the accession.

