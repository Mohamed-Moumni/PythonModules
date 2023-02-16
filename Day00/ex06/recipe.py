cookbook = {
    'Sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'launch', 'prep_time': 10},
    'Cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
    'Salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'launch', 'prep_time': 15}
}

def print_recipes_name(cookbook):
    for name in cookbook:
        print(name)

def print_recipe_details(cookbook, recipe):
    if (recipe in cookbook):
        print(f"Name: {recipe}")
        print(f"Ingredients: {cookbook[recipe]['ingredients']}")
        print(f"Meal: {cookbook[recipe]['meal']}")
        print(f"prep_time: {cookbook[recipe]['prep_time']}")
    else:
        print(f"{recipe} not found in cookbook")

def delete_recipe(cookbook, recipe):
    if (recipe in cookbook):
        cookbook.pop(recipe)
    else:
        print(f"{recipe} not found in cookbook")

def add_recipe(cookbook):
    name = input("Enter a name: ")
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient: ")
        if ingredient == "":
            break
        else:
            ingredients.append(ingredient)
    cookbook[name] = {}
    cookbook[name]['ingredients'] = ingredients
    meal_type = input("Enter a meal type: ")
    cookbook[name]['meal'] = meal_type
    prep_time = input("Enter a preparation time: ")
    cookbook[name]['prep_time'] = prep_time

if __name__ == '__main__':
    print("Welcome To The Python Cookbook !")
    while True:
        print("List of available option:")
        req = input("   1: Add a recipe\n   2: Delete a recipe\n   3: Print a recipe\n   4: Print the Cookbook\n   5: Quit\n")
        print("Please select an option")
        if (int(req) == 1):
            recipe = input("Please Enter a recipe name to add it to the cookbook ")
            add_recipe(cookbook)
        elif int(req) == 2:
            recipe = input("Please Enter a recipe name to delete from the cookbook ")
            delete_recipe(cookbook, recipe)
        elif int(req) == 3:
            recipe = input("Please Enter a recipe name to add it to print its details ")
            print_recipe_details(cookbook, recipe)
        elif int(req) == 4:
            recipe = input("Please the the name of the cookbook to print it ")
            print_recipes_name(cookbook)
        elif int(req) == 5:
            print("Thanks for your time ")
            break
        else:
            print("Sorry, this option does not exist ")
# add_recipe(cookbook)
# print_recipe_details(cookbook, 'Tangia')
# delete_recipe(cookbook, 'Cake')
# print_recipes_name(cookbook)
