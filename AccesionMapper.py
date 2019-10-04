"""Script para cambiar los accession por los de UniProt"""
# Author: Enrique Perez
# Contact: enrique.perez@ucm.es

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
        #output_path = sys.argv[2]

        # file_path = "/home/juanluis/Desktop/mierda_EDU/Prueba.fasta"
        # output_path = "/home/juanluis/Desktop/mierda_EDU/pruebaOUTPUT.fasta"

        # 1. Read the annotation saving the coordinates for each gene

        logger.info('Reading fasta...')

        # Cargamos el txt que queremos analizar
        with open('Accesion.txt', 'r') as filehandle:

            places = []
            accesions_uniprot = []
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
            # handle = urllib.request.urlopen("http://www.uniprot.org/uniprot/J9VS38.xml")

            p = re.compile("class=\"entryID\"><a href=\"/uniprot/(.*)\">")
            result = str(p.search(mystr))

            if result != "None":
                a = re.search('"/uniprot/(.*)"', result).group(1)
            else:
                a = "Sin accesion"
            # accesions_uniprot.append(a)
            accession_dictionary[i] = a
            print(i+"="+a)
            # re.search('name (.*) is valid', resul).group(1)

        # 2. Create the output file and output the results
        logger.info('Saving results...')

        df = pd.DataFrame(data=accession_dictionary, index=[0])

        df = (df.T)

        #print(df)

        df.to_excel('AccesionUniprot.xlsx')

        # 3. Close the file handler
        logger.info('Saved ' )

        logger.info('Done. Exiting program.')

        exit(0)
    except Exception as error:
        logger.error('\nERROR: ' + repr(error))
        logger.error('Aborting execution')
        exit(1)


if __name__ == '__main__':
    main()
