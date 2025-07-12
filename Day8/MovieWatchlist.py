# Movie Watchlist App
watchlist = []

def show_menu():
    print("\n🎬 Movie Watchlist Menu")
    print("1. View watchlist")
    print("2. Add a movie")
    print("3. Mark a movie as watched")
    print("4. Show top 5 movies to watch")
    print("5. Exit")

def view_watchlist():
    if not watchlist:
        print("Your watchlist is empty.")
    else:
        print("\n📺 Your Watchlist:")
        for idx, movie in enumerate(watchlist, start=1):
            print(f"{idx}. {movie}")

def add_movie():
    movie = input("Enter movie title to add: ").strip()
    watchlist.append(movie)
    print(f"✅ '{movie}' added to your watchlist.")

def mark_as_watched():
    view_watchlist()
    if watchlist:
        try:
            number = int(input("Enter the movie number to mark as watched: "))
            if 1 <= number <= len(watchlist):
                removed = watchlist.pop(number - 1)
                print(f"🎉 You watched '{removed}'. Removed from watchlist.")
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

def show_top_movies():
    if watchlist:
        print("\n🔥 Top 5 Movies to Watch:")
        for movie in watchlist[:5]:  # Top 5 using slicing
            print("-", movie)
    else:
        print("No movies in your watchlist.")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1–5): ")

    if choice == "1":
        view_watchlist()
    elif choice == "2":
        add_movie()
    elif choice == "3":
        mark_as_watched()
    elif choice == "4":
        show_top_movies()
    elif choice == "5":
        print("Goodbye! Enjoy your movies 🎥")
        break
    else:
        print("Invalid choice. Please try again.")
