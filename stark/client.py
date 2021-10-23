from newspaper2 import newspaper
import percentage
if __name__ == '__main__':
    title, keywords, articleSummary, nlpSummary = newspaper("https://www.bbc.co.uk/sport/formula1/59017996")
    percentage.main(title, keywords, articleSummary, nlpSummary)