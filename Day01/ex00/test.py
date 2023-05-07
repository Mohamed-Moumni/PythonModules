from book import Book
from recipe import Recipe

book = Book("chomicha")

recipe = Recipe("tangia", 2, 40, ["la7em", "zaafrane", "9arfa"], "had l9es ghir dyal s7ab marrakech", "lunch")

book.add_recipe(recipe)

book.get_recipe_by_name("tangia")

book.get_recipes_by_types("lunch")