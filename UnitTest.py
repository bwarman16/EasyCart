import unittest
from unittest.mock import Mock, patch

import TargetAPI as Target
import SpoonacularAPI as Spoonacular


class TestTargetAPI(unittest.TestCase):
    @patch('TargetAPI.TargetCart')
    def test_location(self, mock_get):
        mock_get.storeID = "935"
        self.assertEqual(mock_get.storeID, "935")

    def test_query(self):
        result = Target.QueryTarget("936", "Bacon")
        self.assertIsNot(result.itemName, "")


class TestSpoonacular(unittest.TestCase):
    def test_recipes(self):
        recipes = Spoonacular.RecipeBook("American", "burger")
        self.assertIsNot(len(recipes.recipes.get("results")), 0)
        for recipe in recipes.recipeBook.values():
            self.assertIsNot(len(recipe.ingredients), 0)

            for ingredient in recipe.ingredients.values():
                self.assertIsNotNone(ingredient.name)


if __name__ == '__main__':
    unittest.main()
