from flask import Blueprint, render_template, request
import SpoonacularAPI as recipeAPI
import TargetAPI as targetAPI

auth = Blueprint( 'auth', __name__ )

@auth.route("/searchpage")
def search_result():
	return render_template( "searchPage.html" )

@auth.route("/find", methods=['GET', 'POST'])
def find():
	if request.method == "POST":
		search = request.form.get('searchRecipe')
	
	targetCartDict = {}

	result = recipeAPI.RecipeBook( "american", search )
	recipes = list(result.recipeBook.values())

	for recipe in recipes:

		targetCart = targetAPI.TargetCart( 85255 )

		for data in recipe.ingredients.values():
			shoppingItem = targetAPI.QueryTarget( targetCart.storeID, data.name )
			targetCart.addItemToCart( shoppingItem )

		targetCartDict[ recipe.title ] = targetCart

	return render_template('searchResults.html', targetCartDict=targetCartDict, recipes=recipes)
