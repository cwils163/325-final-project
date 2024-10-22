import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import nltk
#nltk.download('punkt_tab') # RUN WITH THIS ONCE
from nltk.tokenize import word_tokenize

# imports csv data to pandas datafram
data = pd.read_csv('Data.csv', index_col=0)

# removes NAN values from dataframe
data.dropna(inplace=True)
#print(data.head())

