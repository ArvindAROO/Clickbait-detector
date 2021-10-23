from newspaper import Article

import gensim
from gensim.summarization import summarize

def newspaper(url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'):
    article = Article(url)
    article.download()

    article.parse()

    article.authors
    ['Leigh Ann Caldwell', 'John Honway']


    text = article.text
    # print("######", text)
    "Washington (CNN) -- Not everyone subscribes to a New Year's resolution..."

    article.nlp()


    # print(article.keywords)

    ['New Years', 'resolution', ...]
    summary = article.summary
    # print("<<<<<<", summary)

    'The study shows that 93% of people ...'
    # print(">>>>>>", article.title)


    summary_gen = summarize(text, ratio=0.05)
    return summary_gen