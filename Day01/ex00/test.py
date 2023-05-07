import typing

class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list[str], description: str, recipe_type: str) -> None:
        