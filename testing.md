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

## Client Stories Testing

As a user, I want to find and share recipes. I want to be able to create an account that is secure and keeps track of the recipes I create, allowing me to update them and delete them as I please. 

As a site owner, I want to promote a brand of cooking tools to my users. I sought to accomplish this by making a direct connection between the recipes users were making and viewing and the tools I wished to promote and sell. The tools are presented to users as facilitating their needs and interests. 

## Manual Testing

### Responsiveness

The application was tested across browsers on mobile phone, laptop, tablet and desktop. 

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

### Logging In/Out

Users may log out from their account or from the navbar. The session is cleared of the user's username. 

### Account Settings

#### Deleting Account

Should a user wish to delete their account, they must reenter their password. They will then be asked to confirm that they wish to delete their account by a modal. Once a user has chosen to delete their account, any recipe written by them is removed from the database (they are warned that this will happen in the delete account template).

I tested this by creating test user accounts and writing test recipes before attempting to delete the account. My account was removed along with the recipes tied to the account. 

#### Changing Password

Should a user wish to change their password, they will be asked to reenter their current password before selecting a new password. I was able to successfully change my password. 

#### Changing Avatar

Because this is purely an asethetic choice and not bearing on the integrity of an account, a user may choose to change their avatar without having to enter their password.

### Recipes

#### Creating and Updating Recipes

Only registered and logged in users may add recipes to the database. If the user attempts to navigate to the add recipe page without registering or logging in, they will be met with an error message prompting them to login or register. 
Registered users may add recipes at any time using the add recipe tab contained in the navbar or by selecting the add recipe button in their account page under the 'My Recipes' tab. All recipes must have at least one step or ingredient. Both steps and ingredients may be dynamically added and removed. Once the user is satisfied with the recipe they have written, they may submit it to the database. The date and time of submission is noted and passed into the document. 

#### Reading Recipes

By default, every recipe in the database is returned when the user first navigates to the recipes page. Each recipe is represented by a card, with a maximum of twelve per page. Results are paginated in the interest of organisation and preventing the user becoming overwhelmed.

Clicking on a card will bring the user to that recipe's individual page. 

Search options include text search and search by filter. Filters include cuisine, dietary requirements and meal-time.

#### Updating and Deleting Recipes

Users may edit or delete any and all of their recipes by navigating to each recipes resptive page. If the session username matches the author of the recipe, the user will be given the option to edit or delete their recipe if they so wish. 
If a user decides to edit the recipe, they will be taken to a page that mirrors the page they used to upload the recipe in the first place, with each input area occupied by the current details of the recipe. Users may delete all but one of the recipes steps and/or ingredients. Once the user is happy with their changes, they may submit the recipe. A note is made of when the edit took place and contained in the recipe document.

On the other hand, if they decide to delete the recipe they will be asked to confirm their decision through a modal. If they do not change their mind, the recipe will be removed from the database. Users other than the author will not be given this option nor the option to edit the recipe. Instead, a user who is logged in but is not the author will be given the option of adding the recipe to their favourites while a user who is not logged in at all will be prompted to login to add the recipe to their favourites.

### Products

Users attempting to buy a product will be greeted by a modal advising them that a checkout functionality for buying products is currently unavailable.

## Bugs Discovered

Python logic in flask still works despite being commented out. 

100vh is not really 100vh on mobile.

CSS fires on page load with Chrome.

## Further Testing 