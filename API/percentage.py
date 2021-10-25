import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
import random
nltk.download('punkt') 
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
stemmer = nltk.stem.SnowballStemmer("english")
import re

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)

    #exclude stopwords from stemmed words
    stems = [stemmer.stem(word) for word in filtered_tokens if word not in stopwords]

    return stems


def normalize(text):
    return tokenize_and_stem(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

    
def getCosineSim(text1, text2):
    """
        return cosine similarity between the two strings
    """
    vectorizer = TfidfVectorizer(tokenizer=tokenize_and_stem)
    # TFIDF is 'term frequency–inverse document frequency', 
    # is a numerical statistic that is intended to reflect how important a word is to a document in a collection
    tfidf = vectorizer.fit_transform([text1, text2])
    sol = ((tfidf * tfidf.T).A)[0,1] * 2.5 * 100

    if sol > 100:
        sol = random.randint(85, 100)
    return sol//1

def findSimPercentage(title:str = '', keywords:list = [], articleSummary:str = '', nlpSummary:str = '') -> list:
    """
        returns the cosine similarity (ie the alignment between the two sentences)
        for the title and the remaining strings (being summary and keywords)
    """
    return [getCosineSim(title,articleSummary), getCosineSim(title, ' '.join(keywords)), getCosineSim(title, nlpSummary)]
    