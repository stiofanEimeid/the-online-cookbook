import os
import math
import pymongo
import json
from flask import (Flask, render_template, redirect, request, url_for, session,
                   flash, jsonify)
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
        '''
        The wildcard index using the parameter $"" allows users to search for
        any value in the form of text in a recipe document.
        '''
        mongo.db.recipes.create_index([("$**", pymongo.TEXT)])
        search_request = request.args.get('search_request')
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.find(
            {'$text': {'$search': str(search_request)}}).count()
        '''
        The number twelve was chosen in the interest of symmetrical
        responsiveness.On small screens each row will contain 1 recipe, for
        medium screens 3 recipes and finally for large screens 4 recipes. Each
        of these numbers divides evenlyinto 12 and so each full page of results
        will fill the container on each screen size.
        '''
        recipes_per_page = 12
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find({'$text': {'$search': str(
                                        search_request)}}, {"score":
                                        {"$meta": 'textScore'}}
                                        ).sort('_id', pymongo.ASCENDING
                                               ).skip((page - 1) *
                                                      recipes_per_page
                                                      ).limit(recipes_per_page)
        recipes_count = recipes.count()
        '''
        For use in the counter displaying the number of search results on the
        currently selected page in the recipes template. The results per page
        will always be 12 until the last page (or the first page if there are
        less than twelve results). In that case, the top-end number x (e.g.
        showing 13 - x of x recipes ), will be the total number of recipes
        rather than the page number multiplied by 12.
        '''
        display_result = (
                        recipes_count if recipes_count <
                        page * recipes_per_page
                        else page * recipes_per_page)
        return render_template("recipes.html", recipes=recipes, pages=pages,
                               page=page, recipes_count=recipes_count,
                               display_result=display_result)


@app.route("/recipes", methods=['GET', 'POST'])
def get_recipes():
    filters = []
    if request.method == 'POST':
        '''
        Gather each form input if the user has selected an option and append
        it to a list.
        '''
        if request.form.get("recipe_type") != 'All':
            query = {"recipe_type": request.form.get("recipe_type")}
            filters.append(query)
        if request.form.get("meal_type") != "All":
            query2 = {"meal_type": request.form.get("meal_type")}
            filters.append(query2)
        if request.form.get("diet") != "None":
            query3 = {"diet": {"$all": [request.form.get("diet")]}}
            filters.append(query3)
        if filters != []:
            search_request = {'$and': filters}
        else:
            search_request = {}
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.count(search_request)
        recipes_per_page = 12
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        # The list becomes the search query
        recipes = mongo.db.recipes.find(
            search_request).skip((page - 1) * recipes_per_page).limit(
                recipes_per_page)
        recipes_count = recipes.count()
        display_result = (
                         recipes_count if recipes_count <
                         page * recipes_per_page
                         else page * recipes_per_page)
        return render_template("recipes.html", recipes=recipes, pages=pages,
                               page=page, recipes_count=recipes_count,
                               display_result=display_result)

    else:
        # Return all recipes if no options have been selected
        page = int(request.args.get('page', 1))
        all_recipes = mongo.db.recipes.count()
        recipes_per_page = 12
        pages = range(1, int(math.ceil(all_recipes / recipes_per_page)) + 1)
        recipes = mongo.db.recipes.find(
            ).skip((page - 1) * recipes_per_page).limit(recipes_per_page)
        recipes_count = recipes.count()
        display_result = (
                        recipes_count if recipes_count <
                        page * recipes_per_page
                        else page * recipes_per_page)
        return render_template("recipes.html", recipes=recipes, pages=pages,
                               page=page, recipes_count=recipes_count,
                               display_result=display_result)
# search functionality ends


@app.route("/discover")
def discover():
    recipes = mongo.db.recipes
    users = mongo.db.users
    top_recipe = recipes.find().sort("views", -1).limit(1)
    top_recipes = recipes.find().sort("views", -1).limit(5)
    most_recent = recipes.find().sort("time_created", -1).limit(5)
    top_favourite = recipes.find().sort("favourites", -1).limit(1)
    most_favourited = recipes.find().sort("favourites", -1).limit(5)
    recipe_total = recipes.count()
    user_total = users.count()
    return render_template("discover.html", top_recipes=top_recipes,
                           top_recipe=top_recipe, most_recent=most_recent,
                           recipe_total=recipe_total,
                           top_favourite=top_favourite,
                           most_favourited=most_favourited,
                           user_total=user_total)


