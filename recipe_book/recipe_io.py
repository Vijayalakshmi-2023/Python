# recipe_io.py

def add_recipe(book, name, ingredients, steps, category, categories):
    book[name] = (ingredients, steps)
    categories.add(category)

def remove_recipe(book, name):
    if name in book:
        del book[name]
        return True
    return False

def modify_recipe(book, name, ingredients=None, steps=None):
    if name in book:
        current_ingredients, current_steps = book[name]
        book[name] = (
            ingredients if ingredients is not None else current_ingredients,
            steps if steps is not None else current_steps
        )
        return True
    return False

def search_by_ingredient(book, ingredient):
    results = []
    for name, (ingredients, _) in book.items():
        if ingredient.lower() in (ing.lower() for ing in ingredients):
            results.append(name)
    return results

def list_all_recipes(book):
    return list(book.keys())

def get_recipe(book, name):
    return book.get(name, None)
