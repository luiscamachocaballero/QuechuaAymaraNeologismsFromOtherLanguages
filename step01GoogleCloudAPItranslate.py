#!/usr/bin/env python3
import os
import csv
import pandas as pd
from pathlib import Path
from retrying import retry
from google.cloud import translate_v2 as translate
from google.cloud.exceptions import ServiceUnavailable
# Initialize the translation client outside the function to reuse it.
translate_client = translate.Client()

@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=5)
def translate_text(target, text):
    if isinstance(text, bytes):
        text = text.decode("utf-8")

    result = translate_client.translate(text, target_language=target)
    return result["translatedText"]

def main(input_file, translate_to, code):
    input_file_path = Path(input_file)
    target_lang = translate_to
    new_directory = "/home/alonso/PalabrasWikipediaTraducidasGoogleAPI2/"
    output_file_path = new_directory + code + "_" + target_lang + "_" + os.path.basename(input_file_path)

    with open(input_file_path) as f:
        list_lines = f.readlines()

    with open(output_file_path, 'w') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        my_writer.writerow(['id', 'original_text', 'translated_text'])

        for i, each_line in enumerate(list_lines):
            line_id = f'{i + 1:04}'
            original_text = each_line.strip('\n')
            
            # Use retrying to handle transient errors
            translated_text = translate_text_with_retry(
                target=target_lang,
                text=each_line
            )

            my_writer.writerow([line_id, original_text, translated_text])

def translate_text_with_retry(target, text):
    try:
        return translate_text(target, text)
    except Exception as e:
        print(f"Error: {e}")
        raise ServiceUnavailable("Google Cloud Translation API service is temporarily unavailable. Retrying...")

# The path to the directory containing the files
directory = '/home/alonso/words3/'

df = pd.read_csv('ISO639google.csv', sep='\t')

if __name__ == '__main__':
    for index, row in df.iterrows():
        output_lang = row['639-1']
        ISO15924script = row['Code']
        
        for filename in os.listdir(directory):
            origin_file = os.path.join(directory, filename)
            main(input_file=origin_file, translate_to=output_lang, code=ISO15924script)
