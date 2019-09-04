import os
import math
import pymongo
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
from datetime import date
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# create instance of app in variable 'app'

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['MONGO_DBNAME'] = 'the-online-cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)

today = date.today()

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
    
# search functionality begins

@app.route("/recipe_text_search_results")
def search():
        mongo.db.recipes.create_index([("$**", pymongo.TEXT)])
        
        search_request = request.args.get('search_request')
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.find({'$text': {'$search': str(search_request)}}).count()
        recipes_per_page = 4
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find({ '$text': { '$search': str(search_request)}}, {"score": {"$meta": 'textScore'}}).sort('_id'
            , pymongo.ASCENDING).skip((page - 1) * recipes_per_page).limit(recipes_per_page)
            
        return render_template("recipes.html", recipes=recipes, pages=pages, page=page)

@app.route("/recipes", methods=['GET', 'POST'])
def get_recipes():
    
    filters = []
    if request.method == 'POST':
        if request.form.get("recipe_type") != 'All':
            query = {"recipe_type": request.form.get("recipe_type")}
            filters.append(query)
            
        if request.form.get("meal_type") != "All":
            query2 = {"meal_type": request.form.get("meal_type")}
            filters.append(query2)
          
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.count({'$and': filters})
        recipes_per_page = 4
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find({'$and': filters}).skip((page - 1) * recipes_per_page).limit(recipes_per_page)
        # variable containing string that lists filters used in search
        return render_template("recipes.html", recipes=recipes, pages=pages, page=page)

    else:
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.count()
        recipes_per_page = 4
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find().skip((page - 1) * recipes_per_page).limit(recipes_per_page)
        return render_template("recipes.html", recipes=recipes, pages=pages, page=page)
    
# search functionality ends

@app.route("/discover")
def discover():
    recipes = mongo.db.recipes
    top_recipes = recipes.find().sort("views", -1).limit(3)
    most_recent = recipes.find().sort("date_created", -1).limit(3)
    total = recipes.count()
    return render_template("discover.html", top_recipes=top_recipes, most_recent=most_recent, total=total)
    
@app.route("/recipe/<id>", methods=['GET', 'POST'])
def recipe(id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    # Like option
    # if request.method == "POST":
    #     mongo.db.recipes.update({'_id': ObjectId(id)}, {'$inc': {'likes': int(1)}})
    # Like only once and attach like to user
        
    # recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    if session.get('username') != recipe['name']:
        mongo.db.recipes.update({'_id': ObjectId(id)}, {'$inc': {'views': int(1)}})
    return render_template("recipe.html", recipe=recipe)
    
@app.route("/recipe/<id>/favourite")
def add_favourite(id):
    # mongo.db.users.update(
    #     {"name": session.get('username') }, {"$push": {"favourites": ObjectId(id)}})
    # mongo.db.recipes.update(
    #     {"_id": ObjectId(id)}, {"$inc": {"favourited": 1}})
    user = session["username"]
    mongo.db.recipes.update({ "_id": ObjectId(id)}, {"$push": {"favourited_by": user }})
    return redirect(url_for('recipe', id=id))
    
@app.route("/product/<name>")
def product(name):
    product = mongo.db.products.find_one({"product_name": name})
    return render_template("product.html", product=product)
    
# create and update recipes in the database
    
@app.route("/add_recipe")
def add_recipe():
    if 'username' in session:
        return render_template("addrecipe.html", recipes=mongo.db.recipes.find())
    return "Please login/register to add recipes"
    
@app.route('/insert_recipe', methods=['GET','POST'])
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
                "name": session["username"],
                "recipe_type": request.form.get("recipe_type"),
                "recipe_image": request.form.get("recipe_image"),
                "date_created": today.strftime("%d/%m/%Y"),
                "last_updated": "",
                "tools": request.form.getlist("tool"),
                "diet": request.form.getlist("diet"),
                "views": 0,
                "likes": 0,
                "favourited_by": []
            })
        return redirect(url_for('get_recipes'))
        
@app.route('/edit_recipe/<id>')
def edit_recipe(id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    return render_template("editrecipe.html", recipe=recipe)

@app.route('/update_recipe/<id>', methods=["GET", "POST"])
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
                "name": session["username"],
                "meal_type": request.form.get('meal_type'),
                "recipe_type": request.form.get("recipe_type"),
                "recipe_image": request.form.get("recipe_image"),
                "last_updated": today.strftime("%H:%M:%S, %d/%m/%Y"),
                 "tools": request.form.getlist("tool"),
                "diet": request.form.getlist("diet")
            })
    
    return redirect(url_for("account"))
    
@app.route('/delete_recipe/<id>')
def delete_recipe(id):
    mongo.db.recipes.remove({'_id': ObjectId(id)})
    return redirect(url_for('account'))
    
# create and update recipes in the database ends

#Products Page

@app.route('/products')
def products():
    return render_template("products.html", products=mongo.db.products.find())
 
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
            users.insert({'name' : request.form['username'], 'password': hashpass, 'favourites': []})
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
        
        favourites=mongo.db.recipes.find({"favourited_by": user})
        recipes = mongo.db.recipes.find({ "name": user })
        return render_template('account.html', recipes=recipes, favourites=favourites)
        
    return "Please login to view your account"
    
@app.route('/settings')
def settings():
    return render_template('settings.html')
    
@app.route('/settings/change_pw')
def change_pw():
    return render_template("changepw.html")
    
@app.route('/settings/change_pw', methods=["POST", "GET"])
def change_pw_form():
    
    users = mongo.db.users
    login_user = users.find_one({'name' : session['username']})
    
    if bcrypt.check_password_hash(login_user['password'].encode('utf-8'), request.form['old_password'].encode('utf-8')):
                users.update_one({"name": session["username"]},
                {"$set": {"password": bcrypt.generate_password_hash(request.form['new_password']).decode('utf-8')}})
                return redirect(url_for('account'))
    
    return render_template("error1.html")

@app.route('/settings/delete_account')  
def delete_account():
        return render_template("deleteaccount.html")
    
@app.route('/settings/delete_account', methods=["POST", "GET"])
def delete_account_form():
    
    users = mongo.db.users
    recipes = mongo.db.recipes
    username = session['username']
    login_user = users.find_one({'name' : username })
    
    if bcrypt.check_password_hash(login_user['password'].encode('utf-8'), request.form['password'].encode('utf-8')):
        recipes.remove({"name": username})
        session.clear()
        users.remove({"name": username})
        # remove favourites
        return redirect(url_for('home'))

    return render_template('error1.html')
    

# User functionality ends

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def something_wrong(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)