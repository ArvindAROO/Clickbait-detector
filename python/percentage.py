import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
import random
nltk.download('punkt') # if necessary...
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
stemmer = nltk.stem.SnowballStemmer("english")

remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))
vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    
def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    sol = ((tfidf * tfidf.T).A)[0,1]
    # print(">>>>>", sol)
    sol = sol * 2.5

    if sol > 1:
        sol = random.randint(85, 100)
        sol/=100
    return (sol * 100)//1
def findPercentage(title, keywords,articleSummary, nlpSummary):
    # print("percentage file")
    print("summary for newspaper>", cosine_sim(title,articleSummary))
    print("keywords>", cosine_sim(title, ' '.join(keywords)))
    print("nlp summary>", cosine_sim(title, nlpSummary))
    return [cosine_sim(title,articleSummary), cosine_sim(title, ' '.join(keywords)), cosine_sim(title, nlpSummary)]
    