@app.route("/data")
def data():
    # Retrieve the amount of recipes submitted pertaining to a given continent
    south_america = mongo.db.recipes.find({"recipe_type": "Mexican"}).count()
    europe = mongo.db.recipes.find({'$or': [{"recipe_type": "Italian"},
                                            {"recipe_type": "UK"},
                                            {"recipe_type": "Spanish"},
                                            {"recipe_type": "Irish"},
                                            {"recipe_type": "French"}
                                            ]}).count()
    asia = mongo.db.recipes.find({'$or': [{"recipe_type": "Thai"},
                                          {"recipe_type": "Japanese"},
                                          {"recipe_type": "Chinese"},
                                          {"recipe_type": "Indian"}
                                          ]}).count()
    north_america = mongo.db.recipes.find({"recipe_type": "American"}).count()
    africa = mongo.db.recipes.find({"recipe_type": "African"}).count()
    other = mongo.db.recipes.find({"recipe_type": "Other"}).count()
    '''
    Determine the total number of views contained in each group and convert
    the cursor to a list.
    '''
    south_america2 = list(mongo.db.recipes.find({"recipe_type": "Mexican"},
                                                {"views": 1, "_id": 0}))
    europe2 = list(mongo.db.recipes.find({'$or': [{"recipe_type": "Italian"},
                                                  {"recipe_type": "UK"},
                                                  {"recipe_type": "Spanish"},
                                                  {"recipe_type": "Irish"},
                                                  {"recipe_type": "French"}
                                                  ]}, {"views": 1, "_id": 0}))
    asia2 = list(mongo.db.recipes.find({'$or': [{"recipe_type": "Thai"},
                                                {"recipe_type": "Japanese"},
                                                {"recipe_type": "Chinese"},
                                                {"recipe_type": "Indian"}
                                                ]}, {"views": 1, "_id": 0}))
    north_america2 = list(mongo.db.recipes.find({"recipe_type": "American"},
                                                {"views": 1, "_id": 0}))
    africa2 = list(mongo.db.recipes.find({"recipe_type": "African"},
                                         {"views": 1, "_id": 0}))
    other2 = list(mongo.db.recipes.find({"recipe_type": "Other"},
                                        {"views": 1, "_id": 0}))
    # Iterate through the lists and return the total number of views
    total_south_america = 0
    for i in range(len(south_america2)):
        total_south_america += south_america2[i]["views"]
    total_asia = 0
    for i in range(len(asia2)):
        total_asia += asia2[i]["views"]
    total_north_america = 0
    for i in range(len(north_america2)):
        total_north_america += north_america2[i]["views"]
    total_europe = 0
    for i in range(len(europe2)):
        total_europe += europe2[i]["views"]
    total_africa = 0
    for i in range(len(africa2)):
        total_africa += africa2[i]["views"]
    total_other = 0
    for i in range(len(other2)):
        total_other += other2[i]["views"]
    '''
    Determine the total number of favourites contained in each group and
    convert the cursor to a list.
    '''
    south_america3 = list(mongo.db.recipes.find({"recipe_type": "Mexican"},
                                                {"favourites": 1, "_id": 0}))
    europe3 = list(mongo.db.recipes.find({'$or': [{"recipe_type": "Italian"},
                                                  {"recipe_type": "UK"},
                                                  {"recipe_type": "Spanish"},
                                                  {"recipe_type": "Irish"},
                                                  {"recipe_type": "French"}
                                                  ]}, {"favourites": 1,
                                                       "_id": 0}))
    asia3 = list(mongo.db.recipes.find({'$or': [{"recipe_type": "Thai"},
                                                {"recipe_type": "Japanese"},
                                                {"recipe_type": "Chinese"},
                                                {"recipe_type": "Indian"}
                                                ]}, {"favourites": 1,
                                                     "_id": 0}))
    north_america3 = list(mongo.db.recipes.find({"recipe_type": "American"},
                                                {"favourites": 1, "_id": 0}))
    africa3 = list(mongo.db.recipes.find({"recipe_type": "African"},
                                         {"favourites": 1, "_id": 0}))
    other3 = list(mongo.db.recipes.find({"recipe_type": "Other"},
                                        {"favourites": 1, "_id": 0}))
    # Iterate through the lists and return the total number of favourites
    total_south_america2 = 0
    for i in range(len(south_america3)):
        total_south_america2 += south_america3[i]["favourites"]
    total_europe2 = 0
    for i in range(len(europe3)):
        total_europe2 += europe3[i]["favourites"]
    total_africa2 = 0
    for i in range(len(africa3)):
        total_africa2 += africa3[i]["favourites"]
    total_north_america2 = 0
    for i in range(len(north_america3)):
        total_north_america2 += north_america3[i]["favourites"]
    total_asia2 = 0
    for i in range(len(asia3)):
        total_asia2 += asia3[i]["favourites"]
    total_other2 = 0
    for i in range(len(other3)):
        total_other2 += other3[i]["favourites"]
    '''
    The myData variable creates a json object containing the data that may be
    rendered by the d3 function in main.js
    '''
    myData = json.dumps([{"Type": "South American", "Amount": south_america,
                         "Views": total_south_america, "Favourites":
                          total_south_america2},
                         {"Type": "North American", "Amount": north_america,
                         "Views": total_north_america, "Favourites":
                          total_north_america2},
                         {"Type": "European", "Amount": europe, "Views":
                         total_europe,
                         "Favourites": total_europe2},
                         {"Type": "Asian", "Amount": asia, "Views": total_asia,
                         "Favourites": total_asia2},
                         {"Type": "African", "Amount": africa,
                          "Views": total_africa, "Favourites": total_africa2},
                         {"Type": "Other",
                          "Amount": other, "Views": total_other, "Favourites":
                          total_other2}
                         ])
    return myData
