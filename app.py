import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from datetime import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# create instance of app in variable 'app'

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'the-online-cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
mongo = PyMongo(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    
@app.route("/recipes")
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())
    
# create and update recipes in the database
    
@app.route("/addrecipe")
def add_recipe():
    return render_template("addrecipe.html", recipes=mongo.db.recipes.find())
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(
        {
            "recipe_name": request.form["recipe_name"],
            "recipe_preptime": request.form["recipe_preptime"],
            "recipe_description": request.form["recipe_description"],
            "recipe_serves": request.form["recipe_serves"],
            "recipe_steps":  request.form.getlist('recipe_step'),
            "recipe_ingredients": request.form.getlist('recipe_ingredient')
                
        })
    return redirect(url_for('get_recipes'))
                        

@app.route('/products')
def products():
    return render_template("products.html")
    
@app.route("/login")
def login():
    return render_template("login.html")
    
@app.route("/my_account")
def account():
    return render_template("account.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)