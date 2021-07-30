import requests


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
        self.title = recipe.get("title")
        self.image = recipe.get("image")
        self.readyInMinutes = recipe.get("readyInMinutes")
        self.summary = recipe.get("summary")
        self.ingredients = {}
        self.steps = {}
        self.sourceUrl = recipe.get("sourceUrl")
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
