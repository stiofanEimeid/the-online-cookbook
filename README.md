# The Online Cookbook

## Data Structure

The recipe collection and user collection share a common key-value pair, username, which links the two collections. The recipe entry takes the username of the user who created it. As each recipe can only have one creator, this describes a one-to-one relationship but a user can have many recipes in her name and is therefore a one-to-many relationship.

### Recipe Collection

Title | DB Key | Data type 
--- | --- | --- 
Recipe ID | _id | Object ID 
Name | 2 | String | 4
Preparation Time | 2 | Integer 
Serves | 2 | Integer | 4
Ingredients | receipe_ingredients | Array 
Steps | recipe_steps | Array 
Allergens | recipe_allergens | Boolean 
Description | recipe_description | String 
Username | username | String

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

