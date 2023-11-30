#!/usr/bin/env python3
#el output de epitran no es una lista sino una cadena, por ello era necesario tokenisar para evitar símbolos extraños
#simplemente aplicando tokenise fue suficiente para resolver el problema
#el input de este programa es un directorio con archivos .tsv de cuatro columnas y el output es un archivo .tsv
#de seven columns: contador por file,english,filename,idioma,word,IPA tokenised and IPA raw 
#SE RESOLVIO EL index ERROR añadiendo una condición en:
#if tokenise(pron)[-1] not in NoAlFinalPalabra:
#se resolvió el VALUE ERROR: not enough values to unpack (expected 4, got 1) verificando que len(row)=4
#dealing with aymara morphological rules
from ipatok import tokenise
import os
import csv
#I added blank spaces and guion just in case I find a way to show them in the output, by now tokenise suppress them
IPAaymara=["","-","ɶ","ä","ɒ̈","ɒ","æ","ɐ","ɞ̞","œ","ɞ","ɑ","ɜ","ʌ","ə","ø̞","a","y","ɨ","ɪ","i","e","ɛ","e̞","E","ʏ","ɘ","u","o","ʊ","ɔ","ɤ̞","ɤ","ɯ","ɵ","ʊ̈","ʉ","ø","ɪ̈","o̞","t͡ʃ'","t͡ʃʼ","t͡ʃ","t͡ʃʰ","h","k","kʰ","k'","kʼ","l","ʎ","m","n","ɲ","ŋ","p","pʰ","p'","pʼ","q","qʰ","q'","qʼ","ɾ","s","t","tʰ","t'","tʼ","χ","w","W","j"]
NoAlFinalPalabra=["ɲ","k","kʰ","k'","p","pʰ","p'","q","qʰ","q'","t","tʰ","t'","t͡ʃ'","t͡ʃʼ","t͡ʃ","t͡ʃʰ"] 
NotAtSyllableEnd=["ɲ","h","kʰ","k'","kʼ","pʰ","p'","pʼ","qʼ","qʰ","q'","tʼ","tʰ","t'","t͡ʃ'","t͡ʃʼ","t͡ʃʰ"]
alofonos=["i","ʏ","ɘ","ɛ","e","o","ɔ","e̞","E","o̞"]
uvular=["q","qʼ","q'","qʰ","χ"]
vowels=["ɶ","ä","ɒ̈","ɒ","æ","ɐ","ɞ̞","œ","ɞ","ɑ","ɜ","ʌ","ə","ø̞","a","y","ɨ","ɪ","i","e","ɛ","e̞","E","ʏ","ɘ","u","o","ʊ","ɔ","ɤ̞","ɤ","ɯ","ɵ","ʊ̈","ʉ","ø","ɪ̈","o̞"]
vowelsaymara=["æ","ɑ","a","ɪ","i","e","ɛ","u","o","ʊ","ɔ"] #it includes 3 vowels and their usual alophones
consonants=["t͡ʃ'","t͡ʃʼ","t͡ʃ","t͡ʃʰ","h","k","kʰ","k'","kʼ","l","ʎ","m","n","ɲ","ŋ","p","pʰ","p'","pʼ","q","qʰ","q'","qʼ","ɾ","s","t","tʰ","t'","tʼ","χ","w","W","j"]
directory="/home/alonso/PalabrasTraducidasTranscritasIPA/"
#directory='/media/alonso/3361-6630/neologisms/GoogleAPIcloudEpitran/'
for filename in sorted(os.listdir(directory)):
    with open(directory+filename,'r') as csvfile:
        reader = csv.reader(csvfile,delimiter='\t')
        count=0
        for row in reader:
            if len(row) == 4:
                index, english, word, pron = row
                #I put the clause just below to avoid ValueError: The string starts with a tie bar: '͡' 
                if "'͡" not in pron:
                    #verificar que la palabra examinada solamente contenga fonemas aymaras
                    if all([char in IPAaymara for char in tokenise(pron)]):
                        #verificar que no hay palabras que empiecen con r
                        if len(tokenise(pron)) > 0 and tokenise(pron)[0] != "ɾ":
                            #verificar que no haya consonantes al final de palabra
                            if len(tokenise(pron)) > 0 and tokenise(pron)[-1] not in consonants:
                                with open("filetsvTranslatedbyGoogleIPAbyEpitranTokenisedbyIPAtokSelectedNeologisms4.tsv", "a") as f: 
                                #si la palabra NO tiene sonidos alofonos, no hace falta verificas si tiene uvulares
                                    if all([char not in alofonos for char in tokenise(pron)]):
                                        for i in range(len(tokenise(pron)) - 1): # i is the current index
                                            #verificar si la palabra tiene diptongos o hiatos
                                            if tokenise(pron)[i + 1] in vowels and tokenise(pron)[i] in vowels:
                                                break
                                            else:
                                                if i == len(tokenise(pron))-2:
                                                    for i in range(len(tokenise(pron)) - 1): # i is the current index
                                                        #verificar si la palabra tiene consonantes consecutivas
                                                        if tokenise(pron)[i + 1] in consonants and tokenise(pron)[i] in NotAtSyllableEnd:
                                                            break
                                                        else:
                                                            if i == len(tokenise(pron))-2:
                                                                count+=1
                                                                f.write(f"{count}\t{english}\t{filename}\t{filename[13:15]}\t{word}\t{tokenise(pron)}\t{pron}\n")
                                                                #print(count,word,pron)
                                    else:
                                        #la palabra tiene alofonos, verificar si tiene uvulares 
                                        if any([char in uvular for char in tokenise(pron)]):
                                            #la palabra tiene alofonos y uvulares, verificar si tiene diptongos
                                            for i in range(len(tokenise(pron)) - 1): # i is the current index
                                                if tokenise(pron)[i + 1] in vowels and tokenise(pron)[i] in vowels:
                                                    break
                                                else:
                                                    if i == len(tokenise(pron))-2:
                                                        for i in range(len(tokenise(pron)) - 1): # i is the current index
                                                            #verificar si la palabra tiene consonantes consecutivas
                                                            if tokenise(pron)[i + 1] in consonants and tokenise(pron)[i] in NotAtSyllableEnd:
                                                                break
                                                            else:  
                                                                if i == len(tokenise(pron))-2:
                                                                    count+=1
                                                                    f.write(f"{count}\t{english}\t{filename}\t{filename[13:15]}\t{word}\t{tokenise(pron)}\t{pron}\n")

