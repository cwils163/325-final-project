import pandas as pd
import matplotlib.pyplot as plt
import nltk
#nltk.download('punkt_tab') # RUN WITH THIS ONCE
from nltk.tokenize import word_tokenize

# imports csv data to pandas datafram
data = pd.read_csv('Data.csv', index_col=0)

# removes NAN values from dataframe
data.dropna(inplace=True)
#print(data.head())

## prints current labels in dataset
#statusOptions = []
#for i in data['status']:
#    if statusOptions.count(i) <= 0:
#        statusOptions.append(i)
#print(statusOptions)

## get pie chart for distribution of labels
#OptionCount = []
#labels = []
#labels = ['Anxiety', 'Normal', 'Depression', 'Suicidal', 'Stress', 'Bipolar', 'Personality disorder']
#for l in labels:
#    OptionCount.append(data['status'].value_counts()[l])
#print(OptionCount)
#plt.pie(OptionCount, labels=labels, autopct='%1.1f%%')
#plt.show()

## gets information about number of chars and sentences for each label
## is a lot, going to put it into a box and whiskers plot
#labels = ['Anxiety', 'Normal', 'Depression', 'Suicidal', 'Stress', 'Bipolar', 'Personality disorder']
#for l in labels:
#    df = pd.DataFrame()
#    smallerdf = data[data['status'].isin([l])]
#    df['num_of_chars'] = smallerdf['statement'].str.len()
#    df['num_of_sentences'] = smallerdf['statement'].apply(lambda x: len(nltk.sent_tokenize(x)))
#    description = df[['num_of_chars', 'num_of_sentences']].describe()
#    print(l)
#    print(description)
#    print('')

# gets number of chars and sentences per label and put them into box and whiskers plot
df = pd.DataFrame()
df['num_of_chars'] = data['statement'].str.len()
df['num_of_sentences'] = data['statement'].apply(lambda x: len(nltk.sent_tokenize(x)))
df['status'] = data['status']
#df.boxplot(by='status', column=['num_of_chars'])
df.boxplot(by='status', column=['num_of_sentences'])
plt.show()