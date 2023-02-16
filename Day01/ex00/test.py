from book import Book
from recipe import Recipe


recipe1 = Recipe("sandwich", 2, 30, ['sauce', 'tomatoes', 'meat', 'ketchup'], "",'lunch')
recipe2 = Recipe("hamborger", 2, 30, ['sauce', 'tomatoes', 'meat', 'ketchup'], "",'lunch')
recipe3 = Recipe("tagine", 2, 30, ['sauce', 'tomatoes', 'meat', 'ketchup'], "",'lunch')

book = Book("Chef Moha")

book.add_recipe(recipe1)
print(f"creation time : {book.creation_date} , update time : {book.last_update}")
book.add_recipe(recipe2)
book.add_recipe(recipe3)
print(f"creation time : {book.creation_date} , update time : {book.last_update}")

found = book.get_recipe_by_name('hamborger')

print(found)