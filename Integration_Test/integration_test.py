import testFile as test
import SpoonacularAPI as recipeAPI
import TargetAPI as targetAPI

class TestClass:
	def test_1(self):
		result = recipeAPI.RecipeBook( "american", "chicken" )
		recipes = list(result.recipeBook.values())[0]

		targetCart = targetAPI.TargetCart( 85255 )

		for data in recipe.ingredients.values():
			shoppingItem = targetAPI.QueryTarget( targetCart.storeID, data.name )
			targetCart.addItemToCart( shoppingItem )

		assert targetCart != None

	def test_2(self):
		result = recipeAPI.RecipeBook( "american", "egg" )
		recipes = list(result.recipeBook.values())[0]

		assert recipes.title == "egg"

	def test_3(self):
		result = recipeAPI.RecipeBook( "american", "chicken" )
		recipes = list(result.recipeBook.values())[0]

		targetCart = targetAPI.TargetCart( 85255 )

		for data in recipe.ingredients.values():
			shoppingItem = targetAPI.QueryTarget( targetCart.storeID, data.name )
			targetCart.addItemToCart( shoppingItem )

		assert targetCart.price.values() != None

	def test_4(self):
		result = recipeAPI.RecipeBook( "american", "bread" )
		recipes = list(result.recipeBook.values())[0]

		assert recipes.image != None

	def test_5(self):
		result = recipeAPI.RecipeBook( "american", "fish" )
		recipes = list(result.recipeBook.values())[0]

		assert recipes.sourceUrl != None