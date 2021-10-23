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
    return sol
def main(string):
    


    a = """
    New Year, new laws: Obamacare, pot, guns and drones"""
    b = """
    Oregon: Family leave in Oregon has been expanded to allow eligible employees two weeks of paid leave to handle the death of a family member.\nArkansas: The state becomes 
    the latest state requiring voters show a picture ID at the voting booth.\nMinimum wage and former felon employmentWorkers in 13 states and four cities will see increases to the minimum wage.\nNew Jersey residents voted to raise the state’s minimum wage by $1 to $8.25 per hour.\nCalifornia is also raising its minimum wage to $9 per hour, but workers must wait until July to see the addition.
    """
    c = ['state', 'minimum', 'national', 'wage', 'laws', 'family', 'law', 'drones', 'leave', 'states', 'obamacare', 'latest', 'pot', 'guns']
    d = """
    New Jersey residents voted to raise the state’s minimum wage by $1 to $8.25 per hour."""
    print(cosine_sim('a little bird', 'a little bird'))
    print(cosine_sim('a little bird', 'a little bird chirps'))
    print(cosine_sim('a little bird', 'a big dog barks'))
    print("summary for newspaper>", cosine_sim(a,b))
    print("keywords>", cosine_sim(a, ' '.join(c)))
    print("nlp summary>", cosine_sim(a, d))
    print("For input>>>>", cosine_sim(a, string))