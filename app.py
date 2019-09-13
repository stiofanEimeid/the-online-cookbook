import os
import math
import pymongo
import json
from flask import Flask, render_template, redirect, request, url_for, session, flash, jsonify
from flask_bcrypt import Bcrypt
from time import gmtime, strftime  
from flask_pymongo import PyMongo, pymongo
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
    
# search functionality begins

@app.route("/recipe_text_search_results")
def search():
        mongo.db.recipes.create_index([("$**", pymongo.TEXT)])
        
        search_request = request.args.get('search_request')
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.find({'$text': {'$search': str(search_request)}}).count()
        recipes_per_page = 12
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
            
        if request.form.get("diet") != "None":
            query3 = {"diet": { "$all": [request.form.get("diet")] }}
            filters.append(query3)
            
        if filters != []:
            search_request = {'$and': filters}
        else: 
            search_request = {}
            
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.count(search_request)
        recipes_per_page = 12
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find(search_request).skip((page - 1) * recipes_per_page).limit(recipes_per_page)
        # variable containing string that lists filters used in search
        return render_template("recipes.html", recipes=recipes, pages=pages, page=page)

    else:
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.count()
        recipes_per_page = 12
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find().skip((page - 1) * recipes_per_page).limit(recipes_per_page)
        return render_template("recipes.html", recipes=recipes, pages=pages, page=page)
    
# search functionality ends

@app.route("/discover")
def discover():
    recipes = mongo.db.recipes
    users = mongo.db.users
    top_recipes = recipes.find().sort("views", -1).limit(3)
    most_recent = recipes.find().sort("time_created", -1).limit(3)
    most_favourited = recipes.find().sort("favourites", -1 ).limit(3)
    recipe_total = recipes.count()
    user_total = users.count()
    return render_template("discover.html", top_recipes=top_recipes, most_recent=most_recent, recipe_total=recipe_total, most_favourited=most_favourited, user_total=user_total)
 


@app.route("/data")
def data():
    mexican = mongo.db.recipes.find({"recipe_type": "Mexican"}).count()
    italian = mongo.db.recipes.find({"recipe_type": "Italian"}).count()
    other = mongo.db.recipes.find({"recipe_type": "Other"}).count()
    
    
    mexican2 = list(mongo.db.recipes.find({"recipe_type": "Mexican"}, {"views": 1, "_id":0}))
    italian2 = list(mongo.db.recipes.find({"recipe_type": "Italian"}, {"views": 1, "_id":0}))
    other2 = list(mongo.db.recipes.find({"recipe_type": "Other"}, {"views": 1, "_id":0}))
    
    total_mexican = 0
    for i in range(len(mexican2)):
        total_mexican += mexican2[i]["views"]
        
    total_italian = 0
    for i in range(len(italian2)):
        total_italian += italian2[i]["views"]
    
    total_other = 0 
    for i in range(len(other2)):
        total_other += other2[i]["views"]
    # return jsonify([{ "Mexican": mexican, "Italian": italian, "Other": other
    #         }])
    #Passes a json object that may be rendered by the d3 function in main.js
    myData = json.dumps([{"Type": "Mexican", "Amount": mexican, "Views": total_mexican }, {"Type": "Italian", "Amount": italian, "Views": total_italian }, {"Type": "Other", "Amount": other, "Views": total_other }])
    return myData
    

# @app.route("/data2")
# def data2():
#     mexican2 = list(mongo.db.recipes.find({"recipe_type": "Mexican"}, {"views": 1, "_id":0}))
#     italian2 = list(mongo.db.recipes.find({"recipe_type": "Italian"}, {"views": 1, "_id":0}))
#     other2 = list(mongo.db.recipes.find({"recipe_type": "Other"}, {"views": 1, "_id":0}))
    
#     total_mexican = 0
#     for i in range(len(mexican2)):
#         total_mexican += mexican2[i]["views"]
        
