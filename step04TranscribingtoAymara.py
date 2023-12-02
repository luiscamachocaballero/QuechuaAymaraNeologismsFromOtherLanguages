#!/usr/bin/env python3
#este es el cuarto paso
#convertir la transcripción IPA en una palabra quechua
#se añade una columna al archivo tsv input, dicha columna contiene la palabra quechua correspondiente a la transcripción IPA
import os
import csv
import ast
import pandas as pd
from ipatok import tokenise
def tsv_to_dict(file_path):
    result_dict = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        for row in tsv_reader:
            if len(row) >= 2:
                key = row[0]
                value = row[1]
                result_dict[key] = value
    return result_dict
# Example usage
tsv_file_path = '/media/alonso/3361-6630/neologisms/AlfabetoAymara.tsv'
my_dict = tsv_to_dict(tsv_file_path)
#add this symbols to separate words with blank spaces
my_dict[' '] = ' '
my_dict['-'] = '-'
df=pd.read_csv("/home/alonso/Documents/TranslatedbyGoogleIPAbyEpitranTokenisedbyIPAtokSelectedAymaraNeologismsInfochimpsSource.tsv", sep='\t', names=["ordinal", "english", "filename", "language", "word", "IPA tokenised","IPA raw"])
# la siguiente linea creó una columna, obviamente se ejecuta una sola vez
df.insert(loc=7,column="aymara",value="")
#palabra_escrita_en_aymara=""
for index,word in enumerate(df["IPA raw"].values):
    palabra_escrita_en_aymara=""
    #for letter in str(word):
    for letter in ast.literal_eval(word):
        #if letter in list(my_dict.keys()):
        if letter in my_dict:
        #buscamos en el diccionario el valor equivalente al caracter IPA
            palabra_escrita_en_aymara+=my_dict[letter]
    #despues de construida la palabra quechua, la añadimos al dataframe, en la misma fila
    df.at[index,"aymara"]=palabra_escrita_en_aymara.rstrip()
    
 #grabar en el archivo GlosaTSV
df.to_csv("TranslatedbyGoogleIPAbyEpitranTokenisedbyIPAtokSelectedAymaraNeologismsInfochimpsSourceTranscribed2.tsv", sep='\t')
