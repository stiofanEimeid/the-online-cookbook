import os
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime

# create instance of app in variable 'app'

app = Flask(__name__)

@app.route("/")
def hello():
    return "Milestone Project 3 is under construction"
    
@app.route('/products')
def products():
    return render_template("products.html")
    
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)