# Recipe Recommendation System 


## Table Of Contents

- Business Understanding
- Data Understanding
- Data Preparation
- Modelling 
- Deployment
  

## Business Understanding

### Business Description 
The Boma Pot is a web-based culinary platform dedicated to sharing authentic African recipes with the world. Our mission is to enhance the cooking experience of home chefs by providing them with a diverse collection of recipes rooted in African culinary traditions, while also incorporating global influences. Whether you're an experienced cook or just starting, The Boma Pot offers a wide variety of recipes that empower users to create delicious, flavorful meals from the comfort of their homes.


## Business Goal 
### Objective
The main objective of this project is to develop an item-based recipe recommendation system that suggests recipes to users based on the ingredients they have available. By analyzing the ingredients present in various recipes, the system aims to provide relevant and appealing recommendations that encourage users to explore and cook diverse dishes rooted in African culinary traditions, while also incorporating global flavors.


## Data Understanding
### Data Source
We are working with two datasets. The first is from the Food and Agriculture Organization of the United Nations, in collaboration with Kenya's Ministry of Agriculture and Livestock Development. Originally in PDF format, the necessary information was extracted and converted into a CSV file. The second dataset comes from Kaggle, titled the Food Ingredients and Recipe Dataset with Image Name Mapping, which provides global recipe data.

### Access Data
Click this link below:

      1. Ministry of Agriculture
      
      2. Food Ingredients and Recipe Dataset

### Scope of the project

1.  Ingredient-Based Recommendations:  Develop an algorithm that analyzes user-provided ingredients to recommend recipes based on ingredient similarity, leveraging a diverse dataset that includes recipe_Title, Ingredients, and Instructions for authentic African and global dishes.

2.  User-Friendly Interface:  Design an intuitive web interface that enables users to input their available ingredients and view tailored recipe recommendations, along with detailed cooking instructions and a feedback mechanism to enhance recommendation accuracy.

## Data Preparation

### Data Frame one

The dataset contains a CSV file and a zipped folder, consisting of 13,501 rows and 5 columns respectively as follows:

  1. Title:  Represents the Title of the Food Dish.
    
  2. Ingredients:  Contains the ingredients as they were scraped from the website.
    
  3. Instructions:  Has the recipe instructions to be followed to recreate the dish.
    
  4. Image_Name:  Has the name of the image as stored in the Food Images zipped folder.
    
  5. Cleaned_Ingredients:  Contains the ingredients after being processed and cleaned.


### Data Frame two

The dataset is CSV file, it contains rows 142 and 16 columns respectively as follows:

  1. Title:  Represents the Title of the Food Dish.
  
  2. Ingredients:  Contains the ingredients as they were scraped from the website.
  
  3. Instructions:  Has the recipe instructions to be followed to recreate the dish.

## Modelling

### Function to get Recipes based on Ingredients

 1.  Applying tokenization in our ingredient column
 
 2.  Defining Function for Ingredients and Title, that is the system is set to work and recommend based on the input, the user can input either title or       the ingredients to get the instruction and title or ingredients which will depend with his input.
 
 3.  Feature Engineering
 
 4.  Intiating TF-IDF Vectorizer to create vectors based on both the recipe title and ingredients.


## Deployment

### Saving Code

In order for a user to get recommended recipes, we need to save some code such as the recommend recipe function, combined_df, the tf_idf vectorizer as .py and pickle files in order for a user to get feedback whenever they input data.

So the TF-IDF Vectorizer and the combined dataframe will be saved as pickle files while the combined_df saved as .py file to make it easy to adjust here and there.
Create a simple front end web application which is user friendly

#### visualization of the web application
<p align="center">
  <img src="https://github.com/MwangiKinyeru/The-Boma-Pot/blob/main/images/home%20preview.PNG" 
  width="45%" />
  <img src="https://github.com/MwangiKinyeru/The-Boma-Pot/blob/main/images/results%20preview.PNG" 
  width="45%" />
</p>

### Future Improvements
intergrate a user friendly chatbot to this web application

>>>> Deployment link: [web_link](https://the-boma-pot.onrender.com)

<br>
Author by:
DS Martin Waweru
  <br>
