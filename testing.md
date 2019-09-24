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
14. View products that I may need for cooking meals;
15. Navigate the site quickly and easily;
16. View the site on my preferred device, be it mobile, tablet, laptop or desktop. 


1. **See all recipes on the site without requiring an account to do so**

Users may search recipes without having to register or login. By default, every recipe in the database is returned when the user first navigates to the recipes page. Each recipe is represented by a card, with a maximum of twelve per page. Results are paginated in the interest of organisation and preventing the user becoming overwhelmed.

Each result is contained in a card which displays an image of the recipe, its name and its author, when it was submitted or when it was last updated, and a link to the recipe's individua; page. 

2. **Filter recipes by dietary requirements, meal type, and cuisine**

Users may search for recipes based on cuisine, meal type and dietary requirements. Each filter may be used with the other two or by itself. I have now uploaded at least recipe for each individual option within the three categories although not every combination of the three e.g. "Thai Gluten-free Shake" will return a recipe at this time. 

3. **Search Recipes with text-search**

Users may also search recipes by text. The text search considers all text in recipe documents and not just the title. 

4. **View each individual recipe and its details on its own page**

Users may click the "Go to recipe" function to view that recipe's page, from the search page, discover page or their account with regard to recipes they have created or favourited. 

Individual recipe pages provide fundamental information as well as a recipe image at the top of the page, including name, meal type, cuisine, cooking time, preparation time, dietary requirements. Users are not required to have an account to view individual recipes pages but if they are logged in they will see the option to add/remove the recipe from their favourites or, if they are the author, the option to update or delete the recipe.

Below this section is a section where the author may choose to add a description if they so wish. The author of the recipe will view a button labelled 'add description' if they are logged in while viewing the page. 

Following the description section are the ingredients and steps sections. Clicking on each ingredient or step adds a text-decoration property of 'line-through', crossing them off, so users can more easily keep track of the ingredients they have added and which step in the recipe they are currently on.. This is conveyed to the user by way of a tool-tip that appears when the user hovers over or taps the info icon beside the section heading.

Finally, the user will see three of nine random product cards, containing the respective product's image, name, and a link to the product's individual page. 

5. Create an account on the site that is secure

Users may create an account by clicking on the link contained the copy when the open the home page or from the side navigation bar, under the 'login/register' tab. Clicking the latter will bring them to the login page first where they will be asked to register if they do not already have an account. 

Users are then prompted to enter a username two to ten characters long, a password eight to sixteen characters long and an avatar.

If registration is successful they will be brought to their account page where they can view their username, time they became a registered user, their recipes, favourites and account settings along with an option to logout at the end of the page. 

6. Choose an avatar for my account

As mentioned above, users may choose one of four avatars upon registration. One is preselected and will become their avatar if they do not make a choice. 

7. Create, update and delete my own recipes;

**Create**

Only registered, logged in users may add recipes to the database. They may add recipes at any time using the 'add recipe' link contained in the side navigation bar or by selecting the 'add recipe' button in their account page under the 'My Recipes' tab.  Both steps and ingredients may be dynamically added and removed. Once the user is satisfied with the recipe they have written, they may submit it to the database. The date and time of submission is noted and passed into the document. Once submitted the recipe may be viewed in the search page or directly from their account page under the 'My Recipes' tab. 

**Update**

If the user wishes to update the recipe, they may do so directly from the recipe page while logged in as the recipe's author or from their account page. An 'edit recipe' button sits beside the 'go to recipe' button for each of their recipes.

The update recipe fields mirror those of the add recipe page but with each of the recipe's current field values appearing in their respective fields. Once the user is happy with the changes they must click submit to update the recipe in the database or simply click cancel to return to the previous page if they change their mind about updating the recipe. 

**Delete**

Users may delete their own and only their own recipes at any time from the recipe's page. The option to delete sits alongside the option to edit the recipe in the top section of the recipe page. They will be asked to confirm their decision by way of a modal before the recipe is removed from the database. 

8. Favourite recipes and tie them to my account so I can see all of them when I log in

