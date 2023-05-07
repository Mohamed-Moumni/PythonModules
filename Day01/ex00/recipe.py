import typing


class Recipe:
    def __init__(self, name: str,
                 cooking_lvl: int,
                 cooking_time: int,
                 ingredients: list[str],
                 description: str,
                 recipe_type: str) -> None:
        if len(name) == 0:
            raise ValueError("Empty name attribute")
        self.name = name
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("Cooking level out of range")
        self.cooking_lvl = cooking_lvl
        if cooking_time < 0:
            raise ValueError("No Negative Cooking time")
        self.cooking_time = cooking_time
        if len(ingredients) == 0:
            raise ValueError("Invalid ingredients")
        for ingre in ingredients:
            if type(ingre) != str:
                raise ValueError("Invalid typedients")
        self.ingredients = ingredients
        self.description = description
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Recipe type is Invalid")
        self.recipe_type = recipe_type
    
    def __str__(self) -> str:
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "name: " + self.name + "\n"
        txt += "cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "cooking time: " + str(self.cooking_time) + "\n"
        txt += "ingredients: " + str(self.ingredients) + "\n"
        txt += "description: " + self.description + "\n"
        txt += "type: " + self.recipe_type
        return txt
# try:
#     recipe = Recipe("tangia", 2, 40, ["la7em", "zaafrane", "9arfa"], "had l9es ghir dyal s7ab marrakech", "lunch")
#     info = str(recipe)
#     print(info)
#     # print(f"name: {recipe.name} cooking level: {recipe.cooking_lvl}  cooking time: {recipe.cooking_time}  ingredients: {recipe.ingredients} description: {recipe.description} type: {recipe.recipe_type}")
# except ValueError as err:
#     print("", err)
