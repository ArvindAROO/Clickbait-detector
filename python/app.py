# flask app
from flask import Flask, request
from sklearn.base import is_classifier
from newspaper2 import getSummary

from percentage import findPercentage

app = Flask(__name__)

@app.route("/url", methods=['GET'])
def index():

    try:

        url = request.args.get('query')
        isClickBait = False
        title, keywords, articleSummary, nlpSummary = getSummary(url)
        Keywords, articlePercent, nlpPercent = findPercentage(title, keywords, articleSummary, nlpSummary)
        Summary = (articlePercent + nlpPercent)/2
        sol = [Keywords,Summary]
        if nlpPercent < 9.99:
            isClickBait = True
        
        if any( sol[i] > 50 for i in range(len(sol))) or not isClickBait:
            verdict = "<br>The chances of this being a clickbait are low."
        else:
            verdict = "<br>The chances of this being a clickbait are high."
        sol = [str(i)+ "%" for i in sol]
        sol[0] = "Keywords: " + sol[0]
        sol[1] = "Summary: " + sol[1]
        print(articlePercent, nlpPercent)
        return "<h3>Similarities-</h3>" + '<br>'.join(sol) + verdict 
    except:
        return "Summary not available for the current url"