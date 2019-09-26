# Apéritif: The Online CookBook - Testing Details

[Main README.md file](README.md)

[Go to site](https://the-online-cookbook.herokuapp.com/)

## Table of Contents

1. [**Automated Testing**](#automated-testing)
    - [**Validation services**](#validation-services)
2. [**Client Stories Testing**](#client-stories-testing)
    - [**User Stories Testing**](#as-a-user-i-want-to)
    - [**Owner Stories Testing**](#as-an-owner-i-want-to)
3. [**Manual Testing**](#manual-testing)
    - [**Responsiveness**](#responsiveness)
    - [**Browser Compatibility**](#browser-compatibility)
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

### As a user I want to:

1. **See all recipes on the site without requiring an account to do so**

Users may search recipes without having to register or login. By default, every recipe in the database is returned when the user first navigates to the recipes page. Each recipe is represented by a card, with a maximum of 12 per page. Results are paginated in the interest of organisation and preventing the user from becoming overwhelmed.

Each result is contained in a card which displays an image of the recipe, its name and its author, when it was submitted or when it was last updated, and a link to the recipe's individual page. 

2. **Filter recipes by dietary requirements, meal type, and cuisine**

Users may search for recipes based on cuisine, meal type, and dietary requirements. Each filter may be used with the other two or by itself. I have now uploaded at least recipe for each individual option within the three categories although not every combination of the three e.g. "Thai Gluten-free Shake" will return a recipe at this time. 

3. **Search Recipes with text-search**

Users may also search recipes by text. The text search considers all text in recipe documents and not just the title. 

4. **View each individual recipe and its details on its own page**

Users may click the "Go to Recipe" button to view that recipe's page, from the search page, discover page or their account with regard to recipes they have created or favourited. 

Individual recipe pages provide basic information as well as a recipe image at the top of the page, including name, meal type, cuisine, cooking time, preparation time, dietary requirements. Users are not required to have an account to view individual recipes pages but if they are logged in they will see the option to add or remove the recipe from their favourites or, if they are the author, the option to update or delete the recipe.

Below this section is a section where the author may choose to add a description, if they so wish. The author of the recipe will view a button labelled 'Add Description' if they are logged while viewing the page. 

Following the description section are the ingredients and steps sections. Clicking on each ingredient or step adds a text-decoration property of 'line-through', crossing them off, so users can more easily keep track of the ingredients they have added and which step in the recipe they are currently on. The user is informed of this feature by way of a tool-tip that appears when the user hovers over or taps the info icon beside the section heading.

Finally, the user will see three of nine random product cards, containing the respective product's image, name, and a link to the product's individual page.

5. **Create an account on the site that is secure**

Users may create an account by clicking on the link contained the copy when the open the home page or from the side navigation bar, under the 'login/register' tab. Clicking the latter will bring them to the login page first where they will be asked to register if they do not already have an account. 

Users are then prompted to enter a username two to ten characters long, a password eight to sixteen characters long and an avatar.

If registration is successful they will be brought to their account page where they can view their username, the time they became a registered user, their recipes, favourites and account settings along with an option to logout at the end of the page. 

6. **Choose an avatar for my account**

As mentioned above, users may choose one of four avatars upon registration. One is preselected and will become their avatar if they do not make a choice. 

7. **Create, update and delete my own recipes**

Create

- Only registered, logged in users may add recipes to the database. They may add recipes at any time using the 'Add Recipe' link contained in the side navigation bar or by selecting the 'Add Recipe' button in their account page under the 'My Recipes' tab.  Both steps and ingredients may be dynamically added and removed. Once the user is satisfied with the recipe they have written, they may submit it to the database. The date and time of submission is noted and passed into the document. Once submitted the recipe may be viewed in the search page or directly from their account page under the 'My Recipes' tab. 

Update

- If the user wishes to update the recipe, they may do so directly from the recipe page while logged in as the recipe's author or from their account page. An 'Edit Recipe' button sits beside the 'Go to Recipe' button for each of their recipes.

- The update recipe fields mirror those of the add recipe page but with each of the recipe's current field values appearing in their respective fields. Once the user is happy with the changes they must click submit to update the recipe in the database or simply click cancel to return to the previous page if they change their mind about updating the recipe. 

Delete

- Users may delete their own and only their own recipes at any time from the recipe's page. The option to delete sits alongside the option to edit the recipe in the top section of the recipe page. They will be asked to confirm their decision by way of a modal before the recipe is removed from the database. 

8. **Favourite recipes and tie them to my account so I can see all of them when I log in**

Registered users may favourite recipes they have not authored from each recipes individual page. Favourites are then viewable under the relevant tab in their account page. 

9. **Remove recipes from my favourites**

They may also remove the recipe at any time, again directly from the recipe page where the add to favourites button has been replaced by a remove from favourites button. 

10. **Be able to change my password**

Users may change their password by following the link in the settings tab in their account page. For security reasons, the user must enter their password again before they can create a new password. 

11. **Be able to change my avatar**

Users may change their avatar by following the link in the settings tab in their account page. Their is no requirement to enter their password as this is merely an aesthetic and not a security concern. 

12. **Be able to delete my account**

Users may delete their account by following the link in the settings tab in their account page. For security reasons, they must enter their password before their account is removed from the database. Once the user has decided to delete their account, the account along with all the recipes tied to the account are removed from the database. The user is warned of this on the page. 

13. **View statistical data of the site in an appealling visual format**

Users may view site data on the statistics dashboard or the 'Discover' page. The page includes the number of recipes and users on the site, three pie charts showing the proportion of recipes by cuisine submitted, viewed, and favourited. Types of cuisine are broken down into continents (Europe, Africa, North America, South America, Asia) and 'Other' to present the data as clearly as possible to the user. 

Below the pie charts are three lists of five items each - most viewed recipes, most favourited recipes, and most recently submitted recipes. Each entry shows the recipe's name, author and the number of views or favourites it has or the date of its submission depending on which section it falls into. A link is to each recipe's individual page is included in each entry. The top recipe in each of the three sections also includes the recipe's image. 

14. **View products that I may need for cooking meals**

Users may view a list of products in a 3x3 grid from the products link in the side navigation bar. Each entry contains a product image and name along with a link to its individual page. The individual page contains such information as a product image, the product name, its price, a description and an indication of whether or not it is in stock. At the bottom of the page is an option to buy. Unfortunately, check-out functionality is not currently available. 

### As an owner I want to:

1. **Promote a brand of cooking tools to my users**

I sought to accomplish this by making a direct connection between the recipes users were making and viewing and the tools I wished to promote and sell. Each individual recipe page features a random selection of three of nine tools. Users can click through to each of the three products' individual page, where a larger image of the product along with a description, a price, and an option to buy appear.

Users may also view products directly from the products page which leads them to the product's individual page.

I kept the product copy light-hearted and playful to inject some personality into the brand.

2. **Collect data on what users are submitting to determine what types of recipes are popular and any trends that may exist for marketing purposes**

Some site statistics are represented in the 'Discover page'. They offer some general statistics about the site, such as the number of users and recipes currently in the database, as well as visual representations of the the type of recipes that are popular. 

Three pie-charts evaluate the proportion of each recipe being submitted as well as the proportion of each recipe being viewed and favourited. These charts may be used to identify trends among those who use the site and better understand how they use the site. Furthermore, I may be able to determine what areas of cooking are most popular to users and tailor cooking utensils and applicances to them. 

In addition, there are sections that show the user five recipes are the most viewed, another five that are most favourited and finally five of the most recent submissions. 

#### Searching Recipes

When the user first opends the recipes page, every recipe in the database is returned. They may search these recipes with text-search or with the three search filters. I ran a number of search queries with the text-search to verify it worked as intended and performed a extensive amount of searches with the filters together and in isolation and verified the returned recipes matched the selected criteria. 

#### Adding Recipes

Users may only add recipes if they are logged in. Users who attempt to add recipes without logging in by using the add recipe url will be asked to login or register to add recipes. Users who are logged in may add recipes from the link in the side navigation bar or from the link in their account under the 'My Recipes' tab. 

They will be required to complete a number of fields including recipe name, recipe description, meal type, cuisine, cooking time, preparation time, number of people the recipe serves, steps, ingredients, dietary information and finally recipe image. All these fields are required except for recipe description, image and dietary information (although the latter merely equates to no special dietary information). All recipes must have at least one step or ingredient. Users may only include a maximum of 30 ingredients and 30 steps.

If a user attempts to submit a form without filling one or more of the required fields, the form will not submit and they will be asked to provide input for the empty required fields. I tested this feature with recipes I myself inputted to the database. I then made sure the correct information appeared in the database through MongoDB Atlas.

#### Editing Recipes

Users may only update/edit the recipes they have authored. In order to do this they must navigate to the recipe's individual recipe page where they will be given the option to edit the recipe(along with the option to delete the recipe.) In order to test this feature, I visited the same recipe page as a visitor, a logged-in user who was not the author and logged-in as the recipe's author. The option only appeared when logged in as the recipe's author, as intended.I repeated this process with other recipes with different author accounts.

If a visitor to the site who is not logged in attempts to view the edit recipe page with a recipe id in the url, they will be asked to sign in to edit their recipes or register an account. If a logged-in user who is not the author tries this action, they will instead see an error message telling them they may only delete their own recipes. 

When users decide to edit their recipe, they will be taken to a page that mirrors the page they used to add the recipe with all the same fields now filled with the values they inputted when adding the recipe. All fields are required apart from recipe description, recipe image and dietary requirements. Users may delete all but one of the steps and ingredients and include up to 30 steps and ingredients. Once the user is happy with their changes, they may submit the recipe. A note is made of when the edit took place and contained in the recipe document. If a user removes any of the required values and attempts to submit the updated recipe, the form will not submit. Instead they will be pointed to the empty required fields and asked for input. This process was carried out for each recipe in the database. 

#### Deleting Recipes

Users may only delete the recipes they have themselves authored. In order to do this they must navigate to the recipe's individual recipe page where they will be given the option to delete the recipe (along with the option to edit the recipe) and asked to confirm this decision through a modal. In order to test this feature, I visited the same recipe page as a visitor, a logged-in user who was not the author and logged-in as the recipe's author. The option only appeared when logged in as the recipe's author, as intended. I repeated this with other recipes with different author accounts.

Once I had chosen to delete a recipe, I made sure it had been removed from the database through Mongo DB Atlas. I repeated this process for more test recipe documents.

# Account Access

<div align="center">
<img src="https://github.com/stiofanEimeid/the-online-cookbook/blob/master/static/img/flowchartfinal.png" alt="User login and registration flowchart"/>
</div>

The flowchart documents all the eventualities of a user trying to login or register. 

### Registering

Usernames may be a maximum of eight characters long. Passwords must be between eight and twelve characters inclusive. 

In the interest of security, duplicate usernames are not allowed. A lowercase version of a user's chosen username is created during a new account registration. This is then checked against the lowercase versions of usernames already in the database among the users' collection. If such a match exists, the user will be met with an error message, prompting them to register with a different name (or login should the user have mistaken the registration page for the login page). As such, a user will not be able to regsiter a username that already exists by changing the case of a letter or letters. 

In order to test this measure, I attempted to login with different case versions of usernames already in the database. Being unable to register a duplicate username confirmed that the measure works as intended. 

In addition, usernames may not be changed once a user has registered although they may change their password. 

An avatar is preselected for the user although they may change it during registration or any time after through the settings found on their account page.

If registration is successful, users will be brought to their account page where they can view their avatar, recipes, favourites and access account settings.

### Logging In/Out

Users may login with a case-insensitive version of their username along with their password. If either the username or password is incorrect, the user will be prompted by an error message asking them to login again or register a new account. The user does not know whether the username or the password or both were correct in the interest of greater security to the database. Upon successfully logging in, users are brought to their account page.

Users may log out from their account or from the navbar. The session is cleared of the user's username. 

### Account Settings

#### Access to Settings

Users may only view the account page if they are logged in. If they attempt to view the account page or any of its settings, they will be met with an error page and asked to login or register an account.

The account page visible to users is based on the username they used to sign in. This is set as the session username and used to retrieve the relevant user documents in the database. The account url has no information tied to which specific account it is displaying. 

#### Account Tabs

The Account page displays some basic information about the user currently logged in along with their recipes and favourites. I logged in with multiple accounts to ensure that the correct information was being displayed. 

#### Deleting Account

Should a user wish to delete their account, they must reenter their password. They will then be asked to confirm that they wish to delete their account by a modal. Once a user has chosen to delete their account, any recipe written by them is removed from the database (they are warned that this will happen at the top of the page).

I tested this by creating test user accounts and writing test recipes before attempting to delete the account. My account was removed along with the recipes tied to the account. I repeated this process with a number of dummy accounts and dummy recipe entries.

#### Changing Password

Should a user wish to change their password, they will be asked to reenter their current password before selecting a new password. I was able to successfully change my password a number of times with different accounts. 

#### Changing Avatar

Because this is purely an asethetic choice and not bearing on the security of an account, a user may choose to change their avatar without having to enter their password. I was successfully able to change my avatar a number of times with different accounts.

#### Navigation Bar

The navigation bar is fixed to the top of the page. It disappears on scroll down but reappears on scroll up. The Menu button opens a side navigation bar with a number of options to choose from. Once the side menu is open, an overlay covers the rest of the webpage not already covered by the sidenav. Users may scroll down the sidenav through the options but they may not scroll through the webpage or otherwise interact with it while the sidenav is open. 

Different options appear depending on whether the user is logged in or not. I checked the options while logged out compared to being logged in with different accounts to verify the intended options appeared as expected. 

#### Discover Page

The Discover Page dynamically generates three pie-charts using site data using dc.js and d3.js. I tested this feature by hard-coding various values to be graphed by each of the three pie-charts before switching to data generated by MongoDB search queries. Cross-referencing the results with the values in the database confirmed the correct values were being displayed. 

It also returns 5 results of a sort query based on number of recipe views, recipe favourites and time a particular recipe was submitted. I created a number of test recipes to verify that they appeared in the recently submitted section and cross-referenced the top recipes based on views and favourites with the values contained in the database through MongoDB Atlas. 

#### Pagination

Pagination is provided on the search recipes page. A maximum of twelve results per page is displayed. The range of recipes being displayed (a multiple of 12) of total recipes returned is displayed in a div container at the top and bottom of the results e.g. 13-24 of 28 results displayed. 
Once the user reaches a page where the results do not reach the next multiple of 12, the recipe total will instead be displayed rather than a multiple of 12 i.e. 24-28 of 28 results displayed. This feature was implemented with conditional operators - if the page number by a multiple of 12 was greater than the total recipes, the total recipe value would take the place of the second value in the statement. Otherwise, it would be a multiple of 12. 

I tested this feature using a variety of search queries i.e. text search and filter combinations.

#### Products

Users attempting to buy a product will be greeted by a modal advising them that a checkout functionality for buying products is currently unavailable.

## Manual Testing

### Responsiveness

The application was tested on mobile phone (Oneplus6, iphone), laptop(Macbook Air), tablet(iPad) and desktop(Mac Desktop) in addition to Google Chrome devtools. 

The site is fully responsive - it's mobile, tablet, laptop and desktop-friendly.

### Browser Compatibility

The application was tested on Edge, Firefox, Google Chrome, Opera and Safari. The site functioned satisfactorily on every browser except Safari, discussed below. 

## Bugs Discovered

### Solved Bugs

Initially, when submitting forms, form fields changed would be updated despite clicking on the cancel button. I realised that the attribute 'type' set to 'button' must be set to a button on the page if it was not intended to post form data.

A bug was noticed when using the application on Safari. The navbar would disappear when the user scrolled up while at the top of the page. In general, the navbar should stay fixed at the top of the page and only disappear when the user scrolls down, reappearing when the user scrolls up again. This is based on the current scroll position being greater than the previous scroll position for the navbar to disappear and vice-versa for it to reappear. I attributed the problem on Safari to the fact that the user may scroll up further, even while at the top of the page. This meant that the user's previous scroll position, a negative Y-axis value, would be greater than the current scroll position and would therefore disappear as stipulated by the code. I changed the code to make the navbar appear then the previous scroll position was greater than the current scroll position OR when the previous scroll position was less than or greater than zero. This seemed to fix the issue.

### Unsolved Bugs

There are no bugs I am aware of at this time.

## Further Testing 

Family and friends were asked to test the application and provide feedback. This proved immensely helpful for fine-tuning the applicaiton.

[**Jump to top &uarr;**](#table-of-contents)