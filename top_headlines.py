from flask import Flask, render_template
import requests
from secrets import api_key
import json
import datetime

app = Flask(__name__)

def get_articles(section):
    url = "https://api.nytimes.com/svc/topstories/v2/" + section + ".json"
    params = {
        "api_key": api_key
    }
    results = requests.get(url, params).json()["results"]
    return results[0:5]
    
def get_greeting():
    t = datetime.datetime.now()
    h = t.hour
    m = t.minute
    if (h>=0 and h<12) or (h==12 and m==0):
        return "Good morning"
    elif (h<16) or (h==16 and m==0):
        return "Good afternoon"
    elif (h<20) or (h==20 and m==0):
        return "Good evening"
    elif h<=24:
        return "Good night"
    else:
        return "What's wrong with your time"

@app.route('/user/<nm>/<section>')
def articles(nm, section):
    results = get_articles(section)
    text = []
    for i in results:
        text.append(i["title"] + " (" + i["url"] + ")")
    return render_template('user.html', greeting = get_greeting(),
        title="Today's top headers in " + section + " are...", my_list=text, name=nm)

@app.route('/user/<nm>')
def articles_tech(nm):    
    results = get_articles("technology")
    text = []
    for i in results:
        text.append(i["title"] + " (" + i["url"] + ")")
    return render_template('user.html', greeting = get_greeting(),
        title="Today's top headers in technology are...", my_list=text, name=nm)

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'


if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)