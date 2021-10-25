from newspaper import Article

import gensim
from gensim.summarization import summarize

def getSummary(url:str = '') -> list:
    article = Article(url)
    article.download()
    article.parse()

    title = article.title

    keywords = article.keywords

    text = article.text
    # entire article as a plain text
    article.nlp()

    summary = article.summary

    summary_gen = summarize(text, ratio=0.1)
    return title, keywords, article.summary, summary_gen