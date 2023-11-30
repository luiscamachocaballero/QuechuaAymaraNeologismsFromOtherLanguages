#!/usr/bin/env python3
#Este es el segundo paso. Este script recibe como input un archivo csv con tres columnas: numeración, english words y
#the same words translated to another language. The output is a set of tsv files con cuatro columnas, las tres anteriores
#más la transcripción IPA de la palabra en el idioma traducido
import os
import csv
#import pandas as pd
from csv import writer
from csv import reader
from epitran.backoff import Backoff

directory="/home/alonso/PalabrasWiktionaryTraducidasGoogleAPI/" #directorio donde están las palabras traducidas
new_directory="/home/alonso/PalabrasWiktionaryTraducidasTranscritasIPA/" #here will be saved the files with IPA notation

for filename in sorted(os.listdir(directory)):
    # Open the input_file in read mode and output_file in write mode
    code = filename[:8]        
    backoff = Backoff([code], cedict_file='/media/alonso/3361-6630/neologisms/cedict_ts.u8')
    newfile = new_directory+"IPA_"+filename 
    with open(directory+filename, 'r') as f, \
        open(newfile, 'w', newline='') as w:
        # Create a csv.reader object from the input file object
        csv_reader = reader(f)
        # Create a csv.writer object from the output file object
        csv_writer = writer(w, delimiter='\t', lineterminator='\n')
        # Read each row of the input csv file as list
    #type(csv_reader[0])
        for row in csv_reader:
            IPA=backoff.trans_list(row[2])
        #este procedimiento coloca row e IPA en la misma fila 
            row.append(IPA)
        # Add the updated row / list to the output file oxfioxfi
            csv_writer.writerow(row)
