# flask app
from flask import Flask, request
from newsScraper import getSummary

from percentage import findSimPercentage

app = Flask(__name__)

@app.route("/url", methods=['GET'])
def main():
    try:
        url = request.args.get('query') #the url to be checked
        
        title, keywords, articleSummary, nlpSummary = getSummary(url) #get the relevant info from the article
        KeywordsSimilarity, articlePercentSimilarity, nlpPercentSimilarity = findSimPercentage(title, keywords, articleSummary, nlpSummary) #find the similarity
        
        finalSummaryPercentage = (articlePercentSimilarity + nlpPercentSimilarity) / 2 # average of two types
        similarityArray = [KeywordsSimilarity, finalSummaryPercentage]
        
        if all( similarityArray[i] < 50 for i in range(len(similarityArray))) or nlpPercentSimilarity < 9.99:
            verdict = "<br>The chances of this being a clickbait are high"
        else:
            verdict = "<br>The chances of this being a clickbait are low."
        similarityArray = [str(i)+ "%" for i in similarityArray]
        similarityArray[0] = "Keywords: " + similarityArray[0]
        similarityArray[1] = "Summary: " + similarityArray[1]
        return "<h3>Similarities-</h3>" + '<br>'.join(similarityArray) + verdict 
    except Exception as E:
        print(E)
        return "Summary not available for the current url"