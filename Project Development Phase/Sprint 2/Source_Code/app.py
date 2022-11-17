from flask import Flask, render_template , request , redirect
import requests
import json

url = "https://api.newscatcherapi.com/v2/search"


headers = {
    "x-api-key": "API_KEY"
    }   

app = Flask(__name__, static_url_path='/static')

@app.route("/",methods = ['GET'])
def index():
    querystring = {"q":"latest","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(json.loads(response.text)['articles'][0])
    return render_template("index.html" ,data=json.loads(response.text))

@app.route("/sports",methods = ['GET'])
def index_sport():
    querystring = {"q":"sports","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(json.loads(response.text)['articles'][0])
    return render_template("sports.html" ,data=json.loads(response.text))

@app.route("/international",methods = ['GET'])
def index_inter():
    querystring = {"q":"international","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(json.loads(response.text)['articles'][0])
    return render_template("inter.html" ,data=json.loads(response.text))

@app.route("/entertainment",methods = ['GET'])
def index_enter():
    querystring = {"q":"entertainment","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(json.loads(response.text)['articles'][0])
    return render_template("enter.html" ,data=json.loads(response.text))

@app.route("/search",methods = ['POST'])
def index_search():
    querystring = {"q":request.form['search'],"lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(json.loads(response.text)['articles'][0])
    return render_template("search.html" ,data=json.loads(response.text))


if __name__ == '__main__':
   app.run()