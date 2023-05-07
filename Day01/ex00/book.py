from datetime import datetime
import typing

class Book:
    def __init__(self, name: str) -> None:
        if len(name) == 0:
            raise ValueError("Name Error")
        self.name = name
        self.creation_date = self.last_update = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""

        for re_type in self.recipes_list:
            for recipe in self.recipes_list[re_type]:
                if name == recipe.name:
                    print(str(recipe))
                    return recipe
        return None

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        
        for recipe_elem in self.recipes_list[recipe_type]:
            print(recipe_elem.name)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        
        self.recipes_list[recipe.recipe_type].append(recipe)        