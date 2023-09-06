import os
import string
import pandas as pd

import spacy 

nlp = spacy.load("en_core_web_sm")



file_path = '/Users/tanunair/Downloads/sentiment-analysis.csv' 
df = pd.read_csv(file_path, sep=', ')
print(df.columns)

feedback = df['"Text']

all_feedbacks = ' '.join(feedback)



doc = nlp(all_feedbacks) 

unique_adjectives = set() 

for token in doc:
    if token.pos_ == "ADJ":  # ADJ is the POS (Part of Speech) tag for adjectives in spaCy
        unique_adjectives.add(token.text.lower())

unique_adjectives_list = list(unique_adjectives)

print("Unique Adjectives/Descriptive Words:")
print(unique_adjectives_list) 

