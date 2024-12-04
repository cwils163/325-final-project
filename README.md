# Content Warning: Mental Health Sentiment Analysis and Trigger Detection

## Overview

One in five adults in the United States suffer from mental illness, and five in every one hundred adults suffer from some form of Post Traumatic Stress Disorder (PTSD). For individuals facing these challenges, consuming media can often be stressful due to exposure to triggering content with little or no prior warning. 

The goal of this project is to develop a tool that helps readers regain confidence and comfort while engaging with media. This tool aims to provide readers with peace of mind by ensuring they receive appropriate forewarnings for any potentially triggering content.

## Project Objectives

- **Sentiment Analysis for Mental Health Contexts**  
  Utilize sentiment analysis techniques to classify the tone of a given text as it relates to common mental health statuses.

- **Comprehensive Trigger Detection**  
  Develop a robust model that identifies a list of potential triggers within a work, using data from research papers like Wolska’s *Trigger Warnings: Bootstrapping a Violence Detector for Fan Fiction* and *Trigger Warning Assignment as a Multi-Label Document Classification Problem* by Wiegmann.

## Methodology

1. **Data Collection**
   - Source labeled datasets relevant to mental health sentiment and trigger detection.
   - Use additional open-source datasets for training and validation of sentiment and trigger detection models.

2. **Model Development**
   - Tokenize and preprocess text so our model can properly utilize it in training and testing.
      - In the process of working on model accuracy we ended up with two models that differ in the way that they break words down to their roots. One model uses Stemming which will not necessarily generate real words for roots and the other uses Lemming which guarantees real words.
   - Use a logistic regression model for mental health sentiment classification.
   - Fine-tune the model to classify texts with mental health-related sentiments and generate a comprehensive list of triggers within the content.
   - Use specialized natural language processing techniques to enhance the model’s ability to identify subtle triggers in text.

4. **Evaluation**
   - Evaluate the model’s effectiveness in classifying mental health tones and identifying triggers using relevant metrics like precision, recall, and F1-score.
   - Utilize a confusion matrix to help visualize our model's performance.

## Expected Outcomes

- **Comprehensive Mental Health Sentiment Classification**  
  A model capable of accurately assessing the mental health-related tone of text.

- **Detailed Trigger Warnings**  
  A tool that generates a detailed list of identified triggers, providing users with transparent and specific content warnings.

- **Enhanced Reading Experience**  
  Users will experience greater comfort and safety in consuming media with forewarnings for potential triggers.

## References

- \[b1\] *National Institute of Mental Health*. "Mental Illness." Available at: [https://www.nimh.nih.gov](https://www.nimh.nih.gov).
- \[b2\] Wolska, Wiegmann, Schröder, Borchardt, Stein, Potthast. "Trigger Warnings: Bootstrapping a Violence Detector for Fan Fiction." Available at: [https://downloads.webis.de/publications/papers/wolska_2023.pdf]
- \[b3\] Sarkar, Suchintika. "Sentiment Analysis for Mental Health: Unlocking Mental Health Patterns through Statements." Available at: [https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data]
- \[b4\] Wiegmann, Wolska, Schröder, Borchardt, Stein, Potthast. "Trigger Warning Assignment as a Multi-Label Document Classification Problem." Available at: [https://aclanthology.org/2023.acl-long.676.pdf]
- \[b5\] Wiegmann, "acl23-trigger-warning-assignment." Available at: [https://github.com/MattiWe/acl23-trigger-warning-assignment?tab=readme-ov-file]

---

## Future Work

- Continuing to increase accuracy of the model
  - With further cleaning of the data we believe we can increase the model's accuracy. The data we used contained large chunks of text from a piece of literature with multiple labels attached. These labels are sometimes only attributed to a piece of that text, sometimes just a phrase or a word. If we could break down the text and more specifically label those smaller pieces within the whole text, it would probably improve the model's accuracy.
  - This can be seen by how a lot of the broken down phrases and sentences weren't always labeled the most accurate label, but as a whole the text did contain the list of labels that was generated. I believe this is because of how it was trained on data that labeled large chunks of text rather than specific pieces of it. 
- Train with full Wiegmann Dataset
  - This would take a longer time to clean and setup the data as even just the small chunk took us a while. We believe using the full dataset would give the model more data to train on and could possibly improve the outputs.
 
## What We Learned

We learned a lot from this project, especially a lot about the processing of data before a model is even trained. In many of our assignments and other classes we are given datasets that have already been processed and optimized for the project, but this is one of the first times where we had to shape and set up the dataset so that it would work better for our model. We know now that picking the right dataset is very important to a project, and that sometimes something that you think will help the dataset to improve the accuracy may not be the problem with the accuracy at all. We realize that tuning the datasets and improving accuracy of a model is all part of machine learning and that people spend their careers focused on that. 

---
## Our Code

- `Dataset_Setup`: Code and files relating to the setting up/creation of our datasets.
- `Datasets`: Datasets actively used in our models.
- `Demonstration_Text`: .txt examples to use for our in class presentation as well as .jpg examples of website results.
- `Lemming_Model`: Model and other files needed to run our model that uses Lemmatize in place of Stemming.
- `Midterm_Model`: Code and images used for our midterm report.
- `Stemming_Model`: Model and other files needed to run our model that uses Stemming in place of Lemmatize
---
## How to Compile
- To compile our website code you will need streamlit installed.
- Running the Lemming Model
  - Navigate to `/Lemming_Model`
  - Run code in the Jupyter notebook titled `lem_model.ipynb`
- Running the Interactive Website for the Lemming Model: 
  - Navigate to `/Lemming_Model`
  - Run command `streamlit run LemWebsite.py`
- Running the Stemming Model
  - Navigate to `/Stemming_Model`
  - Run code in the Jupyter notebook titled `stem_model.ipynb`
- Running the Interactive Website for the Stemming Model: 
  - Navigate to `/Stemming_Model`
  - Run command `streamlit run StemWebsite.py`
## Contributors

- **Deborah (Katie) Moffitt**
- **Constance Wilson**
- **Laura Smith** 
