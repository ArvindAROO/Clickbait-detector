import numpy as np 
import pandas as pd
import nltk
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



cb_data = pd.read_csv("clickbait_data.csv")

x=cb_data.headline
y=cb_data.clickbait
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.25,random_state=2)

def tokenization(text):
    lst=text.split()
    return lst
train_x=train_x.apply(tokenization)
test_x=test_x.apply(tokenization)

def lowercasing(lst):
    new_lst=[]
    for i in lst:
        i=i.lower()
        new_lst.append(i)
    return new_lst
train_x=train_x.apply(lowercasing)
test_x=test_x.apply(lowercasing)  

def remove_punctuations(lst):
    new_lst=[]
    for i in lst:
        for j in s.punctuation:
            i=i.replace(j,'')
        new_lst.append(i)
    return new_lst
train_x=train_x.apply(remove_punctuations)
test_x=test_x.apply(remove_punctuations) 



def remove_stopwords(lst):
    stop=stopwords.words('english')
    new_lst=[]
    for i in lst:
        if i not in stop:
            new_lst.append(i)
    return new_lst

train_x=train_x.apply(remove_stopwords)
test_x=test_x.apply(remove_stopwords)  

lemmatizer=nltk.stem.WordNetLemmatizer()
def lemmatzation(lst):
    new_lst=[]
    for i in lst:
        i=lemmatizer.lemmatize(i)
        new_lst.append(i)
    return new_lst
train_x=train_x.apply(lemmatzation)
test_x=test_x.apply(lemmatzation)

train_x=train_x.apply(lambda x: ''.join(i+' ' for i in x))
test_x=test_x.apply(lambda x: ''.join(i+' ' for i in x))

freq_dist={}
for i in train_x.head(20):
    x=i.split()
    for j in x:
        if j not in freq_dist.keys():
            freq_dist[j]=1
        else:
            freq_dist[j]+=1


tfidf=TfidfVectorizer()
train_1=tfidf.fit_transform(train_x)
test_1=tfidf.transform(test_x)


# train_arr=train_1.toarray()
# test_arr=test_1.toarray()

NB_MN=MultinomialNB()

NB_MN.fit(train_1,train_y)
pred=NB_MN.predict(test_1)
print(test_1)
print('first 20 actual labels: ',test_y.tolist()[:20])
print('first 20 predicted labels: ',pred.tolist()[:20])



from sklearn.metrics import f1_score,accuracy_score
print("F1 score of the model")
print(f1_score(test_y,pred))
print("Accuracy of the model")
print(accuracy_score(test_y,pred))
print("Accuracy of the model in percentage")
print(accuracy_score(test_y,pred)*100,"%")

f = open('my_classifier.pickle', 'wb')
pickle.dump(NB_MN, f)
f.close()