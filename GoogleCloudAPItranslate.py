#!/usr/bin/env python3



import csv
from pathlib import Path


def translate_text(target, text):
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    import six
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result["translatedText"]


def main(input_file, translate_to):
    """
    Translate a text file and save as a CSV file
    using Google Cloud Translation API
    """
    input_file_path = Path(input_file)
    target_lang = translate_to
    output_file_path = input_file_path.with_suffix('.csv')

    with open(input_file_path) as f:
        list_lines = f.readlines()
        total_lines = len(list_lines)
    with open(output_file_path, 'w') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        my_writer.writerow(['id', 'original_text', 'translated_text'])

        for i, each_line in enumerate(list_lines):
            line_id = f'{i + 1:04}'
            original_text = each_line.strip('\n')  # Strip for the writer(*).
            translated_text = translate_text(
                target=target_lang,
                text=each_line)
            my_writer.writerow([line_id, original_text, translated_text])  # (*)
            # Progress monitor, non-essential.


if __name__ == '__main__':
    origin_file = '/home/alonso/words_alpha.txt'
    output_lang = 'hi'
    main(input_file=origin_file,
         translate_to=output_lang)
