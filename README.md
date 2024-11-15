# Content Warning: Mental Health Sentiment Analysis and Trigger Detection

## Overview

One in five adults in the United States suffer from mental illness, and five in every one hundred adults suffer from some form of Post Traumatic Stress Disorder (PTSD). For individuals facing these challenges, consuming media can often be stressful due to exposure to triggering content with little or no prior warning. 

The goal of this project is to develop a tool that helps readers regain confidence and comfort while engaging with media. This tool aims to provide readers with peace of mind by ensuring they receive appropriate forewarnings for any potentially triggering content.

## Project Objectives

- **Sentiment Analysis for Mental Health Contexts**  
  Utilize sentiment analysis techniques to classify the tone of a given text as it relates to common mental health statuses.

- **Comprehensive Trigger Detection**  
  Develop a robust model that identifies a list of potential triggers within a work, using data from research papers like Wolska’s *Trigger Warnings: Bootstrapping a Violence Detector for Fan Fiction*.

## Methodology

1. **Data Collection**
   - Source labeled datasets relevant to mental health sentiment and trigger detection (e.g., Wolska’s dataset).
   - Use additional open-source datasets for training and validation of sentiment and trigger detection models.

2. **Model Development**
   - Tokenize and preprocess text so our model can properly utilize it in training and testing.
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
- \[b2\] Wolska, Magdalena. "Trigger Warnings: Bootstrapping a Violence Detector for Fan Fiction." Available at: [https://downloads.webis.de/publications/papers/wolska_2023.pdf]
- \[b3\] Sarkar, Suchintika. "Sentiment Analysis for Mental Health: Unlocking Mental Health Patterns through Statements." Available at: [https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health/data]

---

## Future Work

- Expanding the trigger detection model to cover more nuanced triggers across multiple media types.

---
## Our Code

- `Data.csv`: A csv file containing the data from Kaggle
- `dataAnalysis.py`: A python file used to analyze the data contained in Data.csv
- `model.ipynb`: A Jupyter file that performs the baseline implementation of our model.
- `B_CM.png, DT_CM.png, LR_CM.png`: PNG files of the confusion matrices generated from running model.ipynb
---
## How to Compile
- To compile our code you will need streamlit installed. To run the website with streamlit use the command `streamlit run website.py`
## Contributors

- **Deborah (Katie) Moffitt**
- **Constance Wilson**
- **Laura Smith** 
