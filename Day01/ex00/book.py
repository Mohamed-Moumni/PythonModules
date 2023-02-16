from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            print(f"Invalid name type {name}")
            return
        if name == "":
            print(f"The name field is empty {name}")
            return
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [],
                             "lunch": [],
                             "dessert": []}

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} \
            and returns the instance"""
        print(f"The of the recipe is : {name}")
        for elem in self.recipes_list:
            for val in self.recipes_list[elem]:
                if val.name == name:
                    return val

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        recipe_names = []
        for elem in self.recipes_list:
            if elem == recipe_type:
                for val in self.recipes_list[elem]:
                    recipe_names.append(val.name)
        return recipe_names

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print(f"Invalid recipe type")
            return
        for elem in self.recipes_list:
            if elem == recipe.recipe_type:
                self.recipes_list[elem].append(recipe)
        self.last_update = datetime.now()
