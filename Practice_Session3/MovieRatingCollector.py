# List to store movie data: [movie_name, rating]
movies = []

# Function to add a movie and rating
def add_movie():
    name = input("🎬 Enter movie name: ").strip()
    try:
        rating = float(input("⭐ Enter rating (0.0 to 10.0): "))
        if 0 <= rating <= 10:
            movies.append([name, rating])
            print(f"✅ '{name}' added with rating {rating}/10\n")
        else:
            print("❌ Rating must be between 0 and 10.\n")
    except ValueError:
        print("❌ Invalid input. Please enter a number.\n")

# Function to display all movies
def show_all_movies():
    if not movies:
        print("📭 No movies rated yet.\n")
        return
    print("\n🎞️ All Movie Ratings:")
    for i, (name, rating) in enumerate(movies, start=1):
        print(f"{i}. {name} - {rating}/10")
    print()

# Function to show top-rated movies
def show_top_movies():
    if not movies:
        print("📭 No movies to compare.\n")
        return
    # Sort by rating descending
    sorted_movies = sorted(movies, key=lambda x: x[1], reverse=True)
    print("\n🏆 Top Rated Movies:")
    for i, (name, rating) in enumerate(sorted_movies[:5], start=1):  # top 5
        print(f"{i}. {name} - {rating}/10")
    print()

# Main menu loop
def main():
    while True:
        print("=== Movie Rating Collector ===")
        print("1. Add Movie Rating")
        print("2. Show All Movies")
        print("3. Show Top Rated Movies")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_movie()
        elif choice == "2":
            show_all_movies()
        elif choice == "3":
            show_top_movies()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

# Run the app
main()
