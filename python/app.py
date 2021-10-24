# flask app
from flask import Flask, request
from newspaper2 import getSummary

from percentage import findPercentage

app = Flask(__name__)

@app.route("/url", methods=['GET'])
def index():

    try:

        url = request.args.get('query')
        title, keywords, articleSummary, nlpSummary = getSummary(url)
        sol = findPercentage(title, keywords, articleSummary, nlpSummary)
        if any( sol[i] < 50 for i in range(len(sol))):
            verdict = "The chances of this being a clickbait are high"
        else:
            verdict = "The chances of this being a clickbait are low"
        sol = [str(i)+ "%" for i in sol]
        return ' '.join(sol) + " similarity\n" + verdict 
    except:
        return "Summary not available for the current url"