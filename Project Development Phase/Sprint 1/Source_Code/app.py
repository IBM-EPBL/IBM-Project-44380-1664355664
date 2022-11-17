from flask import Flask, render_template , request , redirect

app = Flask(__name__, static_url_path='/static')

@app.route("/",methods = ['GET'])
def admin():
    return "Home Page"


if __name__ == '__main__':
   app.run(debug = True)