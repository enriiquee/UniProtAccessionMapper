"""Script to change accessions to UniProt accessions"""

import logging
import re
import sys
import urllib
import pandas as pd

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create console handler and set level to info
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def main():
    try:
        logger.info('Starting execution')
        # Load the fasta file
        file_path = sys.argv[1]
        # output_path = sys.argv[2]

        # file_path = "/home/Desktop/Prueba.fasta"

        # 1. Read the accessions from the file we want to change

        logger.info('Reading file...')

        with open(file_path, 'r') as filehandle:

            places = []
            accession_dictionary = {}
            for line in filehandle:
                # remove linebreak which is the last character of the string
                currentPlace = line[:-1]
                # add item to the list
                places.append(currentPlace)

        for i in places:
            # Take info from  WEB
            fp = urllib.request.urlopen("https://www.uniprot.org/uniprot/?query=" + i + "&sort=score")
            mybytes = fp.read()
            mystr = mybytes.decode("utf8")
            fp.close()

            # print(mystr)
            # From html, we take the line we are interesting
            p = re.compile("class=\"entryID\"><a href=\"/uniprot/(.*)\">")
            result = str(p.search(mystr))

            # If there isn't a result.
            if result != "None":
                a = re.search('"/uniprot/(.*)"', result).group(1)
            else:
                a = "No accession"
            # accesions_uniprot.append(a)
            accession_dictionary[i] = a
            print(i + "=" + a)
            # re.search('name (.*) is valid', resul).group(1)

        # 2. Create the output file and output the results
        logger.info('Saving results...')

        # Export dictionary to excel file
        df = pd.DataFrame(data=accession_dictionary, index=[0])
        df = df.T

        # print(df)
        df.to_excel('AccesionUniprot.xlsx')

        # 3. Close the file handler
        logger.info('Saved ')

        logger.info('Done. Exiting program.')

        exit(0)
    except Exception as error:
        logger.error('\nERROR: ' + repr(error))
        logger.error('Aborting execution')
        exit(1)


if __name__ == '__main__':
    main()

