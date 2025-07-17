# FrozenSet for Immutable Data

# Define meal combinations using frozenset (immutable)
meal_combinations = {
    frozenset({"eggs", "bacon", "toast"}): "Breakfast Combo 1",
    frozenset({"salad", "chicken", "bread"}): "Lunch Combo 2",
    frozenset({"steak", "potatoes", "wine"}): "Dinner Combo 3",
}

# Function to retrieve meal name by ingredient set
def get_meal_name(ingredients):
    # Convert ingredients to frozenset for lookup
    key = frozenset(ingredients)
    return meal_combinations.get(key, "Meal combination not found")

# Example usage:
ingredients1 = {"eggs", "toast", "bacon"}
ingredients2 = {"salad", "bread"}

print(get_meal_name(ingredients1))  # Output: Breakfast Combo 1
print(get_meal_name(ingredients2))  # Output: Meal combination not found
