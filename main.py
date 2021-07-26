import requests
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/', methods = ["POST", "GET"])
@app.route('/home', methods = ["POST", "GET"])
def home():
        return render_template('home.html')

@app.route('/about')
def about():

    if __name__ == '__main__':
     app.run(debug=True)


    class Ingredient:
        def __init__(self, ingredient):
            self.ingredient = ingredient
            self.name = ingredient.get("name")
            self.amount = ingredient.get("amount")
            self.measurement = ingredient.get("unitLong")
            self.image = ingredient.get("image")


    class Recipe:
        def __init__(self, recipe):
            self.recipe = recipe
            self.name = recipe.get("name")
            self.image = recipe.get("image")
            self.readyInMinutes = recipe.get("readyInMinutes")
            self.summary = recipe.get("summary")
            self.ingredients = {}
            self.steps = {}
            self.addIngredient()

        def addIngredient(self):
            for ingredient in self.recipe.get("missedIngredients"):
                ingredientClass = Ingredient(ingredient)
                self.ingredients[ingredientClass.name] = ingredientClass


    class RecipeBook:
        def __init__(self, cuisine, keyword):
            # What gets returned from the API
            self.recipes = {}

            # This will be the one we use to pull information easily from the mess of a return
            self.recipeBook = {}
            self.cuisine = cuisine
            # we can later make it get random recipe if nothing is searched.
            self.keyword = keyword
            self.findRecipes()
            self.addRecipe()

        def findRecipes(self):
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex"

            querystring = {"limitLicense": "false", "offset": "0", "number": "10", "intolerances": "",
                           "instructionsRequired": "true", "ranking": "2", "addRecipeInformation": "true",
                           "fillIngredients": "true", "excludeIngredients": "", "cuisine": self.cuisine,
                           "query": self.keyword, "includeIngredients": "", "type": "main course"}

            headers = {
                'x-rapidapi-key': "25c9120b91mshda2f6434b6ba640p12800cjsn7e5efc1cb1b3",
                'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            self.recipes = response.json()

        def addRecipe(self):
            # make a for loop to loop over recipee
            for recipe in self.recipes.get("results"):
                recipeClass = Recipe(recipe)
                self.recipeBook[recipe.get("title")] = recipeClass


    # Can add more terms later.  But its (cuiseine, keyword)
    result = RecipeBook("american", "burger")
    print(result.recipeBook)
    print("\n\n\n\n")

    # To get ingredients of a recipe
    for value in result.recipeBook.values():
        print(value.name)
        print(value.ingredients)
        print("\n\n")

        # To get the quantities of each ingredient
        for amount in value.ingredients.values():
            print(amount.name)
            print(amount.amount, " ", amount.measurement)



