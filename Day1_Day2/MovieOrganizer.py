movie_collection = []

def add_movie():
    title = input("Enter movie title: ")
    year = input("Enter release year: ")
    genre = input("Enter genre: ")
    movie = {
        'title': title.strip().title(),
        'year': year.strip(),
        'genre': genre.strip().title()
    }
    movie_collection.append(movie)
    print(f"Movie '{title}' added successfully.")

def view_movies():
    if not movie_collection:
        print("No movies in your collection.")
        return
    print("\nYour Movie Collection:")
    for idx, movie in enumerate(movie_collection, 1):
        print(f"{idx}. {movie['title']} ({movie['year']}) - {movie['genre']}")

def search_movie():
    keyword = input("Enter title keyword to search: ").strip().lower()
    found = [movie for movie in movie_collection if keyword in movie['title'].lower()]
    if found:
        print("\nSearch Results:")
        for movie in found:
            print(f"- {movie['title']} ({movie['year']}) - {movie['genre']}")
    else:
        print("No movies found with that keyword.")

def delete_movie():
    title = input("Enter the exact title of the movie to delete: ").strip().title()
    for movie in movie_collection:
        if movie['title'] == title:
            movie_collection.remove(movie)
            print(f"Movie '{title}' removed from collection.")
            return
    print(f"No movie found with the title '{title}'.")

def main():
    while True:
        print("\nMovie Organizer Menu:")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Delete Movie")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            view_movies()
        elif choice == '3':
            search_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            print("Exiting Movie Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 5.")

if __name__ == "__main__":
    main()
