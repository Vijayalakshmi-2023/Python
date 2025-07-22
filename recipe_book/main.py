# main.py

from recipe_io import (
    add_recipe, remove_recipe, modify_recipe,
    search_by_ingredient, list_all_recipes, get_recipe
)

# Recipe book and category store
recipes = {}
categories = set()

# Add sample recipes
add_recipe(recipes, "Pasta", ["noodles", "sauce"], ["Boil noodles", "Add sauce"], "Italian", categories)
add_recipe(recipes, "Omelette", ["eggs", "salt", "pepper"], ["Beat eggs", "Cook in pan"], "Breakfast", categories)

# List all recipes
print("📒 All Recipes:")
for name in list_all_recipes(recipes):
    print(f"- {name}")

# Show full recipe
print("\n📖 Recipe: Pasta")
ingredients, steps = get_recipe(recipes, "Pasta")
print("Ingredients:", ", ".join(ingredients))
print("Steps:")
for i, step in enumerate(steps, 1):
    print(f"  {i}. {step}")

# Search by ingredient
print("\n🔍 Recipes with 'eggs':")
found = search_by_ingredient(recipes, "eggs")
print(", ".join(found) if found else "No matches found.")

# Modify a recipe
print("\n✏️ Modifying 'Omelette' to include onions...")
modify_recipe(recipes, "Omelette", ingredients=["eggs", "salt", "pepper", "onion"])

# Remove a recipe
print("\n🗑️ Removing 'Pasta'...")
if remove_recipe(recipes, "Pasta"):
    print("Removed successfully.")
else:
    print("Recipe not found.")

# List categories
print("\n📂 Recipe Categories:")
print(", ".join(categories))
