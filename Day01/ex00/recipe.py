class Recipe:
    def __init__(self,
                 name,
                 cooking_lvl,
                 cooking_time,
                 ingredients,
                 description,
                 recipe_type):
        if type(name) != str:
            print(f"Invalid type of name {name}")
            return
        if name == "":
            print(f"Empty Name Given")
            return
        if type(cooking_lvl) != int:
            print(f"Invalid type of cooking_lvl {cooking_lvl}")
            return
        if cooking_lvl < 1 or cooking_lvl > 5:
            print(f"The cooking level is out of range {cooking_lvl}")
            return
        if type(cooking_time) != int:
            print(f"Invalid type of cooking_time {cooking_time}")
            return
        if cooking_time < 0:
            print(f"The cooking time is negative {cooking_time}")
            return
        if not isinstance(ingredients, list):
            print(f"Invalid type of ingredients {ingredients}")
            return
        if ingredients == []:
            print(f"Empty list {ingredients}")
            return
        for ingredient in ingredients:
            if not isinstance(ingredient, str):
                print(f"Invalid type of ingredient in \
                       list of ingredients{ingredient}")
                return
        if not isinstance(description, str):
            print(f"Invalid type of description {description}")
            return
        if not isinstance(recipe_type, str):
            print(f"Invalid type of recipe_type {recipe_type}")
            return
        if recipe_type == "":
            print(f"The recipe_type is empty {recipe_type}")
            return
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print(f"The recipe_type is invalid {recipe_type}")
            return
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "Name: {}".format(self.name)
        txt += "cooking level: {}\n".format(self.cooking_lvl)
        txt += "cooking time: {}\n".format(self.cooking_time)
        txt += "ingredients : {}\n".format(self.ingredients)
        txt += "description : {}\n".format(self.description)
        txt += "recipe type : {}".format(self.recipe_type)
        return txt
