import numpy as np 
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string as s
import re
from sklearn.feature_extraction.text import TfidfVectorizer

import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle




test_x = pd.DataFrame(["Which TV Female Friend Group Do You Belong In"])

test_x=test_x.iloc[0,:]


# print(type(test_x))


def tokenization(text):
    lst=text.split()
    return lst

test_x=test_x.apply(tokenization)

def lowercasing(lst):
    new_lst=[]
    for i in lst:
        i=i.lower()
        new_lst.append(i)
    return new_lst

test_x=test_x.apply(lowercasing)  

def remove_punctuations(lst):
    new_lst=[]
    for i in lst:
        for j in s.punctuation:
            i=i.replace(j,'')
        new_lst.append(i)
    return new_lst

test_x=test_x.apply(remove_punctuations) 



def remove_stopwords(lst):
    stop=stopwords.words('english')
    new_lst=[]
    for i in lst:
        if i not in stop:
            new_lst.append(i)
    return new_lst

test_x=test_x.apply(remove_stopwords)  

lemmatizer=nltk.stem.WordNetLemmatizer()

def lemmatzation(lst):
    new_lst=[]
    for i in lst:
        i=lemmatizer.lemmatize(i)
        new_lst.append(i)
    return new_lst

test_x=test_x.apply(lemmatzation)

test_x=test_x.apply(lambda x: ''.join(i+' ' for i in x))

tfidf=TfidfVectorizer()
train_1=tfidf.fit_transform(test_x)
test_1=tfidf.transform(test_x)

print(test_1)

test_arr=test_1.toarray()

print(test_arr)
import pickle
f = open('my_classifier.pickle', 'rb')
NB_MN = pickle.load(f)
f.close()

pred=NB_MN.predict(test_arr)
print(pred)