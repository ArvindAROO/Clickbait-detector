# flask app
from flask import Flask, request
from newspaper2 import getSummary

import percentage

app = Flask(__name__)


@app.route("/url", methods=['GET'])

def index():

    url = request.args.get('query')
    title, keywords, articleSummary, nlpSummary = getSummary(url)
    sol = percentage.findPercentage(title, keywords, articleSummary, nlpSummary)
    sol = [str(i)+ "%" for i in sol]
    return ' '.join(sol) + " similarity"
