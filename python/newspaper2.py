from newspaper import Article

import gensim
from gensim.summarization import summarize

def getSummary(url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'):
    # print("got request in newspaper file")
    article = Article(url)
    article.download()

    article.parse()

    article.authors


    text = article.text
    # print("######", text)

    article.nlp()

    # print(article.keywords)

    summary = article.summary
    # print("<<<<<<", summary)


    # print(">>>>>>", article.title)


    summary_gen = summarize(text, ratio=0.1)
    return article.title, article.keywords, article.summary, summary_gen