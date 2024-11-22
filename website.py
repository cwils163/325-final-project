import streamlit as st
import pandas as pd
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pickle
from annotated_text import annotated_text
import matplotlib.pyplot as plt
import random

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
        decoded_line = decoded_line.replace('\r', '')

        decoded_line = decoded_line
        split = decoded_line.split('.')

        for i in split:
            sentences.append(i)
    
    print(sentences)
    remove = []
    for i in range(len(sentences)):
        if sentences[i] == '':
            remove.append(i)

    for i in remove:
        sentences.remove('')

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
    print(predictions)

    # gets the results for outputting the text
    results = []
    #"Normal":0,"Depression":0,"Suicidal":1,"Anxiety":0,"Stress":0,"Discrimination":0,"Aggression":0,"Abuse":0,"Pregnancy":0,"Medical":0,"Mental-Health":0,"Sexual-Content":0}
    for i in predictions:
        label = ''
        if i[11] == 1:
            label += 'Sexual-Content '
        if i[1] == 1:
            label += 'Depression '
        if i[2] == 1:
            label += 'Suicidal '
        if i[3] == 1:
            label += 'Anxiety '
        if i[4] == 1:
            label += 'Stress '
        if i[5] == 1:
            label += 'Discrimination '
        if i[6] == 1:
            label += 'Aggression '
        if i[7] == 1:
            label += 'Abuse '
        if i[8] == 1:
            label += 'Pregnancy '
        if i[9] == 1:
            label += 'Medical '
        if i[10] == 1:
            label += 'Mental-Health '
        if i[0] == 1:
            label += 'Normal '
        if label == '':
            label += 'Normal '
        results.append(label)
                # khaki, periwinkle, robin egg blue, light blue, light green, pastel green, apricot, coral pink, light pink, thistle, flax, mauve, rose gold, pastel orange
    print(results)
    colors = ['na'] * len(results)
    color_list = ['#f0e68c', '#ccccff', '#96ded1', '#add8e6', '#90ee90', '#c1e1c1', '#fbceb1', '#f88379', '#ffb6c1', '#d8bfd8', '#eedc82', '#e0b0ff', '#e0bfb8', '#fac898']
    found_results = []
    used_colors = []
    for i in results:
        if i in found_results:
            continue
        else:
            found_results.append(i)
            c = random.choice(color_list)
            while c in used_colors:
                c = random.choice(color_list)
            used_colors.append(c)
            for j in range(len(results)):
                if results[j] == i:
                    colors[j] = c
    print(colors)
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