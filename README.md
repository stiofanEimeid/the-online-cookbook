# The Online Cookbook

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

-taregt audience

-user goals

-how aperitif meets these needs

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

...

### How to Run Code Locally

...

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