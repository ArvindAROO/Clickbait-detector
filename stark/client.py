from newspaper2 import getSummary

import percentage
def main():
    title, keywords, articleSummary, nlpSummary = getSummary("https://www.bbc.co.uk/sport/formula1/59017996")
    percentage.findPertentage(title, keywords, articleSummary, nlpSummary)
if __name__ == '__main__':
    main()