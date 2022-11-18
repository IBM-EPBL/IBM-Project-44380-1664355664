from flask import Flask, render_template , request , redirect , session
import requests
import json
import ibm_db


conn_str='<IBM_API>'
conn = ibm_db.connect(conn_str,'','')

url = "https://api.newscatcherapi.com/v2/search"
headers = {
    "x-api-key": "<NEWS_API>"
    }   

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'nmc8so7c0no78ypw9o8b[np0'

@app.route("/db",methods=['GET'])
def db():
#    sql = "create table users (id integer not null GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),name varchar(500),email varchar(500),password varchar(225),PRIMARY KEY (id));"
#    stmt = ibm_db.exec_immediate(conn, sql)
   return "ok"


@app.route("/",methods = ['GET'])
def index():
    querystring = {"q":"latest","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("index.html" ,data=json.loads(response.text))

@app.route("/sports",methods = ['GET'])
def index_sport():
    querystring = {"q":"sports","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("sports.html" ,data=json.loads(response.text))

@app.route("/international",methods = ['GET'])
def index_inter():
    querystring = {"q":"international","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("inter.html" ,data=json.loads(response.text))

@app.route("/entertainment",methods = ['GET'])
def index_enter():
    querystring = {"q":"entertainment","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("enter.html" ,data=json.loads(response.text))

@app.route("/search",methods = ['POST'])
def index_search():
    querystring = {"q":request.form['search'],"lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("search.html" ,data=json.loads(response.text))

@app.route("/login",methods = ['GET'])
def index_login():
    return render_template("login.html")

@app.route("/signin",methods = ['POST'])
def index_signin():
    sql = "select * from users where email='"+request.form["email"]+"'"
    stmt = ibm_db.exec_immediate(conn, sql)
    data = []
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        data.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)
    if(data):
        if(data[0]["PASSWORD"]==request.form["password"]):
            session["user"]=data[0]["ID"]
            session["name"]=data[0]["NAME"]
            session["email"]=data[0]["EMAIL"]
            return redirect("/user")
        else:
            return redirect("/login")
    else:
        return redirect("/login")

@app.route("/register",methods = ['GET'])
def index_register():
    return render_template("register.html")

@app.route("/signup",methods = ['POST'])
def index_signup():
    sql = "INSERT INTO users (name , email , password)values('"+request.form["name"]+"','"+request.form["email"]+"','"+request.form["password"]+"')"
    stmt = ibm_db.exec_immediate(conn, sql)
    return redirect("/login")



# USER

@app.route("/user/",methods = ['GET'])
def user():
    querystring = {"q":"latest","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("user/index.html" ,data=json.loads(response.text))

@app.route("/user/sports",methods = ['GET'])
def user_sport():
    querystring = {"q":"sports","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("user/sports.html" ,data=json.loads(response.text))

@app.route("/user/international",methods = ['GET'])
def user_inter():
    querystring = {"q":"international","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("user/inter.html" ,data=json.loads(response.text))

@app.route("/user/entertainment",methods = ['GET'])
def user_enter():
    querystring = {"q":"entertainment","lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("user/enter.html" ,data=json.loads(response.text))

@app.route("/user/search",methods = ['POST'])
def user_search():
    querystring = {"q":request.form['search'],"lang":"en","sort_by":"relevancy","page":"1"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return render_template("user/search.html" ,data=json.loads(response.text))

@app.route("/user/logout",methods = ['GET'])
def user_logout():
    return redirect("/")


if __name__ == '__main__':
   app.run()