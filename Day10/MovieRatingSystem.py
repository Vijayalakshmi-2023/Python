# Format: {movie_name: {"ratings": [int, int, ...], "genre": ..., "avg_rating": float}}
movies = {
    "Inception": {"ratings": [5, 4, 5, 5], "genre": "Sci-Fi", "avg_rating": 4.75},
    "Titanic": {"ratings": [4, 5, 3, 4], "genre": "Romance", "avg_rating": 4.0},
    "The Dark Knight": {"ratings": [5, 5, 5, 5], "genre": "Action", "avg_rating": 5.0},
    "Avengers: Endgame": {"ratings": [5, 4, 4, 4], "genre": "Action", "avg_rating": 4.25},
}
# Add or update ratings for a movie
def add_rating(movie_name, rating):
    if movie_name in movies:
        movies[movie_name]["ratings"].append(rating)
        print(f"Added rating {rating} for '{movie_name}'.")
    else:
        print(f"Movie '{movie_name}' not found.")

    # Recalculate the average rating after adding a new rating
    recalculate_avg_rating(movie_name)

# Recalculate average rating for a movie
def recalculate_avg_rating(movie_name):
    movie = movies.get(movie_name)
    if movie:
        avg_rating = sum(movie["ratings"]) / len(movie["ratings"])
        movie["avg_rating"] = round(avg_rating, 2)
        print(f"Recalculated average rating for '{movie_name}': {movie['avg_rating']}")
    else:
        print(f"Movie '{movie_name}' not found.")

# Sort movies by average rating
def sort_movies_by_rating():
    sorted_movies = sorted(movies.items(), key=lambda x: x[1]["avg_rating"], reverse=True)
    print("\nMovies sorted by average rating:")
    for movie_name, data in sorted_movies:
        print(f"  {movie_name} - Avg Rating: {data['avg_rating']}")

# Filter movies by genre using dictionary comprehension
def filter_movies_by_genre(genre):
    filtered_movies = {movie_name: data for movie_name, data in movies.items() if data["genre"].lower() == genre.lower()}
    print(f"\nMovies of genre '{genre}':")
    if filtered_movies:
        for movie_name, data in filtered_movies.items():
            print(f"  {movie_name} - Avg Rating: {data['avg_rating']}")
    else:
        print(f"No movies found for the genre '{genre}'.")
# Add a rating for 'Inception'
add_rating("Inception", 4)

# Add a rating for 'Titanic'
add_rating("Titanic", 4)

# Sort movies by their average rating
sort_movies_by_rating()

# Filter movies by genre (e.g., Action)
filter_movies_by_genre("Action")

# Filter movies by genre (e.g., Romance)
filter_movies_by_genre("Romance")
