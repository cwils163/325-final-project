import streamlit as st
import pandas as pd
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pickle
from annotated_text import annotated_text
import matplotlib.pyplot as plt

# for stemming the words
def stem_words(words):
    return ' '.join(stemmer.stem(str(word)) for word in words)

# page title and place to upload txt file
st.title("Trigger Warning Testing")
uploaded_file = st.file_uploader("Upload your text file.")

# if file is uploaded
if uploaded_file:
    sentences = []

    # breaks txt file into sentences for prediction
    for line in uploaded_file:
        decoded_line = line.decode()
        decoded_line = decoded_line.lower()

        decoded_line = re.sub(r'http[s]?://\S+', '', decoded_line)
        decoded_line = re.sub(r'\[.*?\]\(.*?\)', '', decoded_line)
        decoded_line = re.sub(r'@\w+', '', decoded_line)
        
        decoded_line = decoded_line.replace('! ', '.')
        decoded_line = decoded_line.replace('? ', '.')
        decoded_line = decoded_line.replace('. ', '.')
        decoded_line = decoded_line.replace('\n', '')

        decoded_line = decoded_line
        split = decoded_line.split('.')

        for i in split:
            sentences.append(i)

    # adds sentences to dataframe
    df = pd.DataFrame()
    df['sentences'] = sentences

    # tokenizes the words
    df['sentences'] = df['sentences'].apply(word_tokenize)

    # stems the words
    stemmer = PorterStemmer()
    df['sentences'] = df['sentences'].apply(stem_words)
    text = df['sentences']

    # loads vectorizer and vectorizes the text
    with open('tfidf_pkl', 'rb') as f:
        trained_vect = pickle.load(f)
        text_vect = trained_vect.transform(text)

    # predicts labels for text using uploaded model
    with open('model_pkl', 'rb') as f:
        trained_model = pickle.load(f)
        predictions = trained_model.predict(text_vect)

    # uploads the label encoder
    with open('labels_pkl', 'rb') as f:
        imp_labels = pickle.load(f)

    # gets labels from the label encoder
    labels = imp_labels.classes_

    # gets the results for outputting the text
    colors = []
    results = []
    for i in predictions:
        if labels[i] == 'Suicidal':
            colors.append('#ff7f50') # coral
        elif labels[i] == 'Anxiety':
            colors.append('#ccccff') # periwinkle
        elif labels[i] == 'Depression':
            colors.append('#d8bfd8') # thistle
        elif labels[i] == 'Bipolar':
            colors.append('#ffff8f') # canary yellow
        elif labels[i] == 'Stress':
            colors.append('#f0e68c') # khaki
        elif labels[i] == 'Normal':
            colors.append('#e5e4e2') # platinum
        else: # Personality Disorder
            colors.append('#c1e1c1') # pastel green
        results.append(labels[i])

    st.markdown('#')
    st.header('Results:')
    
    # gets info for pie chart
    counts = []
    counts_labels = []
    pie_colors = []
    for i in range(len(results)):
        if results[i] in counts_labels:
            continue
        else:
            counts.append(results.count(results[i]))
            counts_labels.append(results[i])
            pie_colors.append(colors[i])

    # sets up and prints out pie chart
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts_labels, autopct='%1.0f%%', colors=pie_colors)
    ax.axis('equal')
    st.pyplot(fig)

    #print out text with trigger warnings
    for i in range(len(sentences)):
        annotated_text(
            (sentences[i], results[i], colors[i])
        )