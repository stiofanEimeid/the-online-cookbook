import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for, session, flash
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
    
@app.route("/recipe/<id>")
def recipe(id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    return render_template("recipe.html", recipe=recipe)
    
# create and update recipes in the database
    
@app.route("/add_recipe")
def add_recipe():
    if 'username' in session:
        return render_template("addrecipe.html", recipes=mongo.db.recipes.find())
    return "Please login/register to add recipes"
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
        recipes = mongo.db.recipes
        recipes.insert_one(
            {
                "recipe_name": request.form.get("recipe_name"),
                "recipe_preptime": request.form.get("recipe_preptime"),
                "recipe_description": request.form.get("recipe_description"),
                "recipe_serves": request.form.get("recipe_serves"),
                "recipe_steps":  request.form.getlist('recipe_step'),
                "recipe_ingredients": request.form.getlist('recipe_ingredient'),
                "name": session["username"]
            })
        return redirect(url_for('get_recipes'))
        
@app.route('/edit_recipe/<id>')
def edit_recipe(id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    return render_template("editrecipe.html", recipe=recipe)

@app.route('/update_recipe/<id>', methods=["POST"])
def update_recipe(id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(id)},
            {
                "recipe_name": request.form.get("recipe_name"),
                "recipe_preptime": request.form.get("recipe_preptime"),
                "recipe_description": request.form.get("recipe_description"),
                "recipe_serves": request.form.get("recipe_serves"),
                "recipe_steps":  request.form.getlist('recipe_step'),
                "recipe_ingredients": request.form.getlist('recipe_ingredient'),
                "name": session["username"]
            })
    
    return redirect(url_for("account"))
    
@app.route('/delete_recipe')
def delete_recipe():
    # mongo.db.recipes.remove({'_id': ObjectId(id)})
    # return redirect(url_for('account'))
    return "Nothing here yet" 
    # also removes all recipes tied to the account
    
# create and update recipes in the database ends

#Products Page

@app.route('/products')
def products():
    return render_template("products.html")
 
# User functionality begins

@app.route('/login') # formerly 'index' & 'index'
def login():
    if 'username' in session:
        # return 'You are logged in as ' + session['username']
        # flash('Logged in successfully')
        return redirect(url_for('account'))
        
        
    return render_template('login.html')
    
@app.route("/login", methods=["POST"]) # formerly 'index' & 'login'
def login_form():
        
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})
    
    if login_user:
        if bcrypt.check_password_hash(login_user['password'].encode('utf-8'), request.form['password'].encode('utf-8')):
                session['username'] = request.form['username']
                return redirect(url_for('login')) # formerly 'index'
                
        return render_template("error2.html")
    
    return render_template("error2.html")
        
    
@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        
        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
            users.insert({'name' : request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('login')) # formerly 'index'
            
        return render_template("error1.html")
        
    return render_template('register.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
    
@app.route('/account')
def account():
    if 'username' in session:
        user = session['username']
        return render_template('account.html', recipes=mongo.db.recipes.find({ "name": user }))
        
    return "Please login to view your account"
    
@app.route('/settings')
def settings():
    return render_template('settings.html')
    
# User functionality ends

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)