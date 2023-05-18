#el input de este programa es un directorio con archivos .tsv y el output es el archivo file4tsv.csv
from ipatok import tokenise
import os
import csv
#se retiró β, se reemplazaron tʃʼ,tʃʰ,tʃ por "č","čʰ","č'" 
# se añadio "/" dado que ese caracter acompaña al formato IPA en los archivos de la carpeta csv
IPAquechua=["æ","ɑ","a","ɪ","i","e","ɛ","u","U","o","ʊ","ɔ","h","j","k","k̚","ɣ","x","kʰ","kx","k'","l","ʎ","m","n","ɲ","p","ɸ","pʰ","pɸ","p'","q","ɢ","X","qʰ","q'","ɾ","s","ʃ","t","tʰ","ts","θ","t'","č","čʰ","č'","w","W"]
NoAlFinalPalabra=["h","ñ","č'","čʰ","kʰ","k'","pʰ","p'","qʰ","q'","t","tʰ","t'"] 
alofonos=["ɛ","e","o","ɔ"]
uvular=["q","q'","qʰ"]
vowels=["æ","ɑ","a","ɪ","i","e","ɛ","u","U","o","ʊ","ɔ"]
consonants=["h","j","k","k̚","ɣ","x","kʰ","kx","k'","l","ʎ","m","n","ɲ","p","β","ɸ","pʰ","pɸ","p'","q","ɢ","X","qʰ","q'","ɾ","s","ʃ","t","tʰ","ts","θ","t'","č","čʰ","č'","w"]
directory='/media/alonso/3361-6630/neologisms/tsvbroad/'
for filename in os.listdir(directory):
 with open(directory+filename,'r') as csvfile:
  reader = csv.reader(csvfile,delimiter='\t')
  count=0
  for word,pron in reader:
    #verificar que la palabra examinada solamente contenga fonemas quechuas
    if all([char in IPAquechua for char in tokenise(pron)]): 
        #verificar que no haya consonantes prohibidas al final de palabra
        if tokenise(pron)[-1] not in NoAlFinalPalabra:
          with open("file4tsvIncluyeDiacriticos.csv", "a") as f: 
            #si la palabra NO tiene sonidos alofonos, no hace falta verificas si tiene uvulares
            if all([char not in alofonos for char in tokenise(pron)]):
                for i in range(len(tokenise(pron)) - 1): # i is the current index
                    #verificar si la palabra tiene diptongos
                    if tokenise(pron)[i + 1] in vowels and tokenise(pron)[i] in vowels:
                        break
                    else:
                        if i == len(tokenise(pron))-2:
                            for i in range(len(tokenise(pron)) - 1): # i is the current index
                                #verificar si la palabra tiene consonantes consecutivas
                                if tokenise(pron)[i + 1] in consonants and tokenise(pron)[i] in consonants:
                                    break
                                else:
                                    if i == len(tokenise(pron))-2:
                                        count+=1
                                        f.write(f"{count},{filename},{word},{pron}\n")
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
                                if tokenise(pron)[i + 1] in consonants and tokenise(pron)[i] in consonants:
                                    break
                                else:  
                                    if i == len(tokenise(pron))-2:
                                        count+=1
                                        f.write(f"{count},{filename},{word},{pron}\n")
                                        #print(count,word,pron)
