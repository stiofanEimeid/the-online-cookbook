# Apéritif: The Online Cookbook

# Stephen Byrne Portfolio

Stream Three Project: Data-Centric Development - Code Institute 

...

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

### Project Goals

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

Yellow, blue and red, white and grey.

**Styling**

The recipe pages are intended to convey essential information about a particular recipe in an intuitive and effective manner. This intent informs the design process. Recipe pages are intended to be uncluttered. The largest groups of information, steps and ingredients, are contained in tabs that the user may switch between, preventing the user from being bombared with large amounts of text and keeping page space free from everything but the most relevant information at any one time.

**Logo**

The logo is a cartoon ape in a chef's hat, the ape in aperifif if you will. The imagery of the site is intended to be light-hearted and fun in order to make cooking accessible for those who are less confident in their cooking abilities. More generally, the imagery is intended to illustrate that this a site for those who are passionate about cooking but one that doesn't take itself too seriously. 

**Background**

The background consists of two wheels of food with the logo at the center, slowly revolving. The wheels are made up of images of food and cooking utensils. Both of these comprise the content being delivered to the user, recipes which they can search and add to along with kitchen products to help bring these recipes to life. 

In addition, the wheels are meant to arrest the viewers attention and convey a sense of individuality about the site. It speaks to the vast array of possiblities in the world of cooking. 


### Wireframes

...



## Features

### Demo

...

### Existing Features

If they so wish, users may register an account with the site that displays all the recipes they create.

Users may search the recipes collection using a collection of filters whether they are registered or not. The filters are based on meal time and meal type.  

Users who have registered with the site may submit their own recipes to be viewed by other users. They may also update the recipe or even delete it. Naturally, each user will only be able to edit and delete recipes they themselves have submitted.

The discover page displays a number of statistics about the site such as most viewed recipes.

A product page displays products relevant to recipes submitted to the site. During the submission and editing processes of recipes, users may identify kitchen appliances and utensils from a list on each of the pages. Links to each product are then found on the recipe page. 

### Features left to implement 

A forum for users to discuss cooking content. 

## Data Structure

The recipe collection and user collection share a common key-value pair, "username", which links the two collections. The recipe entry takes the username of the user who created it. Each recipe can only have one creator and may therefore be described as a one-to-one relationship between each recipe and the user who created it. However, a user can have many recipes attributed to them.  As such, a one-to-many relationship exists between the user and the recipes created by them. 

### Recipe Collection

Title | DB Key | Data type 
--- | --- | --- 
Recipe ID | _id | Object ID 
Name | recipe_name | String 
Preparation Time | recipe_preptime | Integer 
Serves | recipe_serves | Integer 
Ingredients | receipe_ingredients | Array 
Steps | recipe_steps | Array 
Allergens | recipe_allergens | Boolean 
Description | recipe_description | String 
Username | username | String
Image | recipe_imgURL | String

### User Collection

Title | DB Key | Data Type 
--- | --- | --- 
User ID | _id | Object ID
Name | username | String
Email | user_email | String
Password | user_pw | String

### Product Collection

Title | DB Key | Data Type 
--- | --- | --- 
Product ID | _id | Object ID 
Product Name | product_name | String

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
- [Unsplash](https://unsplash.com/)
    - The default image for recipes was taken from Unsplash, a stock image library.
- Heroku
- Jninja
- Git

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

Create a virtual environment that contains the project's dependencies, and keeps those dependencies separate from those of other projects. 

#### Cloning from Github

In order to run a repository locally, the repository must be cloned. To clone the repository
:
1. Follow the link to the [routeRep GitHub repository](https://github.com/stiofanEimeid/the-online-cookbook).
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

#### Running Site in IDE

Create a virtual environment that contains the project's dependencies, and keeps those dependencies separate from those of other projects. 

1.  Activate Python's built in virtual environment using the command python -m .venv venv where the second instance of venv is the name of the virtual environment and thus serves as a placeholder in this instance. 
2. Activate the venv using the command .venv\Scripts\activate. Note: Successful activation of the virtual environment is indicated by the presence of (env) $ ... in the command terminal. Once finished working in the virtual environment, type in the command $ deactivate
3. Pip may be upgraded with the command pip install --upgrade pip.
4. Install any required modules using the command pip install -r requirements.txt
5. Save config vars Secret Key and Mongo URI to venv.
6. Run using the command Python3 app.py
7. Site may be found running at http://127.0.0.1:8080/ 

### Heroku

In order to deploy to Heroku, please follow these steps: 

1. Install the heroku API to your IDE of choice.
2. Create a requirements.txt file using the command pip freeze > requirements.txt
3. Create a Procfile using the command echo web: Python app.py > Procfile. (Note that 'app.py' is the name of this project's main Python file)
4. Free Dynos
5. Login to your account on Github. If you do not have a Github account, register here.  Create a new repository, name it copy the code that concerns cloning a repository from a remote server. 
6. Input the command git init to the terminal and push the project to github using the following commands, git add ., git commit -m "Initial Commit", and finally Git push. You should be prompted for your Github username and password. 
7. Create or login to your account on Heroku. Create a new app in your dashboard and name it. Set the region to Europe. 
8. Under the settings tab of your account, enable automatic deploy by connecting to Github. Select the relevant repository with which to connect. This will enable your code to automatically update and deploy on heroku when you push Github.
9. Var configs
| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

Note the placeholders for your username, password, cluster name and database name. 
10. MongoDB cluster and collection names...
11. With the site successfully deployed, you may now view it using the open app button. Problems with deployment may be found under the activity tab. 

## Credits

### Content

...

### Media

...

### Code

...

### Acknowledgements

Custom checkbox found at https://www.w3schools.com/howto/howto_css_custom_checkbox.asp

[**Jump to top &uarr;**](#table-of-contents)