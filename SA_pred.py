import numpy as np
import pandas as pd
import re
import pickle
import joblib

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer


#Fetch the model
classifier = joblib.load('c2_Classifier_Sentiment_Model')


# Get the input and data preprocess
review = "I'm not sure I will ever come back."

cvFile='c1_BoW_Sentiment_Model.pkl'
cv = pickle.load(open(cvFile, "rb"))

processed_input = cv.transform([review]).toarray()[0]
prediction = classifier.predict([processed_input])[0]


# Get the setiment result
prediction_map = {
    0: "negative",
    1: "positive"
}
print(f"The model believes the review is {prediction_map[prediction]}.")
