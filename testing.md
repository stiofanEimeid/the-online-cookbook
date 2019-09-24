# Apéritif: The Online CookBook - Testing Details

[Main README.md file](README.md)

## Table of Contents

1. [**Automated Testing**](#automated-testing)
    - [**Validation services**](#validation-services)
2. [**Client Stories Testing**](#client-stories-testing)
3. [**Manual Testing**](#manual-testing)
    - [**Testing undertaken on desktop**](#testing-undertaken-on-desktop)
    - [**Testing undertaken on tablet and phone devices**](#testing-undertaken-on-tablet-and-phone-devices)
4. [**Bugs discovered**](#bugs-discovered)
    - [**Solved bugs**](#solved-bugs)
    - [**Unsolved bugs**](#unsolved-bugs)
5. [**Further Testing**](#further-testing)

## Automated Testing

### Validation services
The following validation services and linter were used to check the validity of the website code.
- [W3C Markup Validation](https://validator.w3.org/) was used to validate HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate JavaScript.
- [Esprima](https://esprima.org/demo/validate.html) was used to validate JS syntax.
- [PEP8](http://pep8online.com/) was used to ensure python code is PEP8 compliant.

## Client Stories Testing

**As a user I want to**

1. **Find recipes.**

#### Reading Recipes

Users may search recipes without having to register or login. By default, every recipe in the database is returned when the user first navigates to the recipes page. Each recipe is represented by a card, with a maximum of twelve per page. Results are paginated in the interest of organisation and preventing the user becoming overwhelmed.

Clicking on a card will bring the user to that recipe's individual page. 

Search options include text search and search by filter. Filters include cuisine, dietary requirements and meal-time.

Dietary options...

Pagination..

Individual recipe pages provide fundamental information as well as a recipe image at the top of the page.

Clicking on each ingredient or step adds strikes them out or adds a text-decoration property of 'line-through' so users can more easily keep track of the cooking materials and process.

2. **Add, update and delete my own recipes.**

Only registered and logged in users may add recipes to the database. If the user attempts to navigate to the add recipe page without registering or logging in, they will be met with an error message prompting them to login or register. 
Registered users may add recipes at any time using the add recipe tab contained in the navbar or by selecting the add recipe button in their account page under the 'My Recipes' tab. All recipes must have at least one step or ingredient. Both steps and ingredients may be dynamically added and removed. Once the user is satisfied with the recipe they have written, they may submit it to the database. The date and time of submission is noted and passed into the document. 

What fields are required?

Users may edit or delete any and all of their recipes by navigating to each recipes resptive page. If the session username matches the author of the recipe, the user will be given the option to edit or delete their recipe if they so wish. 
If a user decides to edit the recipe, they will be taken to a page that mirrors the page they used to upload the recipe in the first place, with each input area occupied by the current details of the recipe. Users may delete all but one of the recipes steps and/or ingredients. Once the user is happy with their changes, they may submit the recipe. A note is made of when the edit took place and contained in the recipe document.

On the other hand, if they decide to delete the recipe they will be asked to confirm their decision through a modal. If they do not change their mind, the recipe will be removed from the database. Users other than the author will not be given this option nor the option to edit the recipe. Instead, a user who is logged in but is not the author will be given the option of adding the recipe to their favourites while a user who is not logged in at all will be prompted to login to add the recipe to their favourites.

3. **Create an account that is secure and keeps track of the recipes I create**

<div align="center">
<img src="https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/flowchartfinal.png" alt="User login and registration flowchart"/>
</div>

The flowchart documents all the eventualities of a user trying to gain access to the database. 

### Registering

Usernames may be a maximum of eight characters long. Passwords must be between eight and twelve characters inclusive. 

In the interest of security, duplicate usernames are not allowed. A lowercase version of a user's chosen username is created during a new account registration. This is then checked against the lowercase versions of usernames already in the database among the users' collection. If such a match exists, users will be met with an error message, prompting them to register with a different name (or login should the user have mistaken the registration page for the login page). As such, a user will not be able to regsiter a username that already exists by changing the case of a letter or letters. 

In order to test this measure, I attempted to login with different case versions of usernames already in the database. Being unable to register a duplicate username confirmed that the measure works as intended. 

In addition, usernames may not be changed once a user has registered although they may change their password. 

An avatar is preselected for the user although they may change it during registration or any time after through the settings found on their account page.

If registration is successful, users will be brought to their account page where they can view their avatar, recipes, favourites and access account settings.

### Logging In/Out

Users may login with a case-insensitive version of their username along with their password. If either the username or password is incorrect, the user will be prompted by an error message asking them to login again or register a new account. The user does not know whether the username or the password or both were correct in the interest of greater security to the database. Upon successfully logging in, users are brought to their account page.

Users may log out from their account or from the navbar. The session is cleared of the user's username. 

### Account Settings

#### Deleting Account

Should a user wish to delete their account, they must reenter their password. They will then be asked to confirm that they wish to delete their account by a modal. Once a user has chosen to delete their account, any recipe written by them is removed from the database (they are warned that this will happen in the delete account template).

I tested this by creating test user accounts and writing test recipes before attempting to delete the account. My account was removed along with the recipes tied to the account. 

#### Changing Password

Should a user wish to change their password, they will be asked to reenter their current password before selecting a new password. I was able to successfully change my password. 

#### Changing Avatar

Because this is purely an asethetic choice and not bearing on the integrity of an account, a user may choose to change their avatar without having to enter their password.

**As a site I want to**

1. **Promote a brand of cooking tools to my users.**

Users may view a selection of products directly through the products link in the navbar. Each product has an individual page similar to recipes. 

I sought to accomplish this by making a direct connection between the recipes users were making and viewing and the tools I wished to promote and sell. Each individual recipe page features a random selection of three of nine tools. The tools are presented to users as facilitating their needs and interests. Users can click through to each of the three products' individual page, where a larger image of the product along with a description, a price and an option to buy appear.

Users attempting to buy a product will be greeted by a modal advising them that a checkout functionality for buying products is currently unavailable.

2. **Observe trends in the content being submitted to the website by way of a statistics dashboard**

Some site statistics are represented in the Discover template. They offer some general statistics about the site, such as the number of users and recipes currently in the database, as well as visual representations of the the type of recipes that are popular. Two pie-charts evaluate the proportion of each recipe being submitted as well as the proportion of each recipe being viewed. This may be used potentially to taylor cooking utensils and applicances to users in the future to determine what areas of cooking are most popular to users. Further scales may be added once larger amounts of data are available.

In addition, there are sections that show the user four recipes are the most viewed, another four that are most favourited and finally a list of recent submissions. In order to promote user engagement, users may be rewarded for appearing in the most-viewed or most-favourited sections. Rewards may take the form of discounts on cooking products. 

## Manual Testing

### Responsiveness

The application was tested on mobile phone (Oneplus6, iphone), laptop(Macbook Air), tablet and desktop(Mac Desktop) in addition to Google Chrome devtools. 

### Browswer Compatibility

The application was tested on Edge, Firefox, Google Chrome, Opera and Safari. 

## Bugs Discovered

### Solved Bugs

Initially, when submitting forms, form fields changed would be updated despite clicking on the cancel button. I realised that
the attribute 'type' set to 'button' must be set to a button on the page if it was not intended to post form data.

A bug was noticed when using the application on Safari. Whereby the navbar would disappear when the user scrolled up while at the top of the page.
In general, the navbar should stay fixed at the top of the page and only disappear when the user scrolls down, reappearing when the user scrolls up again.
This is based on the current scroll position being greater than the previous scroll position for the navbar to disappear and vice versa for it to reappear.
I attributed the problem on Safari to the fact that the user may scroll up further, even while at the top of the page. This meant that the user's previous scroll
position, a negative Y-axis value, would be greater than the current scroll position and would therefore disappear as stupuldated by the code. I changed the code
to make the navbar appear then the previous scroll position was greater than the current scroll position OR when the previous scroll position was less
than or greater than zero. This seemed to fix the issue.

### Unsolved Bugs

The CSS transition associated with the side navigation bar fires when the page is loaded on Chrome. 

## Further Testing 

Family and friends were asked to test the application and provide feedback. This proved immensely helpful for fine-tuning the applicaiton.