import os
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# create instance of app in variable 'app'

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'the-online-cookbook'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", 'mongodb://localhost')

mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    
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