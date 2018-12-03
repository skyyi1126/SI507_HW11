from flask import Flask, render_template
import requests
from secrets import api_key
import json
app = Flask(__name__)

def get_articles():
    url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    params = {
        "api_key": api_key
    }
    results = requests.get(url, params).json()["results"]
    return results[0:5]
    

@app.route('/user/<nm>')
def articles(nm):    
    results = get_articles()
    text = []
    for i in results:
        text.append(i["title"] + " (" + i["url"] + ")")
    return render_template('user.html', 
        title="Today's top headers in technology are...", my_list=text, name=nm)

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)