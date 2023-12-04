#!/usr/bin/env python3
#este es el quinto paso, el reporte de palabras encontradas por idioma
#esta versión funciona y es un poco más legible
import os
import pandas as pd

# Read the main DataFrame
df_main = pd.read_csv("sourceWiktionary-translatedbyGoogle-IPAbyEpitran-tokenisedbyIPAtok-selectedAymaraNeologisms-transcribed.tsv", sep='\t')

# Extract language information from the filename
df_main['language'] = df_main['filename'].str[4:12]

# Count values based on the language column
df_counts = df_main['language'].value_counts().to_frame().reset_index()
df_counts.columns = ['language', 'count']

# Initialize a dictionary to store the total word count per language
language_word_count = {}

# Directory containing CSV files
directory = "/home/alonso/PalabrasWiktionaryTraducidasTranscritasIPA/"

# Iterate through CSV files and update the word count dictionary
for file in os.listdir(directory):
    if file.endswith(".csv"):
        tag = file[4:12]
        df_file = pd.read_csv(os.path.join(directory, file), sep='\t')
        language_word_count[tag] = len(df_file)

# Add the total word count to the main DataFrame
df_counts['words'] = df_counts['language'].map(language_word_count)

# Calculate the percentage
df_counts['percentage'] = (df_counts['count'] / df_counts['words'] * 100).round()

# Save the intermediate DataFrame to a CSV file (optional)
df_counts.to_csv("ReportAymaraWordspartialwiki.csv", sep='\t', index=False)

# Read the second DataFrame
df_iso639 = pd.read_csv("/media/alonso/3361-6630/neologisms/outputs_2nd_paper/ISO639GoogleEpitran.csv", sep='\t')

# Merge the two DataFrames based on the 'language' column
df_combined = pd.merge(df_iso639, df_counts, left_on='Code', right_on='language', how='left')

# Save the final DataFrame to a CSV file
df_combined.to_csv("ReportAymaraWordsWiktionary.csv", sep='\t', index=False)
