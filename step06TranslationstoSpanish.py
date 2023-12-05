#!/usr/bin/env python3
# sexto paso
# translate from english to spanish 
import os
import csv
import pandas as pd
from google.cloud import translate_v2 as translate
from retrying import retry
from google.cloud.exceptions import ServiceUnavailable

# Initialize translation client
translate_client = translate.Client()

# Define a retry decorator to handle transient failures
@retry(wait_fixed=1000, stop_max_attempt_number=5)
def translate_text(text, source_language, target_language):
    try:
        result = translate_client.translate(text, source_language=source_language, target_language=target_language)
        return result["translatedText"]
    except ServiceUnavailable as e:
        print(f"Service Unavailable. Retrying... Error: {e}")
        raise

# Define the input filename
filenameinput = "sourceWiktionary-translatedbyGoogle-IPAbyEpitran-tokenisedbyIPAtok-selectedAymaraNeologisms-transcribed.tsv"

# Read the CSV file
with open(filenameinput, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        if len(row) == 9:
            index, ordinal, english, filename, language, word, IPA_tokenised, IPA_raw, aymara = row
            try:
                # Translate English to Spanish
                spanish = translate_text(english, source_language='en', target_language='es')
                # Write the translated data to a new file
                with open(f"translatedtospanish-{filenameinput}", "a") as f:
                    f.write(f"{ordinal}\t{filename[4:12]}\t{word}\t{IPA_tokenised}\t{aymara}\t{english}\t{spanish}\n")
            except Exception as e:
                print(f"Error translating: {e}")

