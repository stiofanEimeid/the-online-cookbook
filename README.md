<h1 align="center">

<a href="https://the-online-cookbook.herokuapp.com/" target="_blank" rel="noopener"><img src="https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/intro_logo.png" alt="Apéritif: The Online Cookbook Logo"/></a>

</h1>

<div align="center">

[Visit the site](https://the-online-cookbook.herokuapp.com/)

</div>

# Stephen Byrne Portfolio

Stream Three Project: Data-Centric Development - Code Institute 

Apéritif: The Online Cookbook allows users to search recipes and add their own in a quick and easy manner. A live version of the site may be found here: [https://the-online-cookbook.herokuapp.com/](https://the-online-cookbook.herokuapp.com/).

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Goals**](#player-goals)
    - [**User Stories**](#user-stories)
    - [**Design Choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Demo**](#demo)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Data Structure**](#datastructure)

4. [**Technologies**](#technologies)

5. [**Testing**](#testing)

6. [**Deployment**](#deployment)
    - [**How to Run Code Locally**](#how-to-run-locally)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

## UX

#### Project Goals

The goal of this project is to build a database that allows users to carry out each CRUD operation: Creating, Reading, Updating and Deleting recipes. Although authentification is not expected I have included login functionality and user accounts in order to keep user recipes secure. 

#### User Goals

The target audience of the application are those who are relatively new to cooking and are curious about learning how to make new dishes. In addition, it hopes to attract those who are already passionate about cooking to share some of their favourite recipes with other users. Ideally, these groups would join together to create a thriving online community, one that is bound together by a love of cooking and learning more about it. 

Users seek the means to find a variety of recipes through an accessible interface that is easy to use. Frequent users or those with extensive experience in cooking may seek to add their recipes to the website to share with others as well as discover more recipes. 

Aperitif is easy to use and visusally appealling. Filters help users find specific recipes quickly and easily. Unique recipe pages give users all the information they need in an effective manner... With an account, users may add and edit recipes as well as keep track of their favourite recipes. The product section of recipe pages provide additional information to give user's the best cooking experience possible.

#### User Stories

As a user, I want to find and share recipes. I want to be able to create an account that is secure and keeps track of the recipes I create, allowing me to update them and delete them as I please. 

As a site owner, I want to promote a brand of cooking tools to my users. 

### Design Choices

**Fonts**

The Lobster font was chosen for its vibrancy and energy in contrast to the nunito font to make important titles jump out to the user while complimenting aperitif's brand identity.

The Nunito style was chosen for its sharpness and clarity to help convey a significant amount of information clearly. 

Both fonts were sourced from GoogleFonts. 

**Icons**

Icons have been sourced from FontAwesome to help convey essential characteristics about recipes to users in an intuitive manner.

**Colours**

The main colour scheme of the site consisted of yellow(#f3d250), blue(#90CCF4) and red(f78888), white(#fafafa) and grey(#ececec).

**Styling**

The recipe pages are intended to convey essential information about a particular recipe in an intuitive and effective manner. This intent informs the design process. Recipe pages are intended to be uncluttered. The largest groups of information, steps and ingredients, are contained in tabs that the user may switch between, preventing the user from being bombared with large amounts of text and keeping page space free from everything but the most relevant information at any one time.

**Logo**

The logo is a cartoon ape in a chef's hat, the ape in aperifif if you will. The imagery of the site is intended to be light-hearted and fun in order to make cooking accessible for those who are less confident in their cooking abilities. More generally, the imagery is intended to illustrate that this a site for those who are passionate about cooking but one that doesn't take itself too seriously. 

**The Wheel**

The background consists of two wheels of food with the logo at the center, slowly revolving. The wheels are made up of images of food and cooking utensils. Both of these comprise the content being delivered to the user, recipes which they can search and add to along with kitchen products to help bring these recipes to life. 

Designed in SVG. 3 different wheels layered one on top of the other. 

In addition, the wheels are meant to arrest the viewers attention and convey a sense of individuality about the site. It speaks to the vast array of possiblities in the world of cooking. 

Visual Consistency

**Demo**

<img src="https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/atoc_demo.png" alt="Apéritif: The Online Cookbook Logo Displayed on Different Screen Sizes"/>


### Wireframes

* [Home Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Home%20page.png)
* [Registration Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Registration%20Page.png)
* [Login Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Login.png)
* [Account Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Account%20Page.png)
* [Add/Edit Recipe Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Add_Edit%20Recipe.png)
* [Recipe Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Recipe%20Page.png)
* [Recipe Search Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Search%20Results.png)
* [Product Search Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Product%20Search.png)
* [Product Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Product%20Page.png)
* [Statistics Page](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/wireframes/Discover.png)

## Features

### Access

Users may register an account and login to same through dedicated templates. Passwords are encrypted using bcrypt to ensure account integrity and prevent access to the account from anyone but the user. 

Registering or logging in successfully brings users to their account page where they may follow a link to the add recipe page, see their added recipes and recipes they have favourited. Settings include changing their password or deleting their account altogether. Users are cautioned that deleting their account will remove all the content they have created for the site and that the process is irreversible. 
Finally, they may logout from this page. 

### Read

Users may search or 'read' recipes contained in the database. They can define special criteria for their search using the filters provided, including meal origin(mexican, indian, italian, chinese etc), meal type(breakfast, lunch, dinner or snack), and diet type(vegetarian, vegan, dairy-free, gluten-free and nut-free). Search results are paginated with 8 results max for small screens and 12 for larger screens. Clicking on each result's respective "Go to Recipe" button brings users to a dedicated recipe page. 

Recipe pages provide essential information about a recipe, an image of the recipe and links to pages of products that may help when following the recipe. 

### Edit, Add and Delete Recipes

Registered users may add recipes, update these recipes and finally delete the recipes. The add recipe and edit recipe pages consist of forms with spaces for essential information that will be displayed in individual recipe pages. registered users may dynamically add steps or ingredients up to a maximum of fifteen in each case. If users choose not to attach an image of the recipe to the form, a placeholder image will appear when the recipe's page is selected. 

When registered users are taken to the page of a recipe they have created, they are given the option to update or delete the recipe. The user is asked to confirm their decision to remove their recipe if they click on the delete button - first, to encourage users to think twice about removing their recipe and secondly to prevent frustation for users who may click the button accidentally. If the user visits a recipe page that is not of their own creation, they are instead given the option of adding the recipe to their favourites. Favourites are vieweable from their account page and may be removed at any time if they see fit. 

Users may search products on the product page. They are not given the option to add their own. 

### Discover

The discover page provides some statistics about the site, including most viewed recipes, most liked recipes, the proportion of recipes to users, and most popular categories of recipes. 


### Existing Features

If they so wish, users may register an account with the site that displays all the recipes they create.



Users may search the recipes collection using a collection of filters whether they are registered or not. The filters are based on meal time and meal type.  

Users who have registered with the site may submit their own recipes to be viewed by other users. They may also update the recipe or even delete it. Naturally, each user will only be able to edit and delete recipes they themselves have submitted.

The discover page displays a number of statistics about the site such as most viewed recipes.

A product page displays products relevant to recipes submitted to the site. During the submission and editing processes of recipes, users may identify kitchen appliances and utensils from a list on each of the pages. Links to each product are then found on the recipe page. 

### Features left to implement 

A forum for users to discuss cooking content / add comments to recipes

Should users forget their password, I would like to give them the option of creating a new one. As authetification was understood by me not to be a focus of the project, this feature was left to be implemented in the future. 

Checkout functionality

## Data Structure

I choose to use MongoDB, a 'NoSQl' database, in order to implement the knowledge I'd accrued from the module mini-project. In addition, I was aware the next milestone project would involve using a SQL. As such, this was my only opportunity to work with a NoSQL database for a milestone project. Suitability?

The recipe collection and user collection share a common key-value pair, "username", which links the two collections. The recipe entry takes the username of the user who created it. Each recipe can only have one creator and may therefore be described as a one-to-one relationship between each recipe and the user who created it. However, a user can have many recipes attributed to them.  As such, a one-to-many relationship exists between the user and the recipes created by them. 

### Recipe Collection

Title | DB Key | Data type 
--- | --- | --- 
Recipe ID | _id | Object ID 
Name | recipe_name | String 
Preparation Time | recipe_preptime | Integer32
Serves | recipe_serves | Integer32
Ingredients | receipe_ingredients | Array 
Steps | recipe_steps | Array 
Dietary Requirements | diet | Array
Description | recipe_description | String 
Author| author | String
Image | recipe_image | String
Views | views | Integer32
Favourites | favourites | Integer32
Favourited By | favourited-by | Array
Time Created | time_created | String
Last Updated | last_updated | String

### User Collection

Title | DB Key | Data Type 
--- | --- | --- 
User ID | _id | Object ID
Username | name | String
Lowercase username | name_lowercase | String
Password | user_pw | String
Favourites | favourites | Array
Avatar | avatar | String
Member Since | member_since | String

### Product Collection

Title | DB Key | Data Type 
--- | --- | --- 
Product ID | _id | Object ID 
Product Name | product_name | String
Product Image | product_image | String
Product Description | product_description | String
Product Price | product_price | String

## Technologies Used

- This project uses HTML, CSS, JavaScript and Python programming languages.
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [Cloud9](https://c9.io) 
    - Developer used **Cloud9** for their IDE while building the website.
- [Bootstrap](https://www.bootstrapcdn.com/)
    - The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.
    - The project also uses Bootstrap to provide icons from [FontAwesome](https://www.bootstrapcdn.com/fontawesome/)
- [GitHub](https://github.com/)
    - This project uses **GitHub** to store and share all project code remotely. 
- [Heroku](https://www.heroku.com/)
    - The application is hosted on **Heroku**.
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
    - **Jinja** was used to create templates
- [FontAwesome](https://fontawesome.com/)
    - **FontAwesome** was used to provide icons for the side-navigation bar. 
- [GoogleFonts](https://fonts.google.com/)
    - The Lobster and Nunito fonts found on **GoogleFonts** were used for this project. 
- [Git](https://git-scm.com/)
    - Was used to handle version control
- [Am I Responsive Design](http://ami.responsivedesign.is/)
    - **Am I Reponsive Design** was used to test the responsiveness of the site and to provide the [image of the site running
    on all devices](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/atoc_demo.png) contained in this README.md
- [PIP](https://pip.pypa.io/en/stable/installing/)
    - **PIP** was used to install the necessary software packages for this project. 
- [Balsamiq](https://balsamiq.com/?gclid=CjwKCAjw2qHsBRAGEiwAMbPoDGWJ8Vt62S0dfo_Gtqbf5WdHzNWohvOch7nnGT7kxnWNIr85RsS2IxoCmwkQAvD_BwE)
    - **Balsamiq** was used to create the wireframes for this project.
- [MongoDB Atlas](https://www.mongodb.com/)
    - **MongoDB Atlas** was used to create the database for this project
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The **Flask** framework was used to design this project. 
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
    - **Flask-bcrypt** was used for encryption of passwords in this project.
- [ObjectId](https://api.mongodb.com/python/current/api/bson/objectid.html)
    - The ObjectId module was used to read objectIds of documents retrieved from MongoDB in python.
- [PyMongo](https://api.mongodb.com/python/current/)
    The PyMongo package was used to communicate with the Mongo DB database. 
- [Favicon Generator](https://www.favicon-generator.org/) 
    - **Favicon Generator** was used to generate this websites favicon
- [Gravit](https://gravit.io/) 
    - Gravit was used to design this projects SVGs. 
- [CompressJpeg](https://compressjpeg.com/)
    - Compress Jpeg was used to compress website images.

## Testing

Information on the testing process may be found in the [testing.md file](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/testing.md). 

## Deployment

### 

This project was written using the AWS Cloud IDE.

Project code was pushed to Github and Heroku.

MONGO_URI and SECRET_KEY config variables were saved to .bashrc, accessed from the terminal. 

### How to Run Code Locally

In order to run this project locally, the following tools are needed.

Using an IDE of your choice, ensure the following are installed, Git, PIP and Python3. Access to MongoDB Atlas is also required.

It is recommended that you create a virtual environment that contains the project's dependencies, and keeps those dependencies separate from those of other projects. 

Create MongoDB Database. Get Mongo_uri
For further details please consult the [sessions documentation](https://flask.palletsprojects.com/en/1.0.x/quickstart/#sessions)
[MONGO_URI documentation](https://docs.mongodb.com/manual/reference/connection-string/)
Set Secret Key
6. Set SECRET\_KEY
In order to set a secret key
$ python -c 'import os; print(os.urandom(16))'
b'_5#y2L"F4Q8z\n\xec]/'
7. Input the command git init to the terminal and push the project to github using the following commands:```git add .```, ```git commit -m "Initial Commit",``` and finally ```git push```. You should be prompted for your Github username and password. Enter these and the project will be pushed.

#### Cloning from Github

In order to run a repository locally, the repository must be cloned. To clone the repository
:
1. Follow the link to the [Apéritif: The Online Cookbook GitHub repository](https://github.com/stiofanEimeid/the-online-cookbook).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your preferred IDE, open the terminal.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on how to clone a repository from GitHub may be found [here](https://help.github.com/en/articles/cloning-a-repository).

To cut ties with this repository, type ```git remote rm origin``` into the terminal of your editor. In order to verify the terminal has been removed, type ```git remote -v``` to determine which remotes are still connected. 

#### Running the Site in your IDE

Create a virtual environment that contains the project's dependencies, and keeps those dependencies separate from those of other projects. 

1.  Activate Python's built in virtual environment using the command python -m .venv venv where the second instance of venv is the name of the virtual environment and thus serves as a placeholder in this instance. 
2. Activate the venv using the command ```.venv\Scripts\activate```. Note: Successful activation of the virtual environment is indicated by the presence of ```(env) $ ...``` in the terminal. Once finished working in the virtual environment, type in the command ```$ deactivate```
3. Pip may be upgraded with the command ```pip install --upgrade pip```.
4. Install any required modules using the command ```pip install -r requirements.txt```.
5. Save config vars Secret Key and Mongo URI to venv.
7. Create a new database in MongoDB called 'the-online-cookbook'. Create three collections called reipes, users and products
8. and structure them as follows:
9. 

Recipes 

DB Key | Data type 
--- | --- 
_id | Object ID 
recipe_name | String 
recipe_preptime | Integer32
recipe_serves | Integer32
receipe_ingredients | Array 
recipe_steps | Array 
diet | Array
recipe_description | String 
author | String
recipe_image | String
views | Integer32
favourites | Integer32
favourited-by | Array
time_created | String
last_updated | String

Users

DB Key | Data Type 
--- | --- 
_id | Object ID
name | String
name_lowercase | String
user_pw | String
favourites | Array
avatar | String
member_since | String

Products

DB Key | Data Type 
--- | --- 
 _id | Object ID 
product_name | String
product_image | String
product_description | String
product_price | String

8. Run using the command ```python3 app.py```.
9. Site may be found running at http://127.0.0.1:5000/ 

#### Deploying the Project to Heroku

This project has been deployed to Heroku using the master branch on GitHub. In order to deploy to Heroku, please follow these steps: 

1. Install the heroku API to your IDE of choice, using the command ... 
2. Create a requirements.txt file using the command ```sudo pip3 freeze > requirements.txt```
3. Create a Procfile using the command ```echo web: Python app.py > Procfile```. (Note that 'app.py' is the name of this project's main Python file.)
4. Free Dynos...
5. Create or login to your account on Heroku. Create a new app in your dashboard and name it. Set it to your region. Under the settings tab, select reveal var configs and input following:

IP | 0.0.0.0
PORT | 
MONGO URI | mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
SECRET KEY | <your_secret_key> *
DEBUG | FALSE

6. Go to the deploy tab, connect Github under the deployment method section and then select enable automic deployment.
7. At this point, you should be able to see the app running by clicking the Open App button in the top right of the Heroku dashboard. A record of build success and otherwise along with deployment may be viewed from the activity tab, also in the dashboard. If you encounter any issues using Heroku, please visit their [troubleshooting section](https://devcenter.heroku.com/categories/troubleshooting).

*Note the placeholders for your username, password, cluster name and database name. 

9. Under the settings tab of your account, enable automatic deploy by connecting to Github. Select the relevant repository with which to connect. This will enable your code to automatically update and deploy on heroku when you push Github.
10. MongoDB cluster and collection names...
11. With the site successfully deployed, you may now view it using the open app button. Problems with deployment may be found under the activity tab. 

## Credits

### Content

### Media
- [Unsplash](https://unsplash.com/)
    - The default image for recipes was taken from Unsplash, a stock image library.
Unsplash

Color Scheme

Recipe images

### Code

Pretty Printed
w3 schools
SVG wave

### Acknowledgements

Dynamic form field generation https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/

Custom checkbox found at https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

Custom radio box: https://stackoverflow.com/questions/17541614/use-images-instead-of-radio-buttons

https://www.favicon-generator.org/

[**Jump to top &uarr;**](#table-of-contents)