#     total_italian = 0
#     for i in range(len(italian2)):
#         total_italian += italian2[i]["views"]
    
#     total_other = 0 
#     for i in range(len(other2)):
#         total_other += other2[i]["views"]

    
#     myData = json.dumps([{"Type": "Mexican", "Views": total_mexican }, {"Type": "Italian", "Views": total_italian }, {"Type": "Other", "Views": total_other }])
#     return myData
    
# View a recipe
        
@app.route("/recipe/<id>", methods=['GET', 'POST'])
def recipe(id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    products = mongo.db.products.aggregate([ { "$sample": { "size": 3 } } ])
   
    if session.get('username') != recipe['name']:
        mongo.db.recipes.update({'_id': ObjectId(id)}, {'$inc': {'views': int(1)}})
    
    return render_template("recipe.html", recipe=recipe, products=products)

# Add and remove favourites 
@app.route("/recipe/<id>/favourite")
def add_favourite(id):
    # mongo.db.users.update(
    #     {"name": session.get('username') }, {"$push": {"favourites": ObjectId(id)}})
    # mongo.db.recipes.update(
    #     {"_id": ObjectId(id)}, {"$inc": {"favourited": 1}})
    user = session["username"]
    mongo.db.recipes.update({ "_id": ObjectId(id)}, {"$push": {"favourited_by": user }})
    mongo.db.recipes.update({'_id': ObjectId(id)}, {'$inc': {'favourites': int(1)}})
    return redirect(url_for('recipe', id=id))
    
@app.route("/recipe/<id>/remove_favourite")
def remove_favourite(id):
    user = session["username"]
    mongo.db.recipes.update({ "_id": ObjectId(id)}, {"$pull": {"favourited_by": user }})
    mongo.db.recipes.update({'_id': ObjectId(id)}, {'$inc': {'favourites': int(-1)}})
    return redirect(url_for('recipe', id=id))

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
                "time_created": strftime("%H:%M:%S %Y-%m-%d", gmtime()),
                "last_updated": "",
                "diet": request.form.getlist("diet"),
                "views": 0,
                "favourites": 0,
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
                "last_updated": strftime("%H:%M:%S %Y-%m-%d", gmtime()),
                "diet": request.form.getlist("diet")
            })
    
    return redirect(url_for("account"))
    
@app.route('/delete_recipe/<id>')
def delete_recipe(id):
    mongo.db.recipes.remove({'_id': ObjectId(id)})
    return redirect(url_for('account'))
    
# create and update recipes in the database ends

#Products Pages

@app.route('/products')
def products():
    return render_template("products.html", products=mongo.db.products.find())

@app.route("/product/<name>")
def product(name):
    product = mongo.db.products.find_one({"product_name": name})
    return render_template("product.html", product=product)
    
# Login/Registration functionality begins

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
            avatar = request.form.get("avatar")
            users.insert({'name' : request.form['username'], 'password': hashpass, 'favourites': [], 'avatar': avatar, "member_since": strftime("%H:%M:%S %Y-%m-%d", gmtime())})
            session['username'] = request.form['username']
            return redirect(url_for('login')) # formerly 'index'
            
        return render_template("error1.html")
        
    return render_template('register.html')
    
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))
    
# Account and account settings
    
@app.route('/account')
def account():
    if 'username' in session:
        user = session['username']
        
        favourites=mongo.db.recipes.find({"favourited_by": user})
        recipes = mongo.db.recipes.find({ "name": user })
        profile = mongo.db.users.find_one({"name": user})
        return render_template('account.html', recipes=recipes, favourites=favourites, profile=profile)
        
    return "Please login to view your account"
   
   
@app.route('/change_avatar') 
def change_avatar():
    return render_template("changeavatar.html")
    
@app.route('/change_avatar', methods=["POST"])
def change_avatar_form():
    users = mongo.db.users
    users.update_one({"name": session["username"]},
    {"$set": {'avatar': request.form.get("avatar")}}
    );
    return redirect(url_for('account'))
    
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