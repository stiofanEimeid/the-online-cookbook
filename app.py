import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for, session
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# create instance of app in variable 'app'

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['MONGO_DBNAME'] = 'the-online-cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
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
    if 'username' in session:
        return render_template("addrecipe.html", recipes=mongo.db.recipes.find())
    return "Please login/register to add recipes"
    
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
 
# User functionality begins

@app.route('/index')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
        
    return render_template('index.html')
    
@app.route("/index", methods=["POST"])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        # if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'): 
        #         session['username'] = request.form['username']
        if bcrypt.check_password_hash(login_user['password'].encode('utf-8'), request.form['password'].encode('utf-8')):
                session['username'] = request.form['username']
                return redirect(url_for('index'))
                
        return 'Invalid username/password combination'
    
    return 'Invalid username/password combination'
        
    
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            # hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            hashpass = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert({'name' : request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
            
        return 'That username already exists!'
        
    return render_template('register.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
    
@app.route('/account')
def account():
    return render_template('account.html')
    
# User functionality ends

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)