# suggestion_engine.py

def suggest_activities(destination):
    suggestions = {
        "Paris": ["Visit Montmartre", "Try French pastries"],
        "Tokyo": ["Go to Shibuya Crossing", "Eat at a sushi bar"],
        "New York": ["Walk Central Park", "Broadway show"]
    }
    return suggestions.get(destination, ["Explore local attractions"])
