# Daily Meal Planner

# Initialize meal plan for the week
meal_plan = [
    ["Monday", "Idly"],
    ["Tuesday", "Dosa"],
    ["Wednesday", "Chapati"],
    ["Thursday", "Rice"],
    ["Friday", "Pasta"],
    ["Saturday", "Pizza"],
    ["Sunday", "Burger"]
]

def display_meals(plans):
    print("\n📅 Weekly Meal Plan:")
    for day, meal in plans:
        print(f"{day}: {meal}")

def update_meal():
    day = input("Enter the day to update meal for: ").strip().capitalize()
    # Find the day in meal_plan
    for i, (d, m) in enumerate(meal_plan):
        if d == day:
            new_meal = input(f"Enter new meal for {day}: ").strip().capitalize()
            meal_plan[i][1] = new_meal
            print(f"✅ Meal for {day} updated to {new_meal}.")
            return
    print("❌ Day not found.")

def remove_meal():
    day = input("Enter the day to remove meal from: ").strip().capitalize()
    for i, (d, m) in enumerate(meal_plan):
        if d == day:
            meal_plan[i][1] = "No meal planned"
            print(f"🗑️ Meal removed for {day}.")
            return
    print("❌ Day not found.")

def view_weekend():
    # Assuming weekend is Saturday and Sunday
    weekend = meal_plan[-2:]
    print("\n🌞 Weekend Meal Plan:")
    for day, meal in weekend:
        print(f"{day}: {meal}")

def main():
    while True:
        print("\n🍽️ Daily Meal Planner Menu")
        print("1. View all meals")
        print("2. Update a meal")
        print("3. Remove a meal")
        print("4. View weekend meals")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            display_meals(meal_plan)
        elif choice == "2":
            update_meal()
        elif choice == "3":
            remove_meal()
        elif choice == "4":
            view_weekend()
        elif choice == "5":
            print("👋 Exiting Meal Planner. Bon Appétit!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
