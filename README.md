<div align="center">
 <a href="https://the-online-cookbook.herokuapp.com/" target="_blank" rel="noopener"><img src="https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/intro_logo.png" alt="Apéritif: The Online Cookbook Logo"/></a>
 
 <h1 align="center">
 Apéritif: The Online Cookbook
 </h1>
 
</div>

<img src="https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/atoc_demo.png" alt="Apéritif: The Online Cookbook Logo Displayed on Different Screen Sizes"/>

# Stephen Byrne Portfolio

Stream Three Project: Data Centric Development - Code Institute 

Apéritif: The Online Cookbook allows users to search and view recipes, as well as create an account to create, update and delete their own recipes. They may allow view statsitical data on a dashboard and as well as kitchenware to help make the meals contained in the recipes. Visit the site here:  [https://the-online-cookbook.herokuapp.com/](https://the-online-cookbook.herokuapp.com/).

## Table of Contents
1. [**UX**](#ux)
    - [**Project Goals**](#project-goals)
    - [**User Goals**](#user-goals)
    - [**User Stories**](#user-stories)
    - [**Design Choices**](#design-choices)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Data Structure**](#datastructure)

4. [**Technologies**](#technologies)

5. [**Testing**](#testing)

6. [**Deployment**](#deployment)
    - [**How to Run Code Locally**](#how-to-run-code-locally)

7. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

## UX

#### Project Goals

The goal of this project is to build a database that allows users to carry out each CRUD operation: Creating, Reading, Updating and Deleting recipes. Although authentification is not expected I have included login functionality and user accounts in order to keep user recipes secure. 

#### User Goals

The target audience of the application are those who are passionate about cooking or wish to know more about it. The site is intended to be accessible to those who are relatively new to cooking and are curious about learning how to make new dishes. In addition, it hopes to attract those who are already passionate about cooking to share some of their favourite recipes with other users. Ideally, these groups would join together to create a thriving online community, one that is bound together by a love of cooking and learning more about it. 

Users seek the means to find a variety of recipes through an accessible interface that is easy to use. Frequent users or those with extensive experience in cooking may seek to add their recipes to the website to share with others as well as discover more recipes. 

Aperitif is easy to use and visusally appealling. Filters help users find specific recipes quickly and easily. Unique recipe pages give users all the information they need in an effective manner... With an account, users may add and edit recipes as well as keep track of their favourite recipes. The product section of recipe pages provide additional information to give user's the best cooking experience possible.

#### User Stories

As a user, I want to:

1. See all recipes on the site without requiring an account to do so;
2. Filter recipes by dietary requirements, meal type, and cuisine; 
3. Search recipes with text search;
4. View each individual recipe and its details on its own page;
5. Create an account on the site that is secure;
6. Choose an avatar for my account;
7. Create, update and delete my own recipes;
8. Favourite recipes and tie them to my account so I can see all of them when I log in;
9. Remove favourite recipes if I so wish;
10. Be able to change my password;
11. Be able to change my avatar;
12. Be able to delete my account;
13. View statistical data of the site in an appealling visual format;
14. View products that I may need for cooking meals.

As a site owner, I want to:
1. Promote a brand of cooking tools to my users; 
2. Collect data on what users are submitting to determine what types of recipes are popular and any trends that may exist for marketing purposes. 

### Design Choices

#### Fonts

The Lobster font was chosen for its vibrancy and energy to make important titles jump out to the user. 

The Nunito style was chosen for its sharpness and clarity to help convey a significant amount of text information to the reader clearly. 

Both fonts were sourced from GoogleFonts. 

#### Icons

Icons have been sourced from FontAwesome to help convey essential characteristics about menu options to users in an intuitive manner e.g. charts for the discover page to indicate to the user that the page is concerned with statistics.

#### Colours

The following set of colours have been used for the site's colour scheme: 

- #f78888: ![red](https://dummyimage.com/20x20/f78888/f78888.png)
- #f3d250: ![yellow](https://dummyimage.com/20x20/f3d250/f3d250.png)
- #90ccf4: ![blue](https://dummyimage.com/20x20/90ccf4/90ccf4.png)
- #072c43: ![navy](https://dummyimage.com/20x20/072c43/072c43.png)
- #ececec: ![grey](https://dummyimage.com/20x20/ececec/ececec.png)

I found these colours to be rich and pleasing to the eye when filling sections of the website for decoration purposes. Sections containing large amounts of text are grey and white in the interest of making them easy to read, following the style of popular websites such as facebook, reddit, youtube and twitter. Ultimately, I found that both categories, decorative and textual, complimented each other nicely. 

Navy rather than black was used for the side navigation menu to make text appear less flat and pop when the user is selecting a destination on the site.

#### Format

Each major section of the website, the home page, search page, individual recipe page, search product page, individual product page, account page and discover page, contain a rounded header at the top of the page made up of three colours, #90ccf4, #f3d250, and #f78888. I followed this format to provide a contrast between the heading of the page and the content of the page, and repeated this across each of the major pages of the site in the interest of visual consistency, so that the reader may become familiar with the format of the site quickly.

#### Logo

The logo is a cartoon ape in a chef's hat (the ape in apérifif if you will). The imagery of the site is intended to be light-hearted and fun in order to make cooking accessible for those who are less confident in their cooking abilities. More generally, the imagery is intended to illustrate that this a site for those who are passionate about cooking but one that doesn't take itself too seriously. 

#### The Wheel

The background consists of two rings of food revolving around the site logo. The wheels are made up of images of food and cooking utensils drawn by me in SVG format using Gravit. Three SVGs the same size are layered on top of one another. However, all three take up different sections of the circle so that the content of the lower layers may be seen through the upper layers. 

The rings are comprised of examples of the content being delivered to the user: recipes which they can search and add to along with kitchen products to help bring these recipes to life. 

I wanted a design to grab the user's attention as it is the first thing they see when they open the site. In addition, it is intended to speak to the wide range of possiblities in the world of cooking. I hope this stimulates the user's curiosity and leads them to explore the site.

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

### Pagination

Search results are paginated, with a maximum of twelve results(recipes) displayed per page. Users can keep track of how many recipes are displayed by a highlighted page number and a counter that displays the range of recipes being currently viewed of the total returned recipes e.g. 13-24 of 32 recipes.

### Edit, Add and Delete Recipes

Registered users may add recipes, update these recipes and finally delete the recipes. The add recipe and edit recipe pages consist of forms with spaces for essential information that will be displayed in individual recipe pages. registered users may dynamically add steps or ingredients up to a maximum of fifteen in each case. If users choose not to attach an image of the recipe to the form, a placeholder image will appear when the recipe's page is selected. 

When registered users are taken to the page of a recipe they have created, they are given the option to update or delete the recipe. The user is asked to confirm their decision to remove their recipe if they click on the delete button - first, to encourage users to think twice about removing their recipe and secondly to prevent frustation for users who may click the button accidentally. If the user visits a recipe page that is not of their own creation, they are instead given the option of adding the recipe to their favourites. Favourites are vieweable from their account page and may be removed at any time if they see fit. 

Users may search products on the product page. They are not given the option to add their own. 

### Discover

The discover page provides some statistics about the site, including most viewed recipes, most liked recipes, the proportion of recipes to users, and most popular categories of recipes. 

### Navigation

Users may navigate through the site by way of the side navigation bar. The 'sidenav' is accessed by way of the menu icon contained the navigation bar at the time of the page. This navigation bar disappears when the user scrolls down in the interest of freeing up space on the screen. It reappears whenever the user scrolls up or is at the top of the page. 

The options contained in the navbar when not logged in include home, about, login/register, discover, products.

When users have logged in, the options are as follows, home, about, account, discover, products, add recipe and finally logout. 

### Existing Features

If they so wish, users may register an account with the site that displays all the recipes they create.

Users may search the recipes collection using a collection of filters whether they are registered or not. The filters are based on meal time and meal type.  

Users who have registered with the site may submit their own recipes to be viewed by other users. They may also update the recipe or even delete it. Naturally, each user will only be able to edit and delete recipes they themselves have submitted.

The discover page displays a number of statistics about the site such as most viewed recipes.

A product page displays products relevant to recipes submitted to the site. During the submission and editing processes of recipes, users may identify kitchen appliances and utensils from a list on each of the pages. Links to each product are then found on the recipe page. 

### Features left to implement 

I would like to further develop the login and registration system. Should users forget their password, I would like to give them the option of creating a new one via email. As authetification was not meant to be a focus of the project according to the brief, I left this feature to be implemented in the future. 

I would like to implement full checkout functionality so user's may purchase products.

In order to promote user engagement, I would like to develop a reward system whereby users will be rewarded for appearing in the most-viewed or most-favourited sections. Rewards may take the form of discounts on cooking products.

I would like to create public versions of account pages so that user's may view each other's profile.

In terms of searching recipes, I would like to include pagination truncation for when large amounts of results are returned. 

Finally, I would also like to give users the ability to upload images and save those images to the database, for recipes and avatars.

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
Timestamp | timestamp | Double
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

### Languages

- This project uses HTML, CSS, JavaScript, and Python programming languages.

### Tools

- [Am I Responsive Design](http://ami.responsivedesign.is/)
    - **Am I Reponsive Design** was used to test the responsiveness of the site and to provide the [image of the site running
    on all devices](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/atoc_demo.png) contained in this README.md
- [Balsamiq](https://balsamiq.com/?gclid=CjwKCAjw2qHsBRAGEiwAMbPoDGWJ8Vt62S0dfo_Gtqbf5WdHzNWohvOch7nnGT7kxnWNIr85RsS2IxoCmwkQAvD_BwE)
    - **Balsamiq** was used to create the wireframes for this project.
- [Cloud9](https://c9.io) 
    - Developer used **Cloud9** for their IDE while building the website.
- [Git](https://git-scm.com/)
    - **Git** was used to handle version control
- [GitHub](https://github.com/)
    - This project uses **GitHub** to store and share all project code remotely. 
- [Heroku](https://www.heroku.com/)
    - The application is hosted on **Heroku**.
- [Jinja](https://jinja.palletsprojects.com/en/2.10.x/)
    - **Jinja** was used to create templates
- [MongoDB Atlas](https://www.mongodb.com/)
    - **MongoDB Atlas** was used to create the database for this project
- [PIP](https://pip.pypa.io/en/stable/installing/)
    - **PIP** was used to install the necessary software packages for this project. 

### Libraries

- [Bootstrap](https://www.bootstrapcdn.com/)
    - The project uses **Bootstrap** to simplify the structure of the website and make the website responsive easily.
- [CompressJpeg](https://compressjpeg.com/)
    - **Compress Jpeg** was used to compress website images.
- [Dynamic Dummy Image Generator](https://dummyimage.com/)
    - **Dynamic Dummy Image Generator** it was used to generate reference images for the colour scheme section above.
- [FontAwesome](https://fontawesome.com/)
    - **FontAwesome** was used to provide icons for the side-navigation bar. 
- [GoogleFonts](https://fonts.google.com/)
    - The Lobster and Nunito fonts found on **GoogleFonts** were used for this project. 
- [Favicon Generator](https://www.favicon-generator.org/) 
    - **Favicon Generator** was used to generate this websites favicon
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The **Flask** framework was used to design this project. 
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
    - **Flask-bcrypt** was used for encryption of passwords in this project.
- [Gravit](https://gravit.io/) 
    - **Gravit** was used to design this projects SVGs. 
- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.
- [ObjectId](https://api.mongodb.com/python/current/api/bson/objectid.html)
    - The ObjectId module was used to read objectIds of documents retrieved from MongoDB in python.
- [PyMongo](https://api.mongodb.com/python/current/)
    The PyMongo package was used to communicate with the Mongo DB database. 

## Testing

Information on the testing process may be found in the [testing.md file](https://github.com/stiofanEimeid/the-online-cookbook/blob/master/testing.md). 

## Deployment

This project was written using the AWS Cloud IDE.

Project code was pushed to Github and Heroku.

`MONGO_URI` and `SECRET_KEY` config variables were saved to ``.bashrc`, accessed from the terminal. 

### How to Run Code Locally

In order to run this project locally, the following tools are needed.

Using an IDE of your choice, ensure the following are installed, Git, PIP and Python3. Access to MongoDB Atlas is also required.

It is recommended that you create a virtual environment that contains the project's dependencies, and keeps those dependencies separate from those of other projects. 

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
2. Activate the venv using the command ```.venv\Scripts\activate```. Note: Successful activation of the virtual environment is indicated by the presence of ```(env) $ ...``` in the terminal. Once finished working in the virtual environment, type in the command ```$ deactivate```.
3. Pip may be upgraded with the command ```pip install --upgrade pip```.
4. Install any required modules using the command ```pip install -r requirements.txt```.
5. In your local IDE create a file called .flaskenv. Include the following:
FLASK_APP=app.py
FLASK_ENV=development
6. Save config vars Secret Key to .flask.env as environment variable. For guidance creating a secure secret key, please consult the [sessions documentation](https://flask.palletsprojects.com/en/1.0.x/quickstart/#sessions).
7. Create a new database in MongoDB called 'the-online-cookbook'. Create three collections called recipes, users and products. The products collection documents will have to be inputed directly to the database rather than through the application in its current form. It is based on the following structure. 

Products

DB Key | Data Type 
--- | --- 
 _id | Object ID 
product_name | String
product_image | String
product_description | String
product_price | String

8. Save your Mongo URI for the database collection to .flaskenv. The MONGO URI typically comes in the form: `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority` (Note the placeholders for your username, password, cluster name and database name). For further assistance, please consult the [MONGO_URI documentation](https://docs.mongodb.com/manual/reference/connection-string/).
9. Run using the command ```python3 app.py```.
10. Site may be found running at http://127.0.0.1:5000/ 

#### Deploying the Project to Heroku

This project has been deployed to Heroku using the master branch on GitHub. In order to deploy to Heroku, please follow these steps: 

1. Create a requirements.txt file using the command ```sudo pip3 freeze > requirements.txt```
2. Create a Procfile using the command ```echo web: Python app.py > Procfile```. (Note that 'app.py' is the name of this project's main Python file.)
3. Initialise a git repository using the command ```git init``` and push the project to github using the following commands:```git add .```, ```git commit -m "Initial Commit",``` and finally ```git push```. You should be prompted for your Github username and password. Enter these and the project will be pushed.
4. Create or login to your account on Heroku. Create a new app in your dashboard and name it. Set it to your region. Under the settings tab, select reveal var configs and input following:

Key | Value
--- | ---
IP | 0.0.0.0
PORT | 5000
MONGO URI | <your_mongo_uri>
SECRET KEY | <your_secret_key> 

5. Go to the deploy tab, connect Github under the deployment method section and then select enable automic deployment.
6. At this point, you should be able to see the app running by clicking the Open App button in the top right of the Heroku dashboard. A record of build success and otherwise along with deployment may be viewed from the activity tab, also in the dashboard. If you encounter any issues using Heroku, please visit their [troubleshooting section](https://devcenter.heroku.com/categories/troubleshooting).
7. Under the settings tab of your account, enable automatic deploy by connecting to Github. Select the relevant repository with which to connect. This will enable your code to automatically update and deploy on heroku when you push Github.
8. With the site successfully deployed, you may now view it using the open app button. A history of the deployment statuses may be viewed under the activity tab. 

## Credits

### Content

SVG designs and product copy were designed and written by me, respectively. 

### Media

Color scheme was found at [Visme](https://visme.co/blog/website-color-schemes/), no. 39, 'Rich and Colorful', on the list. 

Placeholder image by [Dose Juice](https://unsplash.com/s/photos/dose-juice) on Unsplash found on [Unsplash](https://unsplash.com/).

A number of recipes and their respective images taken from [BBC Food](https://www.bbc.co.uk/food). Links accrediting each auther included in each recipe description. 

#### Product Images:

- Spatula image by [WikimediaImages](https://pixabay.com/users/WikimediaImages-1185597/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2202239) from [Pixabat](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=2202239).

- Frying pan image by [Walter Bichler](https://pixabay.com/users/Silberfuchs-721/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554072) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554072).

- Cutting-board image by [StockSnap](https://pixabay.com/users/StockSnap-894430/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=925544) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=925544).

- Pot image by [Walter Bichler](https://pixabay.com/users/Silberfuchs-721/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554068) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554068).

- Kitchen knife image by [Walter Bichler](https://pixabay.com/users/Silberfuchs-721/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554067) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554067).

- Peeler image by [Walter Bichler](https://pixabay.com/users/Silberfuchs-721/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554070) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=554070).

- Wooden pestle and mortar image by [Robert-Owen-Wahl](https://pixabay.com/users/Robert-Owen-Wahl-2077322/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1238282) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1238282).

- Whisk image by [InspiredImages](https://pixabay.com/users/InspiredImages-57296/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1056226) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1056226).

- Blender image by [Yao Charlen](https://pixabay.com/users/opaye-1806/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=10934) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=10934).


### Code

- Login system designed using [Pretty Printed: Creating a User Login System Using Python, Flask and MongoDB](https://www.youtube.com/watch?v=vVx1737auSE&t=45s).
- Overlay code found at [w3schools](https://www.w3schools.com/howto/howto_css_overlay.asp).
- Navbar disappear on scroll functionality adapted from [w3schools](https://www.w3schools.com/howto/howto_js_navbar_hide_scroll.asp).
- Sidebar functionality found at [w3schools](https://www.w3schools.com/w3css/w3css_sidebar.asp).
- Images used in the place of buttons code found at [StackOverflow](https://stackoverflow.com/questions/17541614/use-images-instead-of-radio-buttons).
- Rounded div code taken from [Smooth](https://smooth.ie/blogs/news/svg-wavey-transitions-between-sections).
- Function used to add percentages to pie charts found at  [StackOverflow](https://stackoverflow.com/questions/25209971/add-percentages-to-the-pie-chart-label-in-dc-js).
- Code for dynamic form fields found at [codexworld](https://www.codexworld.com/add-remove-input-fields-dynamically-using-jquery/).

### Acknowledgements

Thanks to everyone who tested the app. Their feedback helped make it better. 

Thanks again to my mentor for her guidance and encouragement.

### Disclaimer 

The contents of this website are for educational purposes only.

[**Jump to top &uarr;**](#table-of-contents)