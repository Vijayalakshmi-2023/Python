# Recipe Ingredient Matcher

# Ingredients available at home
available_ingredients = {"eggs", "flour", "milk", "sugar", "butter"}

# Ingredients required by the recipe
required_ingredients = {"flour", "milk", "eggs", "baking powder", "vanilla"}

# Check if all required ingredients are available
if available_ingredients.issuperset(required_ingredients):
    print("You have all the ingredients for the recipe!")
else:
    missing = required_ingredients.difference(available_ingredients)
    print("You're missing these ingredients:", missing)
