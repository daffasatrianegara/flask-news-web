from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

conf = {
    'API_URL': os.getenv('API_URL'),
    'API_KEY': os.getenv('NEWS_API_KEY'),
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/news')
def news():
    search = request.args.get('search')
    newsData = conf['API_URL']
    if(search):
        newsData += f"/everything?q={search}&apikey={conf['API_KEY']}"
    else:
        newsData += f"/everything?q=latest&apikey={conf['API_KEY']}"
    
    return render_template('news.html', search=search, newsData=newsData)

@app.route('/about')
def about():
    return render_template('about.html')