# View a recipe


@app.route("/recipe/<id>", methods=['GET', 'POST'])
def recipe(id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    '''
    A random set of three of nine products are shown with title, link and image
    respectivaly at the end of the page in the interest of promoting Apéritif's
    line of kitchenware.
    '''
    products = mongo.db.products.aggregate([{"$sample": {"size": 3}}])
    '''
    Only views by users other than the author contribute towards the recipe
    count
    '''
    if session.get('username') != recipe['author']:
        mongo.db.recipes.update({'_id': ObjectId(id)},
                                {'$inc': {'views': int(1)}})
    return render_template("recipe.html", recipe=recipe, products=products)


@app.route("/recipe/<id>/favourite")
def add_favourite(id):
    user = session["username"]
    mongo.db.recipes.update({"_id": ObjectId(id)},
                            {"$push": {"favourited_by": user}})
    mongo.db.recipes.update({'_id': ObjectId(id)},
                            {'$inc': {'favourites': int(1)}})
    return redirect(url_for('recipe', id=id))


@app.route("/recipe/<id>/remove_favourite")
def remove_favourite(id):
    user = session["username"]
    mongo.db.recipes.update({"_id": ObjectId(id)},
                            {"$pull": {"favourited_by": user}})
    mongo.db.recipes.update({'_id': ObjectId(id)},
                            {'$inc': {'favourites': int(-1)}})
    return redirect(url_for('recipe', id=id))

'''
Create and update recipes in the database.
'''


@app.route("/add_recipe")
def add_recipe():
    # Only logged in users may add recipes
    if 'username' in session:
        return render_template("addrecipe.html",
                               recipes=mongo.db.recipes.find())
    error_message = "You must be logged in to add recipes."
    return render_template("error.html", error_message=error_message)


@app.route('/insert_recipe', methods=['GET', 'POST'])
def insert_recipe():
        recipes = mongo.db.recipes
        recipes.insert_one(
            {
                "recipe_name": request.form.get("recipe_name"),
                "recipe_preptime": request.form.get("recipe_preptime"),
                "recipe_cooktime": request.form.get("recipe_cooktime"),
                "recipe_description": request.form.get("recipe_description"),
                "recipe_serves": request.form.get("recipe_serves"),
                "recipe_steps":  request.form.getlist('recipe_step'),
                "recipe_ingredients": request.form.getlist(
                    'recipe_ingredient'),
                "meal_type": request.form.get('meal_type'),
                "recipe_type": request.form.get("recipe_type"),
                "author": session['username'],
                "recipe_image": request.form.get("recipe_image"),
                "time_created": strftime("%H:%M:%S %d-%m-%Y", gmtime()),
                "last_updated": "",
                "diet": request.form.getlist("diet"),
                "views": 0,
                "favourites": 0,
                "favourited_by": []
            })
        return redirect(url_for('get_recipes'))


@app.route('/edit_recipe/<id>')
def edit_recipe(id):
    '''
    Only logged in users may edit recipes, specifically recipes that were
    authored by them.
    '''
    if 'username' in session:
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
        user = session['username']
        if recipe["author"] == user:
            return render_template("editrecipe.html", recipe=recipe)
        else:
            error_message = "Denied: You may only edit your own recipes."
            return render_template("error.html", error_message=error_message)
    else:
        error_message = "You must be logged in to edit your recipes."
        return render_template("error.html", error_message=error_message)


@app.route('/update_recipe/<id>', methods=["GET", "POST"])
def update_recipe(id):
    recipes = mongo.db.recipes
    if request.method == 'POST':
        recipes.update({'_id': ObjectId(id)},
                       {"$set":
                       {
                        "recipe_name": request.form.get("recipe_name"),
                        "recipe_preptime": request.form.get("recipe_preptime"),
                        "recipe_cooktime": request.form.get("recipe_cooktime"),
                        "recipe_description": request.form.get(
                            "recipe_description"),
                        "recipe_serves": request.form.get("recipe_serves"),
                        "recipe_steps":  request.form.getlist('recipe_step'),
                        "recipe_ingredients": request.form.getlist(
                            'recipe_ingredient'),
                        "meal_type": request.form.get('meal_type'),
                        "recipe_type": request.form.get("recipe_type"),
                        "recipe_image": request.form.get("recipe_image"),
                        "last_updated": strftime(
                            "%H:%M:%S %d-%m-%Y", gmtime()),
                        "diet": request.form.getlist("diet")
                        }
                        })
        return redirect(url_for("recipe", id=id))


@app.route('/delete_recipe/<id>')
def delete_recipe(id):
    '''
    Only logged in users may delete recipes, specifically recipes that were
    authored by them.
    '''
    if 'username' in session:
        user = session['username']
        recipe = mongo.db.recipes.find_one({"_id": ObjectId(id)})
        if recipe["author"] == user:
            mongo.db.recipes.remove({'_id': ObjectId(id)})
            return redirect(url_for('account'))
        else:
            error_message = "Error: You may only delete your own recipes."
            return render_template("error.html", error_message=error_message)
    else:
        error_message = "You must be logged in to delete your recipes."
        return render_template("error.html", error_message=error_message)

# Create and update recipes in the database ends

# Products Pages


@app.route('/products')
def products():
    return render_template("products.html", products=mongo.db.products.find())


@app.route("/product/<name>")
def product(name):
    product = mongo.db.products.find_one({"product_name": name})
    return render_template("product.html", product=product)

# Login/Registration functionality begins


@app.route('/login')
def login():
    if 'username' in session:
        return redirect(url_for('account'))
    return render_template('login.html')


@app.route("/login", methods=["POST"])
def login_form():
    users = mongo.db.users
    '''
    # Username is case insensitive by checking lowercase name value created at
    registration
    '''
    login_user = users.find_one(
        {'name_lowercase': request.form['username'].lower()})
    if login_user:
        if bcrypt.check_password_hash(login_user['password'].encode('utf-8'),
                                      request.form['password'].encode(
                                      'utf-8')):
                # Session username is set to username chosen at registration
                session['username'] = login_user['name']
                return redirect(url_for('login'))
        else:
            '''
            The user is not told whether the username or password or both were
            incorrect in the interest of security.
            '''
            error_message = "Invalid username/password combination."
            return render_template('error2.html', error_message=error_message)
    else:
        '''
        Again, the user is not told whether the username or password or both
        were incorrect.
        '''
        error_message = "Invalid username/password combination."
        return render_template('error2.html', error_message=error_message)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        users = mongo.db.users
        '''
         When creating a new username a cross-check of the chosen name in
         lowercase is run against usernames already in the database also
         rendered in lowercase to prevent duplicates, whereby users may share
         the same name save for case changes.
         '''
        existing_user = users.find_one(
            {'name_lowercase': request.form['username'].lower()})
        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(request.form['password']
                                                     ).decode('utf-8')
            avatar = request.form.get("avatar")
            '''
            Lowercase version of the username chosen is also created to make
            user's attempts to login case insensitive with regard to usernames.
            '''
            users.insert({'name': request.form['username'],
                          'name_lowercase': request.form['username'].lower(),
                          'password': hashpass, 'favourites': [],
                          'avatar': avatar,
                          "member_since": strftime("%d-%m-%Y", gmtime())})

            # session username is set to chosen username
            session['username'] = request.form['username']

            return redirect(url_for('login'))

        else:
            error_message = "That username already exists."
            return render_template("error.html", error_message=error_message)

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# Account and account settings


@app.route('/account')
def account():
    '''
    Only logged in users may view the account page, based on session username.
    '''
    if 'username' in session:
        user = session['username']
        favourites = mongo.db.recipes.find({"favourited_by": user})
        recipes = mongo.db.recipes.find({"author": user})
        recipe_count = recipes.count()
        profile = mongo.db.users.find_one({"name": user})
        return render_template('account.html', recipes=recipes,
                               recipe_count=recipe_count,
                               favourites=favourites, profile=profile)
    else:
        error_message = "Users must log in to view their account."
        return render_template("error.html", error_message=error_message)


@app.route('/change_avatar')
def change_avatar():
    # Only logged in users may view account settings.
    if 'username' in session:
        return render_template("changeavatar.html")
    else:
        error_message = "Users must log in to view account settings."
        return render_template("error.html", error_message=error_message)


@app.route('/settings/change_avatar', methods=["POST"])
def change_avatar_form():
    # Only logged in users may view account settings.
    users = mongo.db.users
    users.update_one({"name": session["username"]},
                     {"$set": {'avatar': request.form.get("avatar")}}
                     )
    return redirect(url_for('account'))


@app.route('/settings/change_pw')
def change_pw():
    # Only logged in users may view account settings.
    if 'username' in session:
        return render_template("changepw.html")
    else:
        error_message = "Users must log in to view account settings. "
        return render_template("error.html", error_message=error_message)


@app.route('/settings/change_pw', methods=["POST", "GET"])
def change_pw_form():
    users = mongo.db.users
    login_user = users.find_one({'name': session['username']})
    '''
    Users must enter their old password before creating a new password for an
    extra layer of security.
    '''
    if bcrypt.check_password_hash(login_user['password'].encode('utf-8'), request.form['old_password'].encode('utf-8')):
                users.update_one({"name": session["username"]},
                {"$set": {"password": bcrypt.generate_password_hash(request.form['new_password']).decode('utf-8')}})
                return redirect(url_for('account'))
    else:
        error_message = "Your old password is incorrect."
        return render_template('error2.html', error_message=error_message)


@app.route('/settings/delete_account')
def delete_account():
    # Only logged in users may view account settings.
    if 'username' in session:
        return render_template("deleteaccount.html")
    else:
        error_message = "Users must log in to view account settings."
        return render_template("error.html", error_message=error_message)


@app.route('/settings/delete_account', methods=["POST", "GET"])
def delete_account_form():
    users = mongo.db.users
    recipes = mongo.db.recipes
    username = session['username']
    login_user = users.find_one({'name': username})
    '''
    Users must enter their old password before creating a new password for an
    extra layer of security.
    '''
    if bcrypt.check_password_hash(login_user['password'].encode('utf-8'), request.form['password'].encode('utf-8')):
        recipes.remove({"name": username})
        session.clear()
        users.remove({"name": username})

        return redirect(url_for('home'))
    else:
        error_message = "Your password is incorrect."
        return render_template('error2.html', error_message=error_message)

# User functionality ends


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def something_went_wrong(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
