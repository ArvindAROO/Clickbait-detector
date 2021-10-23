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
def main(title, keywords,articleSummary, nlpSummary):
    


    b = """Verstappen called Hamilton a "stupid idiot" over the team radio after an incident in which the two raced side by side down the pit straight.
Verstappen then gave Hamilton a middle-finger salute as they accelerated out of the corner.
Hamilton was third, his best lap deleted, while Verstappen was eighth.
The incident between Hamilton and Verstappen happened when Hamilton passed the Red Bull going into the final corner.
The television cameras caught only the very end of a situation that had begun earlier in the lap when Verstappen passed Hamilton."""
    c = ['second', 'verstappen', 'hamilton', 'frustrated', 'lap', 'sergio', 'lewis', 'set', 'practice', 'gp', 'max', 'perez', 'red', 'bottas', 'fastest', 'track', 'session']
    d = """
    New Jersey residents voted to raise the state’s minimum wage by $1 to $8.25 per hour."""
    print(cosine_sim('a little bird', 'a little bird'))
    print(cosine_sim('a little bird', 'a little bird chirps'))
    print(cosine_sim('a little bird', 'a big dog barks'))
    print("summary for newspaper>", cosine_sim(title,articleSummary))
    print("keywords>", cosine_sim(title, ' '.join(keywords)))
    print("nlp summary>", cosine_sim(title, nlpSummary))
    