Registered users may favourite recipes they have not authored from each recipes individual page. Favourites are then viewable under the relevant tab in their account page. 

9. Remove recipes from my favourites

They may also remove the recipe at any time, again directly from the recipe page where the add to favourites button has been replaced by a remove from favourites button. 

10. Be able to change my password;

Users may change their password by following the link in the settings tab in their account page. For security reasons, the user must enter their password again before they can create a new password. 

11. Be able to change my avatar;

Users may change their avatar by following the link in the settings tab in their account page. Their is no requirement to enter their password as this is merely an aesthetic and not a security concern. 

12. Be able to delete my account;

Users may delete their account by following the link in the settings tab in their account page. For security reasons, they must enter their password before their account is removed from the database. Once the user has decided to delete their account, the account along with all the recipes tied to the account are removed from the database. The user is warned of this on the page. 

13. View statistical data of the site in an appealling visual format;

Users may view site data on the statistics dashboard or the 'Discover' page. The page includes the number of recipes and users on the site, three pie charts showing the proportion of recipes by cuisine submitted, viewed and favourited respectively. Categories are broken down into continents (Europe, Africa, North America, South America, Asia) and 'Other' to present the data as clearly as possible to the user. 

Below the pie charts are three lists of five items each - most viewed recipes, most favourited recipes, and most recently submitted recipes. Each entry shows the recipe's name, author and the number of views or favourites it has or the date of its submission depending on which section it falls into. A link is to each recipe's individual page is included in each entry. The top recipe in each of the three sections also includes the recipe's image. 

14. View products that I may need for cooking meals;

Users may view a list of products in a 3x3 grid from the products link in the side navigation bar. Each entry contains a product image and name along with a link to its individual page. The individual page contains such information as a product image, the product name, its price, a description and an indication of whether or not it is in stock. At the bottom of the page is an option to buy. Unfortunately, check-out functionality is not currently available. 

15. Navigate the site quickly and easily;

Users may navigate through the site by way of the side navigation bar. The 'sidenav' is accessed by way of the menu icon contained the navigation bar at the time of the page. This navigation bar disappears when the user scrolls down in the interest of freeing up space on the screen. It reappears whenever the user scrolls up or is at the top of the page. 

The options contained in the navbar when not logged in include home, about, login/register, discover, products.

When users have logged in, the options are as follows, home, about, account, discover, products, add recipe and finally logout. 

16. View the site on my preferred device, be it mobile, tablet, laptop or desktop. 

The site is fully responsive - it's mobile, tablet, laptop and desktop-friendly.

Owner Stories

1. Promote a brand of cooking tools to my users

Users are shown three random products each time they view a recipe page. They may also view products directly from the products page which leads them to the product's individual page.

2. Collect data on what users are submitting to determine what types of recipes are popular and any trends that may exist for marketing purposes. 

The site collects data that is dynamically represented on a statistcs dashboard in the 'Discover page'. This allows me to view correlations in the data and identify trends among those who use the site in order to understand them better. 

If the user attempts to navigate to the add recipe page without registering or logging in, they will be met with an error message prompting them to login or register. All recipes must have at least one step or ingredient.



What fields are required?

Users may edit or delete any and all of their recipes by navigating to each recipes resptive page. If the session username matches the author of the recipe, the user will be given the option to edit or delete their recipe if they so wish. 
If a user decides to edit the recipe, they will be taken to a page that mirrors the page they used to upload the recipe in the first place, with each input area occupied by the current details of the recipe. Users may delete all but one of the recipes steps and/or ingredients. Once the user is happy with their changes, they may submit the recipe. A note is made of when the edit took place and contained in the recipe document.

On the other hand, if they decide to delete the recipe they will be asked to confirm their decision through a modal. If they do not change their mind, the recipe will be removed from the database. Users other than the author will not be given this option nor the option to edit the recipe. Instead, a user who is logged in but is not the author will be given the option of adding the recipe to their favourites while a user who is not logged in at all will be prompted to login to add the recipe to their favourites.



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