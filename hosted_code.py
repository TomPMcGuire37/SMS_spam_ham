##Bringing in packages

import numpy as np
import pandas as pd
import nltk
nltk.download('punkt')

data = pd.read_csv('C:/Users/Tom/Desktop/R Help/smsspamcollection/SMSSpamCollection.txt', sep='\t', skipinitialspace=True ,header=None)
data.columns =['label', 'text_body']
data['text_body'] = data['text_body'].astype(str)
print(data.head())

data['label'].replace({'ham': 1, 'spam': 0}, inplace=True)
data.info()

"""
nltk_tokens = nltk.word_tokenize(data['text_body'])
print(nltk_tokens) 
"""